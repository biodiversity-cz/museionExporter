from .base import BaseStep
import pandas
import re


class DecimalLongitude(BaseStep):
    _column_name = "decimalLongitude"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Zem. délka (°)"].copy().apply(self.parse_coordinate)
        series = series.fillna('')
        return pandas.DataFrame({self._column_name: series})



    def parse_coordinate(self, value: str) -> str:
        if not isinstance(value, str):
            return ''
        value = value.strip().upper().replace("°", "")
        match = re.match(r'^([NE\-SW\s]*)([\d.]+)$', value)
        if not match:
            return ''

        prefix, number = match.groups()
        number = float(number)

        if 'S' in prefix or 'W' in prefix or '-' in prefix:
            number = -abs(number)
        return str(number)
