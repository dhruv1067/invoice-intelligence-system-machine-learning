🧾 Vendor Invoice Intelligence System

<div align="center">

AI-Powered Freight Cost Prediction & Invoice Risk Flagging

An end-to-end machine learning project that combines vendor invoice analytics, predictive modeling, and an interactive Streamlit application to support freight forecasting and invoice review.

<br>



</div>

🎯 What is this project?

Vendor invoice processing involves checking invoice values, quantities, freight charges, purchase information, and delivery timelines. This project builds an ML-based workflow around two practical use cases:

Module

Purpose

Output

🚚 Freight Cost Prediction

Estimate freight cost from invoice quantity and value

Predicted freight cost

🚨 Invoice Risk Flagging

Identify invoices that may require additional review

Manual Approval / Auto-Approval

Both models are integrated into a single Streamlit-based Vendor Invoice Intelligence Portal.

✨ Key Features

📊 Exploratory data analysis and feature analysis

🗄️ SQLite-based data extraction

🤖 Multiple ML models for model comparison

🔎 Random Forest hyperparameter tuning with GridSearchCV

📈 Regression and classification evaluation

💾 Model persistence using Joblib

⚡ Separate inference modules for production-style prediction

🖥️ Interactive Streamlit dashboard

🔄 End-to-end workflow from database → ML → application

🧠 Machine Learning Pipeline

flowchart LR
    A[(SQLite Database)] --> B[Data Extraction]
    B --> C[Feature Engineering]
    C --> D{ML Pipelines}

    D --> E[Freight Cost Prediction]
    D --> F[Invoice Risk Flagging]

    E --> G[Model Comparison]
    G --> H[Best Regression Model]

    F --> I[Feature Scaling]
    I --> J[Random Forest + GridSearchCV]

    H --> K[Saved Model]
    J --> K2[Saved Model]

    K --> L[Streamlit Portal]
    K2 --> L
    L --> M[Real-Time Predictions]

🚚 1. Freight Cost Prediction

Objective

Predict the freight cost associated with a vendor invoice using:

Quantity

Dollars

The target variable is:

Freight

Model Development

Three regression algorithms are evaluated:

Linear Regression

Decision Tree Regression

Random Forest Regression

The training pipeline evaluates the models using:

MAE

RMSE

R²

The final model is selected using lowest MAE and saved as:

models/predict_freight_model.pkl

📊 Model Comparison

Model

MAE

RMSE

R²

🥇 Linear Regression

24.46

15482.52

97.00%

Decision Tree Regression

33.87

33306.53

93.55%

Random Forest Regression

27.65

19215.83

96.28%

Best model: Linear RegressionR²: 97.00%

🚨 2. Invoice Risk Flagging

Objective

Classify vendor invoices into:

🟢 SAFE FOR AUTO-APPROVAL
🔴 MANUAL APPROVAL

The model uses five features:

invoice_quantity
invoice_dollars
Freight
total_item_quantity
total_item_dollars

🔧 Risk Label Generation

The training data creates the target label using business rules based on invoice/item dollar differences and receiving delays.

An invoice is flagged when:

The difference between invoice_dollars and total_item_dollars is greater than 5, or

avg_receiving_delay is greater than 10 days.

Otherwise, it is classified as normal.

Important: The current target is rule-generated rather than based on historical human approval/fraud labels.

🤖 Model

A Random Forest Classifier is optimized using:

GridSearchCV

5-fold cross-validation

F1 score as the optimization metric

The hyperparameter search includes:

n_estimators
max_depth
min_samples_split
min_samples_leaf
criterion

The trained classifier is saved as:

models/predict_flag_invoice.pkl

🖥️ Streamlit Application

The project provides a single interactive portal with two prediction modes.

🚚 Freight Cost Prediction

Users enter:

Quantity

Invoice Dollars

The application returns:

Estimated Freight Cost

🚨 Invoice Risk Prediction

Users enter:

Invoice Quantity

Invoice Dollars

Freight Cost

Total Item Quantity

Total Item Dollars

The application returns either:

🔴 Invoice requires MANUAL APPROVAL

or

🟢 Invoice is SAFE for Auto-APPROVAL

🗂️ Project Structure

