import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Book Economic Strategy",
    page_icon="📚",
    layout="wide"
)

# ------------------------------
# Custom Styling
# ------------------------------
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
}
.subtle {
    color: #6c757d;
    font-size:18px;
}
.metric-card {
    background-color:#f8f9fa;
    padding:20px;
    border-radius:12px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Load Model
# ------------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ------------------------------
# Header
# ------------------------------
st.markdown('<div class="big-title">📚 Book Economic Strategy Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtle">AI-driven market segmentation & economic success prediction</div>', unsafe_allow_html=True)
st.divider()

# ------------------------------
# Tabs
# ------------------------------
tabs = st.tabs(["📊 Overview", "🔮 Predict", "📈 Model Insights"])

# =====================================================
# 📊 OVERVIEW TAB
# =====================================================
with tabs[0]:

    st.subheader("📊 Dataset Snapshot")

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown('<div class="metric-card"><h3>4.26</h3><p>Average Rating</p></div>', unsafe_allow_html=True)
    col2.markdown('<div class="metric-card"><h3>2</h3><p>Median Review Count</p></div>', unsafe_allow_html=True)
    col3.markdown('<div class="metric-card"><h3>0.57</h3><p>Avg Helpfulness</p></div>', unsafe_allow_html=True)
    col4.markdown('<div class="metric-card"><h3>830</h3><p>Avg Review Length</p></div>', unsafe_allow_html=True)

    st.divider()

    st.subheader("📌 Economic Segments Identified")

    st.markdown("""
    🟢 **Trusted Quality**  
    High ratings + high helpfulness → Strong brand trust  

    🔴 **Risk Segment**  
    Low ratings despite demand → Quality concerns  

    💎 **Premium Niche**  
    High price + low demand → Specialized market  

    🔵 **Mass Market Leader**  
    High demand + strong ratings → Revenue driver  
    """)

# =====================================================
# 🔮 PREDICTION TAB
# =====================================================
with tabs[1]:

    st.subheader("Enter Book Metrics")

    colA, colB = st.columns(2)

    with colA:
        rating = st.slider("⭐ Average Rating", 1.0, 5.0, 4.2)
        helpfulness = st.slider("👍 Helpfulness Ratio", 0.0, 1.0, 0.6)

    with colB:
        review_count = st.number_input("📝 Review Count", min_value=0, value=5)
        review_length = st.number_input("📄 Avg Review Length (characters)", min_value=0, value=800)

    st.divider()

    st.subheader("🧪 Quick Examples")

    ex1, ex2, ex3 = st.columns(3)

    if ex1.button("📈 High Success"):
        rating = 4.8
        review_count = 60
        helpfulness = 0.85
        review_length = 1000

    if ex2.button("⚠️ Risk Case"):
        rating = 2.8
        review_count = 20
        helpfulness = 0.4
        review_length = 500

    if ex3.button("💎 Premium Niche"):
        rating = 4.3
        review_count = 3
        helpfulness = 0.6
        review_length = 700

    st.divider()

    if st.button("🚀 Predict Economic Success"):

        log_review_count = np.log1p(review_count)
        log_review_length = np.log1p(review_length)
        interaction = rating * log_review_count

        features = np.array([[rating, log_review_count, helpfulness, log_review_length, interaction]])
        scaled = scaler.transform(features)

        prediction = model.predict(scaled)
        probability = model.predict_proba(scaled)[0][1]

        st.subheader("Prediction Result")

        # Probability Visualization
        fig, ax = plt.subplots(figsize=(6,3))
        ax.barh(["Success Probability"], [probability])
        ax.set_xlim(0,1)
        ax.set_xlabel("Probability")
        st.pyplot(fig)

        if prediction[0] == 1:
            st.success(f"✅ High Economic Success Probability: {probability:.2f}")
        else:
            st.error(f"❌ Low Economic Success Probability: {probability:.2f}")

        # Segment Logic
        if rating >= 4.5 and review_count > 20:
            st.info("Segment Classification: 🔵 Mass Market Leader")
        elif rating < 3:
            st.info("Segment Classification: 🔴 Risk Segment")
        elif review_count < 5:
            st.info("Segment Classification: 💎 Premium / Niche")
        else:
            st.info("Segment Classification: 🟢 Trusted Quality")

# =====================================================
# 📈 MODEL INSIGHTS TAB
# =====================================================
with tabs[2]:

    st.subheader("Model Performance")

    st.markdown("""
    **Accuracy:** 93.8%  
    **Precision:** 96.4%  
    **Recall:** 90.3%  
    **F1 Score:** 93.28%  
    **ROC-AUC:** 0.985  
    """)

    st.divider()

    st.subheader("Key Economic Insight")

    st.markdown("""
    Economic success is primarily driven by:

    - ⭐ Rating (Quality Signal)
    - 📝 Review Volume (Demand Signal)
    - 📈 Rating × Demand Interaction

    This reflects core demand-supply dynamics:
    Products with both high quality and high demand dominate the marketplace.
    """)