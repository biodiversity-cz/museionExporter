from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column10(BaseStep):
    _column_name = "datum"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['DatSberu_S'] = self._sbirky['DatSberu_S'].fillna('s.d.')

        result = self._sbirky.apply(
            lambda row: str(row.get('DatSberu_S', '')).strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})


