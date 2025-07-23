from .base import BaseStep
import pandas
class Column2_HerbNummer(BaseStep):

    _column_name="HerbNummer"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Inventární číslo"].copy()
        return pandas.DataFrame({self._column_name: series})