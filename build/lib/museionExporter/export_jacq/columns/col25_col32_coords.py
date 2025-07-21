from .base import BaseStep
import pandas
import re

class Columns25_32_coords(BaseStep):

    _column_names = ["coord_NS","lat_degree","lat_minute","lat_second","coord_WE","long_degree","long_minute","long_second"]

    def compute(self) -> pandas.DataFrame:
        def parse_coord(value):
            if not value or pandas.isna(value):
                return [None, None, None, None]
            if len(value) == 8 and value[1] == '0':
                raw = value[0] + value[2:]
            else:
                raw = value

            cleaned = re.sub(r'[?#\s]', '', str(raw).strip())

            if not cleaned or len(cleaned) < 3:
                return [None] * 4

            direction = cleaned[0].upper()
            if direction not in {'N', 'S', 'E', 'W'}:
                return ['Neznámý směr'] + [None] * 3

            digits = cleaned[1:]
            if not digits[:2].isdigit():
                return ['Chyba ve stupních'] + [None] * 3

            try:
                deg = int(digits[0:2])
                min_ = int(digits[2:4]) if len(digits) >= 4 else None
                sec = int(digits[4:]) if len(digits) == 6 else None
            except ValueError:
                return ['Chyba při převodu'] + [None] * 3

            return [direction, deg, min_, sec]



        def parse_row(row):
            grid = str(row.get('Grid_S', '')).strip()

            if not grid:
                return [None] * 8

            if grid != 'WGS-84':
                return [f"Nepodporovaný systém: {grid}"] + [None] * 7

            lat = parse_coord(row.get('ZSirka_S', ''))
            lon = parse_coord(row.get('ZDelka_S', ''))

            return lat + lon

        self._sbirky['Grid_'] = self._sbirky['Grid_S'].fillna('')
        self._sbirky['ZSirka_S'] = self._sbirky['ZSirka_S'].fillna('')
        self._sbirky['ZDelka_S'] = self._sbirky['ZDelka_S'].fillna('')
        result = self._sbirky.apply(parse_row, axis=1, result_type='expand')
        result.columns = self._column_names
        return result
