from .base import BaseStep
import pandas


class OccurrenceRemarks(BaseStep):
    _column_name = "occurrenceRemarks"

    def compute(self) -> pandas.DataFrame:
        series = (
            self._data["Poznámka k nálezu"]
            .copy()
            .astype("string")
            .str.replace(r"[\r\n\t]+", " | ", regex=True)
            .str.replace("\u00a0", " ", regex=False)
            .str.strip()
            .str.replace(r'^\s*(\|\s*)+\s*$', '', regex=True)
            .replace({"": pandas.NA, "nan": pandas.NA, "None": pandas.NA})
        )
        return pandas.DataFrame({self._column_name: series})

