from .base import BaseStep
import pandas

class Columns36_37_altitude(BaseStep):

    _column_names = ["alt_min", "alt_max"]

    def compute(self) -> pandas.DataFrame:
        def parse_coord(row):
            value = row.get('Nadmořská výška', '')

            if not value or pandas.isna(value):
                return [None, None]

            return [value, None]

        result = self._data.apply(parse_coord, axis=1, result_type='expand')
        result.columns = self._column_names
        return result
