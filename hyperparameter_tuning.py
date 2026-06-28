from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


class HyperparameterTuner:

    def tune_model(
        self,
        X,
        y
    ):

        parameters = {

            "n_estimators":
            [100, 200, 250],

            "max_depth":
            [5, 10, 15]

        }

        grid = GridSearchCV(

            RandomForestClassifier(),

            parameters

        )

        grid.fit(X, y)

        return grid.best_params_