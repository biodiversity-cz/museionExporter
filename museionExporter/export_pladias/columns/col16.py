from .base import BaseStep
import pandas


class Column16(BaseStep):
    _column_name = "poznámka"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Poznámka k nálezu"].copy()
        return pandas.DataFrame({self._column_name: series})
