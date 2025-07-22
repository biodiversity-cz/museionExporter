from .base import BaseStep
import pandas


class OccurenceId(BaseStep):
    _column_name = "occurrenceID"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Inventární číslo"].copy()
        return pandas.DataFrame({self._column_name: series})