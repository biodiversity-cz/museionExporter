from .base import BaseStep
import pandas
class Column2_HerbNummer(BaseStep):

    _column_name="HerbNummer"

    def _convert_row(self, row) -> str:
        por_c = str(row.get('PorC_S', ''))
        lomeni = row.get('Lomeni_S', '')
        if lomeni != '_':
            if len(por_c) < 5:
                por_c = por_c.zfill(5)
            if len(lomeni) < 2:
                lomeni = lomeni.zfill(2)
            result = f"{por_c}/{lomeni}"
        else:
            if len(por_c) < 7:
                por_c = por_c.zfill(7)
            result = por_c

        return result


    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._convert_row(row),
            axis=1
        )
        return pandas.DataFrame({self._column_name: result})
