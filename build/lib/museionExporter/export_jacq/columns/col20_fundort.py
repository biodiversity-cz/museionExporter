from .base import BaseStep
import pandas
class Column20_Fundort(BaseStep):

    _column_name="Fundort"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['OrigLok_S'] = self._sbirky['OrigLok_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: f"{row.get('OrigLok_S', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
