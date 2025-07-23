from .base import BaseStep
import pandas


class Column13(BaseStep):
    _column_name = "herbář"

    def compute(self) -> pandas.DataFrame:
        def format_herbarium(row):
            herbarium = row['Herbář']
            text = f"herb{herbarium}"
            return text.strip()

        result = self._data.apply(format_herbarium, axis=1)
        return pandas.DataFrame({self._column_name: result})