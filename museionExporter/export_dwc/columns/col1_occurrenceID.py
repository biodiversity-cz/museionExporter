from .base import BaseStep
import pandas


class OccurenceId(BaseStep):
    _column_name = "occurrenceID"

    def compute(self) -> pandas.DataFrame:
        def format_id(row):
            specimen_id = row['Inventární číslo']
            herbarium = row['Herbář']
            text = f"{herbarium} {specimen_id}"
            return text.strip()

        result = self._data.apply(format_id, axis=1)
        return pandas.DataFrame({self._column_name: result})