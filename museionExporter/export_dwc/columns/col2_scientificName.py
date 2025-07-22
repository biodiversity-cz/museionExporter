from .base import BaseStep
import pandas


class ScientificName(BaseStep):
    _column_name = "scientificName"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Taxon-nomen"].copy()
        return pandas.DataFrame({self._column_name: series})