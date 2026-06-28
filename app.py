from fastapi import FastAPI
import joblib


app = FastAPI()

model = joblib.load(
    "fraud_detection_model.pkl"
)


@app.post("/predict")

def predict(transaction: dict):

    prediction = model.predict([[
        transaction["amount"],
        transaction["hour"]
    ]])

    return {

        "fraud_prediction":
        int(prediction[0])

    }