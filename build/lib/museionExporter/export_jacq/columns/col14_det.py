from .base import BaseStep
import pandas
class Column14_det(BaseStep):

    _column_name="det"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Urcil_S'] = self._sbirky['Urcil_S'].fillna('')

        result = self._sbirky.apply(
            lambda row: self._build_adresar(row.get('Urcil_S', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
