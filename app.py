import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("📚 Book Economic Success Predictor")

st.write("Enter book metrics to predict economic success.")

rating = st.slider("Average Rating", 1.0, 5.0, 4.0)
review_count = st.number_input("Review Count", min_value=0)
helpfulness = st.slider("Helpfulness Ratio", 0.0, 1.0, 0.5)
review_length = st.number_input("Average Review Length", min_value=0)

if st.button("Predict"):

    log_review_count = np.log1p(review_count)
    log_review_length = np.log1p(review_length)
    interaction = rating * log_review_count

    features = np.array([[rating, log_review_count, helpfulness, log_review_length, interaction]])

    scaled = scaler.transform(features)

    prediction = model.predict(scaled)
    probability = model.predict_proba(scaled)[0][1]

    if prediction[0] == 1:
        st.success(f"Economic Success Probability: {probability:.2f}")
    else:
        st.error(f"Low Economic Success Probability: {probability:.2f}")