import streamlit as st
import pickle
import numpy as np

# ------------------------------
# Page Setup
# ------------------------------
st.set_page_config(page_title="Book Economic Strategy", page_icon="📚", layout="centered")

st.title("📚 Book Economic Success Predictor")

st.markdown("Predict whether a book is economically successful based on review patterns.")

st.divider()

# ------------------------------
# Load Model
# ------------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ------------------------------
# Initialize Session State
# ------------------------------
if "rating" not in st.session_state:
    st.session_state.rating = 4.2
    st.session_state.review_count = 5
    st.session_state.helpfulness = 0.6
    st.session_state.review_length = 800

# ------------------------------
# Sample Inputs (Top Section)
# ------------------------------
st.subheader("🧪 Try Sample Scenarios")

col1, col2, col3 = st.columns(3)

if col1.button("High Success"):
    st.session_state.rating = 4.8
    st.session_state.review_count = 60
    st.session_state.helpfulness = 0.85
    st.session_state.review_length = 1000

if col2.button("Risk Case"):
    st.session_state.rating = 2.8
    st.session_state.review_count = 20
    st.session_state.helpfulness = 0.4
    st.session_state.review_length = 500

if col3.button("Premium Niche"):
    st.session_state.rating = 4.3
    st.session_state.review_count = 3
    st.session_state.helpfulness = 0.6
    st.session_state.review_length = 700

st.divider()

# ------------------------------
# Prediction Result (Middle)
# ------------------------------
log_review_count = np.log1p(st.session_state.review_count)
log_review_length = np.log1p(st.session_state.review_length)
interaction = st.session_state.rating * log_review_count

features = np.array([[ 
    st.session_state.rating,
    log_review_count,
    st.session_state.helpfulness,
    log_review_length,
    interaction
]])

scaled = scaler.transform(features)
prediction = model.predict(scaled)
probability = model.predict_proba(scaled)[0][1]

st.subheader("📊 Prediction Result")

if prediction[0] == 1:
    st.success(f"High Economic Success Probability: {probability:.2f}")
else:
    st.error(f"Low Economic Success Probability: {probability:.2f}")

# Simple interpretation
if st.session_state.rating >= 4.5 and st.session_state.review_count > 20:
    segment = "Mass Market Leader"
elif st.session_state.rating < 3:
    segment = "Risk Segment"
elif st.session_state.review_count < 5:
    segment = "Premium / Niche"
else:
    segment = "Trusted Quality"

st.info(f"Segment Classification: {segment}")

st.divider()

# ------------------------------
# Adjustable Inputs (Bottom)
# ------------------------------
st.subheader("✏️ Adjust Book Metrics")

st.session_state.rating = st.slider(
    "Average Rating", 1.0, 5.0, st.session_state.rating
)

st.session_state.review_count = st.number_input(
    "Review Count", min_value=0, value=st.session_state.review_count
)

st.session_state.helpfulness = st.slider(
    "Helpfulness Ratio", 0.0, 1.0, st.session_state.helpfulness
)

st.session_state.review_length = st.number_input(
    "Average Review Length (characters)", min_value=0, value=st.session_state.review_length
)