from .base import BaseStep
import pandas


class VerbatimIdentification(BaseStep):
    _column_name = "verbatimIdentification"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Originální jméno"].copy()
        return pandas.DataFrame({self._column_name: series})

