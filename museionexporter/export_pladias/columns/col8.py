from .base import BaseStep
import pandas


class Column8(BaseStep):
    _column_name = "zdroj souřadnic"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Souř. zdroj"].copy()
        return pandas.DataFrame({self._column_name: series})

