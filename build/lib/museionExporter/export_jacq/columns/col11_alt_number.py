from .base import BaseStep
import pandas
class Column11_alt_number(BaseStep):

    _column_name="alt_number"

    def compute(self) -> pandas.DataFrame:
        self._sbirky['JinaC_S'] = self._sbirky['JinaC_S'].fillna('s.n.')

        result = self._sbirky['JinaC_S'].map(self.extract_non_numeric_or_sn)
        return pandas.DataFrame({self._column_name: result})

    def extract_non_numeric_or_sn(self, value) -> str:
        value_str = str(value).strip()
        if value_str == '':
            return 's.n.'
        elif value_str.isdigit():
            return ''
        else:
            return value_str