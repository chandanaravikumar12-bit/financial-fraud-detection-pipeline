import pandas as pd


class FeatureEngineer:

    def create_features(
        self,
        dataframe
    ):

        dataframe["transaction_ratio"] = (
            dataframe["amount"] /
            (dataframe["amount"].mean() + 1)
        )

        dataframe["hour_flag"] = (
            dataframe["hour"] > 22
        ).astype(int)

        return dataframe