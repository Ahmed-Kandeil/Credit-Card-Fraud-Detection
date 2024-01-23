import json
import streamlit as st

from models.predict import predict


st.set_page_config(page_title="FraudGuard", page_icon="💰")
st.title("Credit Card Fraud Detection")

sample_container, predict_container = st.columns(2)

with sample_container:
    sample_type = st.selectbox(
        "Sample Type",
        options=["Default", "Fraud", "Not Fraud"],
    )

with predict_container:
    predict_type = st.selectbox(
        "Predict Type",
        options=["Machine Learning", "Deep Learning"],
    )

with open(f"data/{sample_type}.json", "r") as json_file:
    features_metadata = json.load(json_file)

    if sample_type == "Random":
        pass

    items_list = list(features_metadata.items())
    mid_index = len(items_list) // 2

    features_one = dict(items_list[:mid_index])
    features_two = dict(items_list[mid_index:])

features = []
features_one_container, features_two_container = st.columns(2)

with features_one_container:
    for feature, data in features_one.items():
        feature_min, feature_max, feature_value = data.values()

        feature_slider = st.slider(
            feature,
            min_value=feature_min,
            max_value=feature_max,
            value=feature_value,
            key=feature,
        )

        features.append(feature_slider)

with features_two_container:
    for feature, data in features_two.items():
        feature_min, feature_max, feature_value = data.values()

        feature_slider = st.slider(
            feature,
            min_value=feature_min,
            max_value=feature_max,
            value=feature_value,
            key=feature,
        )

        features.append(feature_slider)

amount = st.number_input("Amount", min_value=0, max_value=12_000)
submit_btn = st.button("Submit")


if submit_btn:
    predictions = predict(features + [amount], predict_type)

    if predictions == "Fraud":
        st.warning("Warning: The transaction is flagged as potentially fraudulent.")
    else:
        st.balloons()
        st.success("Success: The transaction is identified as not fraudulent.")
