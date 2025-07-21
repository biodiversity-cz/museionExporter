from .base import BaseStep
import pandas


class Column4(BaseStep):
    _column_name = "nejbližší obec"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Lokalita - název"].copy()
        return pandas.DataFrame({self._column_name: series})

