# 🧾 Vendor Invoice Intelligence System

<div align="center">

### AI-Powered Freight Cost Prediction & Invoice Risk Flagging

An end-to-end machine learning application that analyzes vendor invoice data to **predict freight costs** and **identify invoices requiring manual review**.

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square\&logo=pandas\&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=flat-square\&logo=scikit-learn\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=flat-square\&logo=streamlit\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square\&logo=sqlite\&logoColor=white)

</div>

---

## 📌 Overview

Vendor invoice processing can involve checking invoice amounts, quantities, freight charges, purchasing information, and delivery timelines.

This project develops an **end-to-end ML pipeline** to automate two parts of this process:

| 🚚 Freight Cost Prediction                                               | 🚨 Invoice Risk Flagging                                   |
| :----------------------------------------------------------------------- | :--------------------------------------------------------- |
| Predicts expected freight cost using invoice quantity and invoice value. | Identifies invoices that should be sent for manual review. |
| **Input:** Quantity + Dollars                                            | **Input:** Invoice & purchase-level features               |
| **Output:** Predicted Freight Cost                                       | **Output:** Manual Approval / Auto-Approval                |

Both models are integrated into an interactive **Streamlit Vendor Invoice Intelligence Portal**.

---

# ✨ Highlights

* 🚚 **Freight cost prediction**
* 🚨 **Invoice risk classification**
* 🗄️ SQLite database integration
* 🧹 Data preprocessing and feature engineering
* 🤖 Comparison of multiple ML algorithms
* 🔍 Random Forest hyperparameter tuning using `GridSearchCV`
* 📊 Regression and classification evaluation
* 💾 Model serialization with Joblib
* 🖥️ Interactive Streamlit interface
* 🔌 Separate training and inference pipelines

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │    SQLite Database   │
                         │     inventory.db     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Data Extraction &    │
                         │ Feature Engineering  │
                         └──────────┬───────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
          ┌────────────────────┐        ┌────────────────────┐
          │ Freight Prediction │        │ Invoice Risk       │
          │     Pipeline       │        │    Pipeline        │
          └─────────┬──────────┘        └─────────┬──────────┘
                    │                             │
                    ▼                             ▼
          ┌────────────────────┐        ┌────────────────────┐
          │ Model Comparison   │        │ Random Forest +   │
          │                    │        │   GridSearchCV     │
          └─────────┬──────────┘        └─────────┬──────────┘
                    │                             │
                    ▼                             ▼
          ┌────────────────────┐        ┌────────────────────┐
          │ Best Regression    │        │ Tuned Classifier   │
          │      Model         │        │                    │
          └─────────┬──────────┘        └─────────┬──────────┘
                    │                             │
                    └──────────────┬──────────────┘
                                   ▼
                         ┌──────────────────────┐
                         │   Saved ML Models   │
                         │      (.pkl)          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Streamlit Portal   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Real-Time Results  │
                         └──────────────────────┘
```

---

# 🚚 Module 1 — Freight Cost Prediction

## Objective

Predict the freight cost associated with a vendor invoice using:

```text
Quantity
Dollars
```

Target:

```text
Freight
```

The data is loaded from the `vendor_invoice` table in the SQLite database.

### Models Evaluated

Three regression algorithms were compared:

* Linear Regression
* Decision Tree Regression
* Random Forest Regression

Evaluation metrics:

* MAE
* RMSE
* R²

The training pipeline automatically selects the model with the **lowest MAE**.

### 📊 Results

| Model                    |     MAE ↓ |       RMSE ↓ |       R² ↑ |
| :----------------------- | --------: | -----------: | ---------: |
| 🥇 **Linear Regression** | **24.46** | **15482.52** | **97.00%** |
| Decision Tree Regression |     33.87 |     33306.53 |     93.55% |
| Random Forest Regression |     27.65 |     19215.83 |     96.28% |

### 🏆 Selected Model

**Linear Regression**

```text
MAE  : 24.46
RMSE : 15482.52
R²   : 97.00%
```

The selected model is saved as:

```text
models/predict_freight_model.pkl
```

---

# 🚨 Module 2 — Invoice Risk Flagging

## Objective

Determine whether a vendor invoice should be:

```text
🟢 SAFE FOR AUTO-APPROVAL
```

or

```text
🔴 MANUAL APPROVAL
```

### Features

The deployed classifier uses:

```text
invoice_quantity
invoice_dollars
Freight
total_item_quantity
total_item_dollars
```

### 🔧 Feature Engineering

The preprocessing pipeline aggregates purchase-level information by `PONumber` and derives additional information such as:

* Total brands
* Total item quantity
* Total item dollars
* Average receiving delay
* Days from PO to invoice
* Days from invoice to payment

### Risk Label

The current target variable is **rule-generated**.

An invoice is flagged when:

```text
|invoice_dollars - total_item_dollars| > 5
```

**OR**

```text
avg_receiving_delay > 10 days
```

Otherwise, the invoice is classified as normal.

> ⚠️ The classifier therefore learns the defined business rules rather than historical human-verified fraud outcomes.

---

## 🤖 Model Training

A **Random Forest Classifier** was optimized using:

```text
GridSearchCV
5-fold Cross Validation
F1 Score
```

The hyperparameter search covered:

```text
n_estimators
max_depth
min_samples_split
min_samples_leaf
criterion
```

### 📊 Classification Performance

| Metric        |      Score |
| :------------ | ---------: |
| **Accuracy**  | **88.82%** |
| **Precision** | **89.66%** |
| **Recall**    | **88.82%** |
| **F1 Score**  | **88.34%** |

The trained classifier is saved as:

```text
models/predict_flag_invoice.pkl
```

---

# 🖥️ Streamlit Application

The trained models are exposed through a single interactive application.

### 🚚 Freight Prediction

The user provides:

```text
Quantity
Invoice Dollars
```

The application returns:

```text
Estimated Freight Cost
```

### 🚨 Invoice Risk Prediction

The user provides:

```text
Invoice Quantity
Invoice Dollars
Freight Cost
Total Item Quantity
Total Item Dollars
```

The application returns:

```text
🔴 Invoice requires MANUAL APPROVAL
```

or

```text
🟢 Invoice is SAFE for Auto-Approval
```

---

# 📸 Application Preview

> Add your Streamlit screenshots here.

```text
docs/
├── dashboard.png
├── freight_prediction.png
└── invoice_flagging.png
```

After adding the images to your repository, replace this section with:

```markdown
### Dashboard

