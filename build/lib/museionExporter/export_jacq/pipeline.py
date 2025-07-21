import pandas as pd
from museionExporter.export_jacq.columns.col10_Nummer import Column10_Nummer
from museionExporter.export_jacq.columns.col12_datum import Column12_datum
from museionExporter.export_jacq.columns.col13_Datum2 import Column13_Datum2
from museionExporter.export_jacq.columns.col14_det import Column14_det
from museionExporter.export_jacq.columns.col15_typified import Column15_typified
from museionExporter.export_jacq.columns.col16_typus import Column16_typus
from museionExporter.export_jacq.columns.col17_taxon_alt import Column17_taxon_alt
from museionExporter.export_jacq.columns.col18_nation_engl import Column18_nation_engl
from museionExporter.export_jacq.columns.col19_provinz import Column19_provinz
from museionExporter.export_jacq.columns.col20_fundort import Column20_Fundort
from museionExporter.export_jacq.columns.col21_Fundort_engl import Column21_Fundort_engl
from museionExporter.export_jacq.columns.col22_Habitat import Column22_Habitat
from museionExporter.export_jacq.columns.col23_Habitus import Column23_Habitus
from museionExporter.export_jacq.columns.col24_Bemerkungen import Column24_Bemerkungen
from museionExporter.export_jacq.columns.col2_HerbNummer import Column2_HerbNummer
from museionExporter.export_jacq.columns.col33_exactness import Column33_exactness
from museionExporter.export_jacq.columns.col34_quadrant import Column34_quadrant
from museionExporter.export_jacq.columns.col35_quadrant_sub import Column35_quadrnat_sub
from museionExporter.export_jacq.columns.col36_col37_altitude import Columns36_37_altitude
from museionExporter.export_jacq.columns.col38_digital_image import Column38_digital_image
from museionExporter.export_jacq.columns.col39_digital_image_obs import Column39_digital_image_obs
from museionExporter.export_jacq.columns.col3_collectionID import Column3_CollectionID
from museionExporter.export_jacq.columns.col40_observation import Column40_observation
from museionExporter.export_jacq.columns.col4_Collection import Column4_Collection
from museionExporter.export_jacq.columns.col5_status import Column5_status
from museionExporter.export_jacq.columns.col6_taxon import Column6_taxon
from museionExporter.export_jacq.columns.col7_Sammler import Column7_Sammler
from museionExporter.export_jacq.columns.col8_series import Column8_series
from museionExporter.export_jacq.columns.col9_series_number import Column9_series_number
from museionExporter.export_jacq.columns.col11_alt_number import Column11_alt_number
from museionExporter.export_jacq.columns.col25_col32_coords import Columns25_32_coords
from museionExporter.export_jacq.columns.col1_id import Column1_ID
from museionExporter.workers.mdb_reader import read_table

class Pipeline:
    TBL_SBIRKY = "Sbirky"
    TBL_LOKALITY = "Lokality"
    TBL_ADRESAR = "Adresar"
    TBL_URCENI = "Urceni"
    _steps = [
        Column1_ID(),
        Column2_HerbNummer(),
        Column3_CollectionID(),
        Column4_Collection(),
        Column5_status(),
        Column6_taxon(),
        Column7_Sammler(),
        Column8_series(),
        Column9_series_number(),
        Column10_Nummer(),
        Column11_alt_number(),
        Column12_datum(),
        Column13_Datum2(),
        Column14_det(),
        Column15_typified(),
        Column16_typus(),
        Column17_taxon_alt(),
        Column18_nation_engl(),
        Column19_provinz(),
        Column20_Fundort(),
        Column21_Fundort_engl(),
        Column22_Habitat(),
        Column23_Habitus(),
        Column24_Bemerkungen(),
        Columns25_32_coords(),
        Column33_exactness(),
        Column34_quadrant(),
        Column35_quadrnat_sub(),
        Columns36_37_altitude(),
        Column38_digital_image(),
        Column39_digital_image_obs(),
        Column40_observation()
    ]

    def __init__(self, path: str):
        self._tbl_Sbirky = read_table(path, self.TBL_SBIRKY)
        self._tbl_Lokality = read_table(path, self.TBL_LOKALITY)
        self._tbl_Adresar = read_table(path, self.TBL_ADRESAR)
        self._tbl_Urceni = read_table(path, self.TBL_URCENI)

        self._tbl_Sbirky = self._tbl_Sbirky.sort_values(by='PorC_S').reset_index(drop=True)
        self._tbl_Sbirky['Grid_S'] = self._tbl_Sbirky['Grid_S'].fillna('')
        self._tbl_Adresar['Jmeno_A'] = self._tbl_Adresar['Jmeno_A'].fillna('')

    def run(self) -> pd.DataFrame:
        all_dataframes = []
        for step in self._steps:
            df = step.proceed(self._tbl_Sbirky, self._tbl_Lokality, self._tbl_Adresar, self._tbl_Urceni)
            all_dataframes.append(df)

        final_df = pd.concat(all_dataframes, axis=1)

        return final_df
