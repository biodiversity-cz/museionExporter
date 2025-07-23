from .base import BaseStep
import pandas

class Column24_Bemerkungen(BaseStep):

    _column_name="Bemerkungen"

    def compute(self) -> pandas.DataFrame:
        series = self._data["Poznámka k nálezu"].copy()
        return pandas.DataFrame({self._column_name: series})
