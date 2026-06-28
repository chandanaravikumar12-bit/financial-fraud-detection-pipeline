import joblib

from sklearn.ensemble import RandomForestClassifier


class FraudTrainer:

    def train_model(
        self,
        X_train,
        y_train
    ):

        model = RandomForestClassifier(
            n_estimators=250,
            max_depth=10
        )

        model.fit(
            X_train,
            y_train
        )

        joblib.dump(
            model,
            "fraud_detection_model.pkl"
        )

        return model