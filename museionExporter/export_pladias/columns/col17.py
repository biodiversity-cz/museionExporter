from .base import BaseStep
import pandas


class Column17(BaseStep):
    _column_name = "herbářové ID"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Inventární číslo"].copy()
        return pandas.DataFrame({self._column_name: series})

