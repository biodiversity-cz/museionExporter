import pandas as pd

from museionexporter.export_pladias.columns.col1 import Column1
from museionexporter.export_pladias.columns.col2 import Column2
from museionexporter.export_pladias.columns.col3 import Column3
from museionexporter.export_pladias.columns.col4 import Column4
from museionexporter.export_pladias.columns.col5 import Column5
from museionexporter.export_pladias.columns.col6 import Column6
from museionexporter.export_pladias.columns.col7 import Column7
from museionexporter.export_pladias.columns.col8 import Column8
from museionexporter.export_pladias.columns.col9 import Column9
from museionexporter.export_pladias.columns.col10 import Column10
from museionexporter.export_pladias.columns.col11 import Column11
from museionexporter.export_pladias.columns.col12 import Column12
from museionexporter.export_pladias.columns.col13 import Column13
from museionexporter.export_pladias.columns.col14 import Column14
from museionexporter.export_pladias.columns.col15 import Column15
from museionexporter.export_pladias.columns.col16 import Column16
from museionexporter.export_pladias.columns.col17 import Column17
from museionexporter.export_pladias.columns.col18 import Column18
from museionexporter.workers.excel_reader import read_table

class Pipeline:
    _steps=[Column1(),
            Column2(),
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

    def __init__(self, path: str):
        self._data = read_table(path)


    def run(self) -> pd.DataFrame:
        all_dataframes = []
        for step in self._steps:
            df = step.proceed(self._data)
            all_dataframes.append(df)

        final_df = pd.concat(all_dataframes, axis=1)

        return final_df
