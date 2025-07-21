from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column13(BaseStep):
    _column_name = "herbář"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:
        return f"herb{str(row.get('Herbar_S', '')).strip()}"

