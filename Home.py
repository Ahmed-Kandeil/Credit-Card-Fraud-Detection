import streamlit as st


st.set_page_config(page_title="FraudGuard", page_icon="💰")

# App title and introduction
st.title("FraudGuard: Your Intelligent Fraud Detection Solution")
st.image("images/banner.jpg")
st.markdown(
    """
    At FraudGuard, we empower you with cutting-edge technology to safeguard
    financial transactions. Our data-driven approach and advanced
    machine-learning algorithms ensure the highest accuracy in detecting and
    preventing credit card fraud.
    """
)

# Features section
st.header("Why Choose FraudGuard?")
st.markdown(
    """
    - **Precision and Accuracy:** Our state-of-the-art machine learning models
    analyze vast datasets to distinguish between legitimate and fraudulent
    transactions with unparalleled precision.
    - **User-Friendly Interface:** Experience seamless navigation through our
    intuitive and user-friendly interface. No need for extensive technical
    expertise - FraudGuard is designed for users of all levels.
    """
)

# Getting Started section
st.header("Getting Started:")
st.markdown(
    """
    Ready to enhance your fraud detection capabilities? [Try it now](#) and explore
    the future of secure transactions with FraudGuard.
    """
)

# Call to action
st.markdown(
    "Join FraudGuard today and fortify your defenses against credit card fraud!"
)
