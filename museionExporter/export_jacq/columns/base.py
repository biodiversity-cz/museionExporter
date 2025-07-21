import pandas

class BaseStep:
    _data: pandas.DataFrame
    _column_name: str

    def proceed(self, data: pandas.DataFrame) -> pandas.DataFrame:
        self._data = data
        return self.compute()

    def compute(self) -> pandas.DataFrame:
        result = self._data.apply(
            lambda row: f"".strip(),
            axis=1
        )

        return pandas.DataFrame({self._column_name: result})