Vendor-Invoice-Intelligence/
│
├── 📁 data/
│   └── inventory.db
│
├── 📁 models/
│   ├── predict_freight_model.pkl
│   ├── predict_flag_invoice.pkl
│   └── scaler.pkl
│
├── 📁 inferencing/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── 📄 app.py
│
├── 📄 data_preprocessing.py
├── 📄 model_evaluation.py
├── 📄 train.py
│
├── 📄 data_preprocessing(1).py
├── 📄 model_evaluation(1).py
├── 📄 train(1).py
│
├── 📓 Predicting Freight Cost.ipynb
├── 📓 Invoice flagging.ipynb
│
└── 📄 README.md

🛠️ Tech Stack

Programming & Data

Python · Pandas · NumPy · SQLite

Machine Learning

Scikit-learn · Linear Regression · Decision Tree · Random Forest · GridSearchCV

Visualization

Matplotlib · Seaborn · Plotly

Application

Streamlit

Model Management

Joblib

⚙️ Getting Started

1️⃣ Clone the repository

git clone <your-repository-url>
cd <repository-name>

2️⃣ Install dependencies

pip install pandas numpy scikit-learn matplotlib seaborn plotly streamlit joblib

3️⃣ Verify the database

Place the SQLite database at:

data/inventory.db

▶️ Running the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

Use the sidebar to switch between:

🚚 Freight Cost Prediction
🚨 Invoice Manual Approval Flag

🏋️ Training the Models

Freight Model

Run:

python train.py

The pipeline:

Load SQLite data
      ↓
Select Quantity + Dollars
      ↓
80/20 Train-Test Split
      ↓
Train 3 Regression Models
      ↓
Evaluate MAE / RMSE / R²
      ↓
Select Lowest-MAE Model
      ↓
Save predict_freight_model.pkl

Invoice Risk Model

Run:

python "train(1).py"

The pipeline:

Load invoice + purchase data
          ↓
Create risk labels
          ↓
Select 5 features
          ↓
80/20 Train-Test Split
          ↓
StandardScaler
          ↓
Random Forest + GridSearchCV
          ↓
Evaluate Classifier
          ↓
Save predict_flag_invoice.pkl

📈 Evaluation

Freight Prediction

Regression metrics

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

The best-performing regression model achieved:

R² ≈ 97%
MAE = 24.46

Invoice Risk Classification

Classification metrics

Accuracy

Precision

Recall

F1 Score

Classification Report

The optimized Random Forest classifier achieved:

Accuracy ≈ 88.82%
F1 Score ≈ 88.34%

🔌 Inference Architecture

The application does not retrain models during prediction.

Instead, the saved .pkl models are loaded by dedicated inference modules:

User Input
    │
    ▼
Streamlit UI
    │
    ├───────────────┐
    ▼               ▼
Freight Model   Invoice Flag Model
    │               │
    ▼               ▼
Prediction      Risk Flag

This separates the training pipeline from the application/inference layer.

💡 Business Value

The project demonstrates how machine learning can be applied to common invoice-processing workflows:

🚚 Cost Forecasting

Estimate expected freight charges before or during invoice processing.

🚨 Exception Identification

Prioritize invoices that match defined risk conditions for manual review.

⚡ Process Efficiency

Provide immediate predictions through an interactive application rather than requiring manual analysis for every invoice.

📊 Data-Driven Decisions

Use historical invoice and purchasing information to support financial and operational analysis.

⚠️ Limitations

The invoice-risk classifier currently learns from rule-generated labels rather than historical human-reviewed outcomes.

Therefore, it should be interpreted as a demonstration of an ML-based invoice screening workflow rather than a production fraud-detection system.

For a production implementation, the model could be trained using historical:

Approved invoices

Rejected invoices

Manually flagged invoices

Confirmed fraud/anomaly cases

🚀 Future Improvements

Use historical human-reviewed invoice outcomes as training labels

Add vendor-level historical behavior features

Add price and quantity deviation features

Add anomaly detection

Add prediction probabilities/confidence scores

Add model monitoring

Automate periodic model retraining

Deploy the application to a cloud environment

Add authentication and role-based access

👨‍💻 Author

DhruvB.Tech Chemical Engineering — NIT Jalandhar

<div align="center">

⭐ If you found this project interesting, consider giving the repository a star!

Built with Python • Scikit-learn • SQLite • Streamlit

</div>