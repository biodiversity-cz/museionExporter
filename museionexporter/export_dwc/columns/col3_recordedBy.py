from .base import BaseStep
import pandas


class RecordedBy(BaseStep):
    _column_name = "recordedBy"

    def compute(self) -> pandas.DataFrame:
        series = self._data["(n) Autoři/sběratelé"].copy()
        return pandas.DataFrame({self._column_name: series})