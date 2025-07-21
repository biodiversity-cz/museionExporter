from .base import BaseStep
import pandas


class Column7(BaseStep):
    _column_name = "zeměp. souřadnice"

    def compute(self) -> pandas.DataFrame:
        def format_coordinates(row):
            lat = row['Zem. šířka (°)']
            lon = row['Zem. délka (°)']
            if pandas.isna(lat) or pandas.isna(lon):
                return ""
            return f"{lat}, {lon}"

        result = self._data.apply(format_coordinates, axis=1)
        return pandas.DataFrame({self._column_name: result})