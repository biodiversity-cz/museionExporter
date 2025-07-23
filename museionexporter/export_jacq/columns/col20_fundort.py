from .base import BaseStep
import pandas

class Column20_Fundort(BaseStep):

    _column_name="Fundort"

    def compute(self) -> pandas.DataFrame:
        def format_locality(row):
            text=''
            obec = row['Lokalita - název']
            popis = row['Charakteristika místa sběru']

            if not pandas.isna(obec):
                text += f"{obec} - "

            if not pandas.isna(popis):
                text += str(popis)

            return text.strip()

        result = self._data.apply(format_locality, axis=1)
        return pandas.DataFrame({self._column_name: result})