import os
import joblib


def test_model_file_exists():
    assert os.path.exists("models/churn_model.pkl")


def test_model_can_be_loaded():
    model = joblib.load("models/churn_model.pkl")
    assert model is not None