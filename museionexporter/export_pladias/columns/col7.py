from .base import BaseStep
import pandas
import re

class Column7(BaseStep):
    _column_name = "zeměp. souřadnice"

    def compute(self) -> pandas.DataFrame:
        def format_coordinates(row):
            lat = self.parse_coordinate(row['Zem. šířka (°)'])
            lon = self.parse_coordinate(row['Zem. délka (°)'])
            if pandas.isna(lat) or pandas.isna(lon):
                return ""
            return self.decimal_to_dms(lat, lon)

        result = self._data.apply(format_coordinates, axis=1)
        return pandas.DataFrame({self._column_name: result})

    def parse_coordinate(self, value: str) -> float:
        if not isinstance(value, str):
            return None
        value = value.strip().upper().replace("°", "")
        match = re.match(r'^([NE\-SW\s]*)([\d.]+)$', value)
        if not match:
            return None

        prefix, number = match.groups()
        number = float(number)

        if 'S' in prefix or 'W' in prefix or '-' in prefix:
            number = -abs(number)
        return number

    def decimal_to_dms(self, lat: float, lon: float) -> str:
        def to_dms(degree: float, is_lat: bool) -> str:
            direction = ''
            if is_lat:
                direction = 'N' if degree >= 0 else 'S'
            else:
                direction = 'E' if degree >= 0 else 'W'

            degree = abs(degree)
            d = int(degree)
            m_float = (degree - d) * 60
            m = int(m_float)
            s = round((m_float - m) * 60, 1)

            return f"{d}°{m:02d}'{s:04.1f}\"{direction}"

        return f"{to_dms(lat, is_lat=True)}, {to_dms(lon, is_lat=False)}"
