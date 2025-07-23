from .base import BaseStep
import pandas

class Column12_datum(BaseStep):

    _column_name="datum"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Datace sběru"].copy()
        return pandas.DataFrame({self._column_name: series})
