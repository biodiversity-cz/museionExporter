from .base import BaseStep
import pandas


class BasisOfRecord(BaseStep):
    _column_name = "basisOfRecord"

    def compute(self) -> pandas.DataFrame:
        result = self._data.apply(
            lambda row: 'PreservedSpecimen',
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})

