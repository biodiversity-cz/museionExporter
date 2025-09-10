from .base import BaseStep
import pandas

class Columns25_32_coords(BaseStep):

    _column_names = ["coord_NS","lat_degree","lat_minute","lat_second","coord_WE","long_degree","long_minute","long_second"]

    def compute(self) -> pandas.DataFrame:

        def parse_row(row):
            lat_hem, lat_dec = self.parse_coord(row['Zem. šířka (°)'])
            lon_hem, lon_dec = self.parse_coord(row['Zem. délka (°)'])
            if (lat_hem is None) or (lat_dec is None):
                return [None, None, None, None,None, None, None, None]

            lat_deg, lat_min, lat_sec = self.decimal_to_dms(lat_dec)
            lon_deg, lon_min, lon_sec = self.decimal_to_dms(lon_dec)
            return [
                lat_hem, lat_deg, lat_min, lat_sec,
                lon_hem, lon_deg, lon_min, lon_sec
            ]

        result = self._data.apply(parse_row, axis=1, result_type='expand')
        result.columns = self._column_names
        return result

    def decimal_to_dms(self, decimal):
        degrees = int(decimal)
        minutes_full = (decimal - degrees) * 60
        minutes = int(minutes_full)
        seconds = round((minutes_full - minutes) * 60, 1)
        # Ošetření přetečení sekund
        if seconds >= 60:
            seconds = 0
            minutes += 1

        # Ošetření přetečení minut
        if minutes >= 60:
            minutes = 0
            degrees += 1
        return degrees, minutes, seconds

    def parse_coord(self, coord):
        if not isinstance(coord, str):
            return None, None

        coord = coord.strip().replace('°', '')
        parts = coord.split()

        if len(parts) != 2:
            return None, None

        hemisphere = parts[0]
        try:
            value = float(parts[1])
        except ValueError:
            return None, None

        return hemisphere, value



