from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


class Evaluator:

    def evaluate(
        self,
        model,
        X_test,
        y_test
    ):

        predictions = model.predict(
            X_test
        )

        print(
            "Accuracy:",
            accuracy_score(
                y_test,
                predictions
            )
        )

        print(
            "Precision:",
            precision_score(
                y_test,
                predictions
            )
        )

        print(
            "Recall:",
            recall_score(
                y_test,
                predictions
            )
        )