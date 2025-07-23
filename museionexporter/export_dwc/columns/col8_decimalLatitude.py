from .base import BaseStep
import pandas
import re

class DecimalLatitude(BaseStep):
    _column_name = "decimalLatitude"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Zem. šířka (°)"].copy().apply(self.parse_coordinate)
        return pandas.DataFrame({self._column_name: series})

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
