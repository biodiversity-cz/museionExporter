from .base import BaseStep
import pandas
import re

class Column7_Sammler(BaseStep):

    _column_name="Sammler"

    def compute(self) -> pandas.DataFrame:
        series = self._data["(n) Autoři/sběratelé"].copy()
        return pandas.DataFrame({self._column_name: series})