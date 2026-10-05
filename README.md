# 📊 Predictive Analytics Using Historical Data

## 📌 Project Overview

**Predictive Analytics Using Historical Data** is a machine learning project designed to analyze historical retail sales data and predict future sales trends.

The project uses historical sales records to identify patterns, trends, and relationships within the data. Machine learning models are then trained using time-based and historical sales features to estimate future sales.

The project includes data preprocessing, exploratory data analysis, feature engineering, machine learning model training, model evaluation, and future sales forecasting.

The main goal of this project is to demonstrate how historical business data can be transformed into useful predictions that can support better business decisions.

---

## 🛠️ Technologies Used

The project was built using the following technologies and Python libraries:

* **Python** – Main programming language
* **Pandas** – Data cleaning, manipulation, and analysis
* **NumPy** – Numerical calculations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Scikit-learn** – Machine learning models and evaluation
* **Joblib** – Saving and loading the trained machine learning model
* **Jupyter Notebook** – Data analysis, experimentation, and model development
* **Streamlit** – Creating the interactive prediction dashboard
* **VS Code** – Project development and management

### Machine Learning Models

Two machine learning algorithms were used:

1. **Linear Regression**
2. **Random Forest Regressor**

The models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

The better-performing model was selected for future sales prediction.

---

## 🎯 Use of the Project

This project can be used to analyze historical sales data and generate predictions about future sales.

The dashboard can help users:

* Analyze historical sales trends
* Understand product performance
* Compare sales across different products
* Analyze category-level sales
* Monitor daily and monthly sales
* Identify important factors affecting sales
* Compare machine learning model performance
* Predict future sales
* Estimate expected sales for the next 30 days
* Support sales and inventory planning

The project demonstrates how historical data can be converted into actionable business insights using machine learning.

---

## 📊 Dashboard

The Streamlit dashboard provides an interactive interface for exploring the sales data and predictions.

It includes:

* Total Sales
* Total Units Sold
* Average Daily Sales
* Historical Sales Trend
* Monthly Sales Analysis
* Product Performance
* Category Performance
* 30-Day Future Sales Forecast
* Forecasted Sales Visualization
* Dataset Preview
* Product Selection

The dashboard makes the analytical results easier to understand without requiring users to work directly with the Jupyter Notebook.

---

## ⭐ Advantages of This Dashboard

### 1. Better Decision Making

The dashboard converts historical sales data into meaningful information that can help businesses make more informed decisions.

### 2. Future Sales Planning

The 30-day sales forecast provides an estimate of future sales, which can be useful for planning upcoming business activities.

### 3. Inventory Management

Sales predictions can help businesses estimate future demand and maintain appropriate inventory levels.

### 4. Easy Data Visualization

Charts and graphs make it easier to understand sales patterns, trends, and product performance.

### 5. Product Performance Analysis

Users can compare different products and identify products that generate higher sales.

### 6. Interactive Dashboard

The Streamlit interface allows users to select products and explore the data interactively.

### 7. Machine Learning Based Prediction

Instead of relying only on historical reports, the project uses machine learning models to generate predictions based on historical patterns.

### 8. Reusable Project Structure

The project can be extended with new datasets, additional machine learning models, new features, and more advanced forecasting techniques.

---

## 🔄 Project Workflow

```text
Historical Sales Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Machine Learning Models
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Future Sales Forecast
        ↓
Streamlit Dashboard
```

---

## 📁 Project Structure

```text
Predictive-Analytics-Using-Historical-Data/
│
├── data/
│   ├── retail_sales_historical.csv
│   └── future_sales_forecast.csv
│
├── notebooks/
│   └── predictive_analytics.ipynb
│
├── models/
│   └── predictive_model.pkl
│
├── app/
│   └── app.py
│
├── visualizations/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project in VS Code

Open the project folder in **Visual Studio Code**.

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 6. Run the Jupyter Notebook

Open:

```text
notebooks/predictive_analytics.ipynb
```

Run all cells to perform data analysis, train the models, evaluate them, and generate the future forecast.

### 7. Run the Streamlit Dashboard

From the project root directory:

```bash
streamlit run app/app.py
```

The dashboard will open in your web browser.

---

## 📈 Final Conclusion

The **Predictive Analytics Using Historical Data** project demonstrates how machine learning can be applied to historical retail sales data to discover patterns and predict future sales.

By combining **data analysis, visualization, feature engineering, machine learning, and an interactive Streamlit dashboard**, the project provides a complete workflow from raw historical data to useful business predictions.

The project shows how predictive analytics can support **sales forecasting, inventory planning, product analysis, and data-driven decision making**.

Overall, this project provides a practical example of how historical business data can be transformed into valuable insights and future predictions using Python and machine learning.
