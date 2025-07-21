from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column14(BaseStep):
    _column_name = "fytochorion"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:

        return f"".strip()

