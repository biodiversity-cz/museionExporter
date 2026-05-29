from museionexporter.export_dwc.columns.base import BaseStep
import pandas


class VerbatimEventDate(BaseStep):
    _column_name = "verbatimEventDate"

    def compute(self) -> pandas.DataFrame:
        result = self._data.apply(
            lambda row: row.get('Datace sběru', ''),
            axis=1
        )
        return pandas.DataFrame({self._column_name: result})