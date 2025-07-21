from .base import BaseStep
import pandas
import re

class Columns36_37_altitude(BaseStep):

    _column_names = ["alt_min", "alt_max"]

    def compute(self) -> pandas.DataFrame:
        def parse_coord(row):
            value = row.get('NmVyska_S', '').strip()

            if not value or pandas.isna(value):
                return [None, None]

            # Odstraníme prefixy jako "cca", "~", "přibližně"
            str_val = re.sub(r'(?i)\bcca\b|~|přibližně', '', value).strip()

            # Pokud je rozsah např. "500-550" nebo "500 – 550"
            match = re.match(r'^\s*(\d+)\s*[-–]\s*(\d+)\s*$', str_val)
            if match:
                return [int(match.group(1)), int(match.group(2))]

            # Najdi jedno číslo
            match = re.search(r'\d+', str_val)
            if match:
                return [int(match.group()), None]

            return [None, None]

        self._sbirky['NmVyska_S'] = self._sbirky['NmVyska_S'].fillna('')
        result = self._sbirky.apply(parse_coord, axis=1, result_type='expand')
        result.columns = self._column_names
        return result
