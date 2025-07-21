from .base import BaseStep
import pandas


class Column14(BaseStep):
    _column_name = "fytochorion"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Fytochorion - kód"].copy()
        return pandas.DataFrame({self._column_name: series})

