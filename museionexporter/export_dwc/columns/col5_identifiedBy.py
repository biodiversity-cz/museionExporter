from .base import BaseStep
import pandas


class IdentifiedBy(BaseStep):
    _column_name = "identifiedBy"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Určil"].copy()
        series = series.fillna('')
        return pandas.DataFrame({self._column_name: series})