![Dashboard](docs/dashboard.png)

### Freight Cost Prediction

![Freight Prediction](docs/freight_prediction.png)

### Invoice Risk Flagging

![Invoice Flagging](docs/invoice_flagging.png)
```

---

# 🧰 Tech Stack

### Data

`Python` · `Pandas` · `NumPy` · `SQLite`

### Machine Learning

`Scikit-learn` · `Linear Regression` · `Decision Tree` · `Random Forest` · `GridSearchCV`

### Visualization

`Matplotlib` · `Seaborn` · `Plotly`

### Application

`Streamlit`

### Model Persistence

`Joblib`

---

# 📁 Project Structure

```text
Vendor-Invoice-Intelligence/
│
├── 📂 data/
│   └── inventory.db
│
├── 📂 models/
│   ├── predict_freight_model.pkl
│   ├── predict_flag_invoice.pkl
│   └── scaler.pkl
│
├── 📂 inferencing/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── 📓 Predicting Freight Cost.ipynb
├── 📓 Invoice flagging.ipynb
│
├── 🐍 app.py
│
├── 🐍 data_preprocessing.py
├── 🐍 model_evaluation.py
├── 🐍 train.py
│
├── 🐍 data_preprocessing(1).py
├── 🐍 model_evaluation(1).py
├── 🐍 train(1).py
│
└── 📄 README.md
```

---

# 🔄 ML Workflow

## Freight Prediction

```text
SQLite Database
      ↓
Load Vendor Invoice Data
      ↓
Select Quantity + Dollars
      ↓
Train/Test Split
      ↓
Linear Regression
Decision Tree
Random Forest
      ↓
Model Evaluation
      ↓
Select Lowest MAE
      ↓
Save Best Model
```

## Invoice Risk Classification

```text
SQLite Database
      ↓
Join Invoice + Purchase Data
      ↓
Feature Engineering
      ↓
Generate Risk Labels
      ↓
Train/Test Split
      ↓
StandardScaler
      ↓
Random Forest
      ↓
GridSearchCV
      ↓
Evaluate Best Estimator
      ↓
Save Classifier
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Vendor-Invoice-Intelligence
```

### 2. Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn plotly streamlit joblib
```

### 3. Add the database

Place the SQLite database here:

```text
data/inventory.db
```

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🧪 Train the Models

### Freight Prediction Model

```bash
python train.py
```

This will:

1. Load invoice data
2. Prepare features
3. Split the dataset
4. Train three regression models
5. Evaluate the models
6. Select the lowest-MAE model
7. Save the model to `models/`

### Invoice Risk Model

```bash
python "train(1).py"
```

This will:

1. Load invoice and purchase data
2. Generate invoice-risk labels
3. Prepare the five classifier features
4. Scale the features
5. Tune the Random Forest classifier
6. Evaluate the best estimator
7. Save the trained classifier

---

# 📌 Key Project Takeaways

### 01 — End-to-End ML

The project covers the complete workflow:

**Data → Preprocessing → Feature Engineering → Training → Evaluation → Model Saving → Inference → Application**

### 02 — Model Selection

Instead of assuming a single algorithm would work best, multiple models were evaluated and compared using appropriate performance metrics.

### 03 — Hyperparameter Optimization

The invoice classifier uses `GridSearchCV` with 5-fold cross-validation to optimize the Random Forest model.

### 04 — Business-Oriented ML

The project focuses on practical operational problems:

* Freight cost forecasting
* Invoice exception detection
* Manual review prioritization

---

# ⚠️ Limitations

The invoice-risk model currently uses **rule-generated labels**.

This means the model is learning patterns corresponding to the project's predefined risk criteria rather than learning from a dataset containing verified historical fraud or manual-review outcomes.

A production system should ideally use historical:

* Approved invoices
* Rejected invoices
* Manually reviewed invoices
* Confirmed anomalies/fraud cases

as ground-truth labels.

---

# 🚀 Future Improvements

* [ ] Replace rule-generated labels with historical review outcomes
* [ ] Add vendor-level historical behavior
* [ ] Add price deviation features
* [ ] Add anomaly detection
* [ ] Add prediction probabilities
* [ ] Add model monitoring
* [ ] Automate model retraining
* [ ] Deploy the application
* [ ] Add authentication and role-based access
* [ ] Add automated reporting

---

# 👨‍💻 Author

<div align="center">

### Dhruv

**B.Tech Chemical Engineering — NIT Jalandhar**

Machine Learning · Data Analytics · Python · Supply Chain Analytics

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving the repository a star!

</div>
