from .base import BaseStep
import pandas


class Column11(BaseStep):
    _column_name = "nálezce"

    def compute(self) -> pandas.DataFrame:
        series = self._data["(n) Autoři/sběratelé"].copy()
        return pandas.DataFrame({self._column_name: series})

