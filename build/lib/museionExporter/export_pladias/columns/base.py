import pandas
import re

class BaseStep:
    _sbirky: pandas.DataFrame
    _lokality: pandas.DataFrame
    _adresar: pandas.DataFrame
    _urceni: pandas.DataFrame
    _column_name: str

    def proceed(self, Sbirky: pandas.DataFrame, Lokality: pandas.DataFrame, Adresar: pandas.DataFrame, Urceni: pandas.DataFrame) -> pandas.DataFrame:
        self._sbirky = Sbirky
        self._lokality = Lokality
        self._adresar = Adresar
        self._urceni = Urceni
        return self.compute()

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: f"".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_adresar(self, adresar_str: str) -> str:
        if not pandas.notna(adresar_str) or adresar_str == '':
            return ''

        autori = self._adresar[self._adresar['ZkrJm_A'] == adresar_str]
        if autori.empty:
            return ''
        prijmeni = str(autori.iloc[0].get('Prijmeni_A', '')).strip()
        jmeno = str(autori.iloc[0].get('Jmeno_A', '')).strip()

        if jmeno:
            adresar_str = f"{prijmeni} {jmeno}"
        else:
            adresar_str = prijmeni

        adresar_str = adresar_str.replace(';', '')
        adresar_str = adresar_str.replace(' et al.', ' €')
        adresar_str = adresar_str.replace(' et ', ' & ')
        adresar_str = adresar_str.replace(' €', ' & et al.')

        people = [s.strip() for s in re.split(r',\s*|\s+a\s+|\s+\+\s+|\s+&\s+', adresar_str) if s.strip()]

        if len(people) > 2:
            return ', '.join(people[:-1]) + ' & ' + people[-1]
        elif len(people) == 2:
            return ' & '.join(people)

        return people[0]

    def _build_adresarNameFirts(self, adresar_str: str) -> str:
        if not pandas.notna(adresar_str) or adresar_str == '':
            return ''

        autori = self._adresar[self._adresar['ZkrJm_A'] == adresar_str]
        if autori.empty:
            return ''
        prijmeni = str(autori.iloc[0].get('Prijmeni_A', '')).strip()
        jmeno = str(autori.iloc[0].get('Jmeno_A', '')).strip()

        if jmeno:
            adresar_str = f"{jmeno[0]}. {prijmeni}"
        else:
            adresar_str = prijmeni

        adresar_str = adresar_str.replace(';', '')
        adresar_str = adresar_str.replace(' et al.', ' €')
        adresar_str = adresar_str.replace(' et ', ' & ')
        adresar_str = adresar_str.replace(' €', ' & et al.')

        people = [s.strip() for s in re.split(r',\s*|\s+a\s+|\s+\+\s+|\s+&\s+', adresar_str) if s.strip()]

        if len(people) > 2:
            return ', '.join(people[:-1]) + ' & ' + people[-1]
        elif len(people) == 2:
            return ' & '.join(people)

        return people[0]