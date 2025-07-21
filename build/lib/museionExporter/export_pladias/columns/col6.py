from sqlalchemy.engine import row
import re
from .base import BaseStep
import pandas


class Column6(BaseStep):
    _column_name = "nadmořská výška"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['NmVyska_S'] = self._sbirky['NmVyska_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:

        value = row.get('NmVyska_S', '').strip()

        if not value or pandas.isna(value):
            return f""

        # Odstraníme prefixy jako "cca", "~", "přibližně"
        str_val = re.sub(r'(?i)\bcca\b|~|přibližně', '', value).strip()

        # Pokud je rozsah např. "500-550" nebo "500 – 550"
        match = re.match(r'^\s*(\d+)\s*[-–]\s*(\d+)\s*$', str_val)
        if match:
            return f"{match.group(1)}-{match.group(2)}".strip()

        # Najdi jedno číslo
        match = re.search(r'\d+', str_val)
        if match:
            return f"{match.group()}"

        return ''