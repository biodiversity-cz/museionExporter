from .base import BaseStep
import pandas


class Column1(BaseStep):
    _column_name = "Standardní jméno"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Taxon-nomen"].copy()
        return pandas.DataFrame({self._column_name: series})