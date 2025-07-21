from .base import BaseStep
import pandas


class Column1(BaseStep):
    _column_name = "Standardní jméno"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_item(row),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_item(self, row) -> str:
        nomen = str(row.get('Nomen_S', '')).strip()
        var = str(row.get('Var_S', '')).strip()
        return f"{nomen} {var if var != '' else ''}".strip()

