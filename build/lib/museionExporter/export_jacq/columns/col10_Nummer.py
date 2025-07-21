from .base import BaseStep
import pandas
class Column10_Nummer(BaseStep):

    _column_name="Nummer"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['JinaC_S'] = self._sbirky['JinaC_S'].fillna('')

        result = self._sbirky['JinaC_S'].map(self.extract_numeric_string)
        return pandas.DataFrame({self._column_name: result})

    def extract_numeric_string(self, value) -> str:
        value_str = str(value).strip()
        return value_str if value_str.isdigit() else ''

