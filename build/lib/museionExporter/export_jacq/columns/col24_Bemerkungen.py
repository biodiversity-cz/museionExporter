from .base import BaseStep
import pandas
class Column24_Bemerkungen(BaseStep):

    _column_name="Bemerkungen"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['Pozn_S'] = self._sbirky['Pozn_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: f"{row.get('Pozn_S', '')}".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})
