from museionexporter.export_dwc.columns.base import BaseStep
import pandas


class Id(BaseStep):
    _column_name = "id"

    def compute(self) -> pandas.DataFrame:
        result = self._data.apply(
            lambda row: row.get('UUID-SP', ''),
            axis=1
        )
        return pandas.DataFrame({self._column_name: result})