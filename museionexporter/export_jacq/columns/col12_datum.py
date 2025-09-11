from .base import BaseStep
import pandas

class Column12_datum(BaseStep):

    _column_name="Datum"

    def compute(self) -> pandas.DataFrame:
        datum = self._data["Datace sběru"].copy().fillna('s.d.')
        normalized = datum.apply(self.normalize_date)
        return pandas.DataFrame({self._column_name: normalized})

    def normalize_date(self, value: str) -> str:
        value = value.strip()
        parts = value.split(".")
        parts = [p for p in parts if p]  # odstraní prázdné části (např. po '2.8.1979.')

        if not all(p.isdigit() for p in parts):
            return value  # nebo "" / pd.NA

        if len(parts) == 3:
            # den.měsíc.rok
            day, month, year = parts
            return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
        elif len(parts) == 2:
            # měsíc.rok
            month, year = parts
            return f"{int(year):04d}-{int(month):02d}"
        elif len(parts) == 1:
            # rok
            year = parts[0]
            return f"{int(year):04d}"
        else:
            return value