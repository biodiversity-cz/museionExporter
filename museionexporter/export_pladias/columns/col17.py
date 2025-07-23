from .base import BaseStep
import pandas


class Column17(BaseStep):
    _column_name = "herbářové ID"

    def compute(self) -> pandas.DataFrame:
        def format_herbarium(row):
            herbarium = row['Herbář']
            specimen_id = row['Inventární číslo']
            text = f"{herbarium} {specimen_id}"
            return text.strip()

        result = self._data.apply(format_herbarium, axis=1)
        return pandas.DataFrame({self._column_name: result})