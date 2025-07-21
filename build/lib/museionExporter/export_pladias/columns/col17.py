from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column17(BaseStep):
    _column_name = "herbářové ID"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:

        por_c = row.get('PorC_S', '')
        lomeni = row.get('Lomeni_S', '')
        if lomeni != '_':
            result = f"{por_c}/{lomeni}"
        else:
            result = por_c

        result_str = str(result)
        if len(result_str) < 7:
            result_str = result_str.zfill(7)
        return f"{str(row.get('Herbar_S', '')).strip()}_{result_str}"

