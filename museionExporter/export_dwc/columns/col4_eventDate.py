from .base import BaseStep
import pandas


class EventDate(BaseStep):
    _column_name = "eventDate"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Datace sběru"].copy()
        pandas.to_datetime(series, errors="coerce").dt.strftime("%Y-%m-%d"),
        return pandas.DataFrame({self._column_name: series})

