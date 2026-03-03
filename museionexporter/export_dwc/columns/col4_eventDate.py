from .base import BaseStep
import pandas


class EventDate(BaseStep):
    _column_name = "eventDate"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Datace sběru"].copy()
        series = pandas.to_datetime(series, errors="coerce", dayfirst=True).dt.strftime("%Y-%m-%d")
        return pandas.DataFrame({self._column_name: series})

