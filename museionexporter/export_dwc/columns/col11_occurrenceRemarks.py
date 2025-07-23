from .base import BaseStep
import pandas


class OccurrenceRemarks(BaseStep):
    _column_name = "occurrenceRemarks"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Poznámka k nálezu"].copy()
        series = series.astype(str).str.replace(r'[\r\n\t]+', ' | ', regex=True).str.strip()
        return pandas.DataFrame({self._column_name: series})

