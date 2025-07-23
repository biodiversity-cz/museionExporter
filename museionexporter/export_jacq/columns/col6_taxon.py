from .base import BaseStep
import pandas

class Column6_taxon(BaseStep):

    _column_name="taxon"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Taxon-nomen"].copy()
        return pandas.DataFrame({self._column_name: series})