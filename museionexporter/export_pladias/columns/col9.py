from .base import BaseStep
import pandas


class Column9(BaseStep):
    _column_name = "přesnost souřadnic"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Souř. přesnost"].copy()
        return pandas.DataFrame({self._column_name: series})
