from .base import BaseStep
import pandas


class Column2(BaseStep):
    _column_name = "taxon_alt"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Originální jméno"].copy()
        return pandas.DataFrame({self._column_name: series})