import pandas as pd

from museionExporter.export_dwc.columns.col10_verbatimElevation import VerbatimElevation
from museionExporter.export_dwc.columns.col11_occurrenceRemarks import OccurrenceRemarks
from museionExporter.export_dwc.columns.col12_verbatimIdentification import VerbatimIdentification
from museionExporter.export_dwc.columns.col1_occurrenceID import OccurenceId
from museionExporter.export_dwc.columns.col2_scientificName import ScientificName
from museionExporter.export_dwc.columns.col3_recordedBy import RecordedBy
from museionExporter.export_dwc.columns.col4_eventDate import EventDate
from museionExporter.export_dwc.columns.col5_identifiedBy import IdentifiedBy
from museionExporter.export_dwc.columns.col6_dateIdentified import DateIdentified
from museionExporter.export_dwc.columns.col7_locality import Locality
from museionExporter.export_dwc.columns.col8_decimalLatitude import DecimalLatitude
from museionExporter.export_dwc.columns.col9_decimalLongitude import DecimalLongitude

from museionExporter.workers.excel_reader import read_table


class Pipeline:
    _steps = [OccurenceId(),
              ScientificName(),
              RecordedBy(),
              EventDate(),
              IdentifiedBy(),
              DateIdentified(),
              Locality(),
              DecimalLatitude(),
              DecimalLongitude(),
              VerbatimElevation(),
              OccurrenceRemarks(),
              VerbatimIdentification()
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
