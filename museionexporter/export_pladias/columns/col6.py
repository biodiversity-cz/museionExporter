from .base import BaseStep
import pandas


class Column6(BaseStep):
    _column_name = "nadmořská výška"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Nadmořská výška"].copy()
        return pandas.DataFrame({self._column_name: series})