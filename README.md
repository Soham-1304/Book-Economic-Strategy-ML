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

## 📈 Model Performance

Final Logistic Regression Accuracy: **93.8%**

### Performance Metrics

- **Precision:** 96.4%
- **Recall:** 90.3%
- **F1 Score:** 93.28%
- **ROC-AUC:** 0.985

### Confusion Matrix

|                      | Predicted Not Successful | Predicted Successful |
|----------------------|--------------------------|----------------------|
| **Actual Not Successful** | 3230                     | 101                  |
| **Actual Successful**     | 292                      | 2728                 |

### Interpretation

- The model demonstrates strong class separation (ROC-AUC ≈ 0.99).
- High precision indicates low risk of misclassifying weak books as successful.
- High recall ensures most successful books are correctly identified.
- The strong diagonal dominance in the confusion matrix confirms reliable predictive performance.

---

## 🚀 Deployment

Interactive Streamlit application:
- Input book metrics
- Predict economic success
- View probability score