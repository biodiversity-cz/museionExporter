from .base import BaseStep
import pandas


class Column17_taxon_alt(BaseStep):
    _column_name = "taxon_alt"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Originální jméno"].copy()
        return pandas.DataFrame({self._column_name: series})