from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column16(BaseStep):
    _column_name = "poznámka"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Pozn_S'] = self._sbirky['Pozn_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: f"{row.get('Pozn_S', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

