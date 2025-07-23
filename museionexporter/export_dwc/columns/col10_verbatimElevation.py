from .base import BaseStep
import pandas


class VerbatimElevation(BaseStep):
    _column_name = "verbatimElevation"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Nadmořská výška"].copy()
        return pandas.DataFrame({self._column_name: series})

