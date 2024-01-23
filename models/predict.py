import joblib
import streamlit as st

ml_pipeline = joblib.load("models/ml_pipeline.joblib")
dl_pipeline = joblib.load("models/dl_pipeline.joblib")


def predict(features, predict_type: str):
    if predict_type == "Machine Learning":
        prediction = ml_pipeline.predict([features])
    elif predict_type == "Deep Learning":
        prediction = dl_pipeline.predict([features])

    return "Fraud" if int(prediction) == 0 else "Not Fraud"


def main() -> None:
    pass


if __name__ == "__main__":
    main()
