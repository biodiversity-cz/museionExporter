from .base import BaseStep
import pandas


class Column17_taxon_alt(BaseStep):
    _column_name = "taxon_alt"

    def compute(self) -> pandas.DataFrame:
        result = self._sbirky.apply(
            lambda row: self._build_revisions(row.get('IdC_S', ''),row.get('Sberatel_S', ''), row.get('DatSberu_S', '')),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

    def _build_revisions(self, sbirky_id: int, sberatel_S: str, datum_S: str) -> str:
        zaznamy = self._urceni[self._urceni['IdC_UR'] == sbirky_id]
        if zaznamy.empty:
            return ''

        zaznamy['__sort_key__'] = zaznamy['DatUrc_UR'].apply(self._sort_key)
        zaznamy = zaznamy.sort_values(by='__sort_key__').drop(columns=['__sort_key__'])

        polozky = []
        first_row = zaznamy.iloc[0]
        first_nomen = str(first_row.get('Nomen_UR', '')).strip()
        first_urcil = str(first_row.get('Urcil_UR', '')).strip()
        first_date = str(first_row.get('DatUrc_UR', '')).strip()

        first_text = f"orig."
        if sberatel_S != first_urcil:
            first_text += f" {self._build_adresarNameFirts(first_urcil)} {first_date}: {first_nomen}"
        elif '<neurčený>' in first_nomen:
            first_text += f": -"
        else:
            first_text += f": {first_nomen}"
        polozky.append(first_text)

        for _, row in zaznamy.iloc[1:].iterrows():
            daturc = str(row.get('DatUrc_UR', '')).strip()
            rok = daturc[:4] if daturc else ''
            text = f"{self._build_adresarNameFirts(str(row['Urcil_UR']).strip())}"
            if rok:
                text += f" ({rok})"
            text += f": {str(row['Nomen_UR']).strip()}"
            polozky.append(text)

        return "; ".join(polozky)

    def _sort_key(self, value: str):
        if value.lower() == 's.d.':
            return (0, '')  # s.d. jde úplně dopředu
        return (1, value)  # ostatní podle původní hodnoty
