import pandas as pd


class DataCleaner:

    def clean_dataset(self, dataframe):

        dataframe.drop_duplicates(
            inplace=True
        )

        dataframe.fillna(
            0,
            inplace=True
        )

        return dataframe