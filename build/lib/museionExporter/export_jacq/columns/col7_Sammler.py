from .base import BaseStep
import pandas
import re

class Column7_Sammler(BaseStep):

    _column_name="Sammler"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_adresar(row.get('Sberatel_S', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})