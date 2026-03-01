# 📚 Book Economic Strategy Using Review Patterns

## 🔍 Business Problem

How can sellers identify economically successful books using review patterns?

This project applies machine learning techniques to:
- Segment books into economic categories
- Predict economic success
- Support pricing and demand strategy

---

## 📊 Dataset

Amazon Books Reviews Dataset  
https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews

---

## 🧠 Economic Concepts Applied

- Demand-Supply Theory
- Market Segmentation
- Pricing Strategy
- Revenue Optimization
- Risk Identification

---

## 🤖 AI Techniques Used

- Data Cleaning & Feature Engineering
- K-Means Clustering
- Logistic Regression Classification
- Feature Interaction Modeling

---

## 📈 Model Performance

Final Logistic Regression Accuracy: **94%**

### Confusion Matrix

|                      | Predicted Not Successful | Predicted Successful |
|----------------------|--------------------------|----------------------|
| **Actual Not Successful** | 3230                     | 101                  |
| **Actual Successful**     | 292                      | 2728                 |

### Interpretation

- **True Negatives (3230):** Correctly identified unsuccessful books  
- **True Positives (2728):** Correctly identified successful books  
- **False Positives (101):** Predicted success but actually unsuccessful  
- **False Negatives (292):** Missed successful books  

The strong diagonal dominance indicates high predictive reliability.

---

## 🚀 Deployment

Interactive Streamlit application:
- Input book metrics
- Predict economic success
- View probability score