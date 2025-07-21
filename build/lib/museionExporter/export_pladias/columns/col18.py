from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column18(BaseStep):
    _column_name = "licence"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: 'CC-BY',
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})


