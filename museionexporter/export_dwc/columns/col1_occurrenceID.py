from .base import BaseStep
import pandas


class OccurenceId(BaseStep):
    _column_name = "occurrenceID"

    def compute(self) -> pandas.DataFrame:
        def format_id(row):
            specimen_id = row['Inventární číslo']
            herbarium = row['Herbář']
            
            if pandas.isna(specimen_id) or specimen_id == '':
                specimen_id = ''
            if pandas.isna(herbarium) or herbarium == '':
                herbarium = ''
            
            text = f"{herbarium} {specimen_id}"
            return text.strip()

        result = self._data.apply(format_id, axis=1)
        return pandas.DataFrame({self._column_name: result})
