from sqlalchemy.engine import row
import re
from .base import BaseStep
import pandas


class Column7(BaseStep):
    _column_name = "zeměp. souřadnice"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Grid_'] = self._sbirky['Grid_S'].fillna('')
        self._sbirky['ZSirka_S'] = self._sbirky['ZSirka_S'].fillna('')
        self._sbirky['ZDelka_S'] = self._sbirky['ZDelka_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:
        grid = str(row.get('Grid_S', '')).strip()

        if not grid:
            return ''

        if grid != 'WGS-84':
            return f"Nepodporovaný systém: {grid}"

        lat = self.parse_coord(row.get('ZSirka_S', ''))
        lon = self.parse_coord(row.get('ZDelka_S', ''))
        if lat != '' and lon != '':
            return f"{lat}, {lon}"
        return ''

    def parse_coord(self, value):
            if len(value) == 8 and value[1] == '0':
                raw = value[0] + value[2:]
            else:
                raw = value

            cleaned = re.sub(r'[?#\s]', '', str(raw).strip())
            if not cleaned or pandas.isna(cleaned) or len(cleaned) != 7:
                return ''

            direction = cleaned[0].upper()
            if direction not in {'N', 'S', 'E', 'W'}:
                return 'Neznámý NSWE'

            digits = re.sub(r'\D', '',cleaned[1:])
            if len(digits) != 6:
                return 'Chyba v číslicích'

            deg = digits[:2]
            min = digits[2:4]
            sec = digits[4:]
            return f"{deg}°{min}'{sec}\"{direction}"

