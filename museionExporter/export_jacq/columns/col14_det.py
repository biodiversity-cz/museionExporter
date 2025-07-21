from .base import BaseStep
import pandas

class Column14_det(BaseStep):

    _column_name="det"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Určil"].copy()
        return pandas.DataFrame({self._column_name: series})
