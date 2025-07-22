from .base import BaseStep
import pandas


class DateIdentified(BaseStep):
    _column_name = "dateIdentified"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Datum určení"].copy()
        pandas.to_datetime(series, errors="coerce").dt.strftime("%Y-%m-%d"),
        return pandas.DataFrame({self._column_name: series})