from .base import BaseStep
import pandas


class Locality(BaseStep):
    _column_name = "locality"

    def compute(self) -> pandas.DataFrame:
        def format_locality(row):
            text = ''
            obec = row['Lokalita - název']
            popis = row['Charakteristika místa sběru']

            if pandas.isna(obec) or obec == '':
                obec = ''
            else:
                text += f"{obec} - "

            if not pandas.isna(popis) and popis != '':
                text += str(popis)

            return text.strip()

        result = self._data.apply(format_locality, axis=1)
        return pandas.DataFrame({self._column_name: result})
