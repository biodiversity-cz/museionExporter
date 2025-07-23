from .base import BaseStep
import pandas


class Column10(BaseStep):
    _column_name = "datum"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Datace sběru"].copy()
        return pandas.DataFrame({self._column_name: series})

