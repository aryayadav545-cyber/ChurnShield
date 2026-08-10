import joblib

MODEL_PATH = "models/churn_model.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict_churn(data):
    model = load_model()
    return model.predict(data)