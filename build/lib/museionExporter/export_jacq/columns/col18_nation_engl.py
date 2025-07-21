from .base import BaseStep
import pandas
class Column18_nation_engl(BaseStep):

    _column_name="nation_engl"
    _code_map = {
        'RUS': 'RU',
        'AUT': 'AT',
        'CZE': 'CZ',
        'SVK': 'SK',
        'DEU': 'DE',
        'POL': 'PL',
        'HUN': 'HU',
        'ROM': 'RO',
        'FRA': 'FR',
        'ESP': 'ES',
        'GBR': 'UK',
        'GRC': 'GR',
        'GEO': 'GE'
    }
    def compute(self) -> pandas.DataFrame:

        result = self._sbirky.apply(
            lambda row: self._process_nation(row.get('Lokalita_S', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _process_nation(self, lokalita_id: str) -> str:
        if not lokalita_id:
            return ''

        locality = self._lokality[self._lokality['ZkrLok_L'] == lokalita_id]
        if locality.empty:
            return ''
        stat_l = str(locality.iloc[0].get('Stat_L', '')).strip()
        return self._code_map.get(stat_l, stat_l)