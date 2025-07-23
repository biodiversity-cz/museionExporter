from .base import BaseStep
import pandas


class Column3(BaseStep):
    _column_name = "lokalita"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Charakteristika místa sběru"].copy()
        return pandas.DataFrame({self._column_name: series})