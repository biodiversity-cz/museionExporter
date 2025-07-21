from .base import BaseStep
import pandas


class Column33_exactness(BaseStep):

    _column_name="exactness"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Souř. přesnost"].copy()
        return pandas.DataFrame({self._column_name: series})
