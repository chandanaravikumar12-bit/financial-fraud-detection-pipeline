from sklearn.utils import resample


class DataBalancer:

    def balance_data(
        self,
        dataframe
    ):

        fraud = dataframe[
            dataframe["fraud"] == 1
        ]

        normal = dataframe[
            dataframe["fraud"] == 0
        ]

        fraud_upsampled = resample(
            fraud,
            replace=True,
            n_samples=len(normal)
        )

        balanced = normal.append(
            fraud_upsampled
        )

        return balanced