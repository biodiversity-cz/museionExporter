from sqlalchemy.engine import row

from .base import BaseStep
import pandas


class Column3(BaseStep):
    _column_name = "lokalita"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['OrigLok_S'] = self._sbirky['OrigLok_S'].fillna('')
        self._sbirky['EkoChar_S'] = self._sbirky['EkoChar_S'].fillna('')
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:
        lokalita = row.get('OrigLok_S', '').strip()
        habitat = row.get('EkoChar_S', '').strip()
        if lokalita and habitat:
            result = f"{lokalita}; {habitat}"
        else:
            result = lokalita or habitat

        return result.strip()
