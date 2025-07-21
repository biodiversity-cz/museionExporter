import pandas as pd

from museionExporter.export_jacq.columns.col17_taxon_alt import Column17_taxon_alt
from museionExporter.export_pladias.columns.col1 import Column1
from museionExporter.export_pladias.columns.col3 import Column3
from museionExporter.export_pladias.columns.col4 import Column4
from museionExporter.export_pladias.columns.col5 import Column5
from museionExporter.export_pladias.columns.col6 import Column6
from museionExporter.export_pladias.columns.col7 import Column7
from museionExporter.export_pladias.columns.col8 import Column8
from museionExporter.export_pladias.columns.col9 import Column9
from museionExporter.export_pladias.columns.col10 import Column10
from museionExporter.export_pladias.columns.col11 import Column11
from museionExporter.export_pladias.columns.col12 import Column12
from museionExporter.export_pladias.columns.col13 import Column13
from museionExporter.export_pladias.columns.col14 import Column14
from museionExporter.export_pladias.columns.col15 import Column15
from museionExporter.export_pladias.columns.col16 import Column16
from museionExporter.export_pladias.columns.col17 import Column17
from museionExporter.export_pladias.columns.col18 import Column18
from museionExporter.workers.mdb_reader import read_table

class Pipeline:
    TBL_SBIRKY = "Sbirky"
    TBL_LOKALITY = "Lokality"
    TBL_ADRESAR = "Adresar"
    TBL_URCENI = "Urceni"
    _steps=[Column1(),
            Column17_taxon_alt(),
            Column3(),
            Column4(),
            Column5(),
            Column6(),
            Column7(),
            Column8(),
            Column9(),
            Column10(),
            Column11(),
            Column12(),
            Column13(),
            Column14(),
            Column15(),
            Column16(),
            Column17(),
            Column18(),
            ]

    def __init__(self,path: str):
        self._tbl_Sbirky = read_table(path, self.TBL_SBIRKY)
        self._tbl_Lokality = read_table(path, self.TBL_LOKALITY)
        self._tbl_Adresar = read_table(path, self.TBL_ADRESAR)
        self._tbl_Urceni = read_table(path, self.TBL_URCENI)

        self._tbl_Sbirky = self._tbl_Sbirky.sort_values(by='PorC_S').reset_index(drop=True)
        self._tbl_Sbirky['Var_S'] = self._tbl_Sbirky['Var_S'].fillna('')
        self._tbl_Sbirky['Grid_S'] = self._tbl_Sbirky['Grid_S'].fillna('')
        self._tbl_Adresar['Jmeno_A'] = self._tbl_Adresar['Jmeno_A'].fillna('')

    def run(self) -> pd.DataFrame:
        all_dataframes = []
        for step in self._steps:
            df = step.proceed(self._tbl_Sbirky, self._tbl_Lokality, self._tbl_Adresar, self._tbl_Urceni)
            all_dataframes.append(df)

        final_df = pd.concat(all_dataframes, axis=1)

        return final_df
