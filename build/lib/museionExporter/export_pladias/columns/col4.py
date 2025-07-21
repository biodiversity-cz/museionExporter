from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column4(BaseStep):
    _column_name = "nejbližší obec"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Katastr_S'] = self._sbirky['Katastr_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:
        obec = row.get('Katastr_S', '').strip()

        return f"{obec}"


