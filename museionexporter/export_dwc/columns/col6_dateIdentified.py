from .base import BaseStep
import pandas
import re



class DateIdentified(BaseStep):
    _column_name = "dateIdentified"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Datum určení"].copy().apply(self._parse_date)
        series = series.fillna('')
        return pandas.DataFrame({self._column_name: series})

    def _parse_date(self, value):
        if pandas.isna(value):
            return None

        value = str(value).strip()

        # případ: M.YYYY (např. 8.1933)
        m = re.match(r"^(?P<month>\d{1,2})\.(?P<year>\d{4})$", value)
        if m:
            month = int(m.group("month"))
            year = int(m.group("year"))
            return f"{year:04d}-{month:02d}"

        # případ jen rok
        m = re.match(r"^(?P<year>\d{4})$", value)
        if m:
            return m.group("year")

        # fallback: plné datum
        dt = pandas.to_datetime(value, errors="coerce", dayfirst=True)
        if pandas.isna(dt):
            return None

        return dt.strftime("%Y-%m-%d")