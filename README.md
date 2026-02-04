# JCDSJKTAM-33_Beta
# TECO Customer Churn Analysis and Predictor

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://tecochurn.streamlit.app)
![Task](https://img.shields.io/badge/Task-Churn_Prediction-34495E?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Library-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Model](https://img.shields.io/badge/Model-AdaBoost-A569BD?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-2ECC71?style=flat-square)
## Business Understanding

### Context

Customer churn has a direct impact on revenue and long-term sustainability. Retaining existing customers is generally more cost-effective than acquiring new ones, making churn prediction a critical use case for data-driven decision making. 

### Problem Statement

Teco, a Telecommunication company,  needs a way to identify customers who are likely to churn, using available demographic, service usage, and account information.

### Goal

- Build a classification model to predict customer churn

- Evaluate model performance using metrics aligned with business costs

- Support decision-making for customer retention strategies

## Analytical Approach

1. Data Understanding and Exploration

  * Review dataset structure and features
  * Analyze churn distribution
  *  Explore relationships between categorical and numerical variables

2.  Data Preparation
  * Handle missing values
  * Encode categorical features
  * Scale numerical features where needed

3.  Modeling
  * Train multiple classification models
  * Compare model performance using classification metrics

4. Evaluation
  * Use precision, recall, F-score variants, and confusion matrix
  * Incorporate cost and benefit considerations in model selection

## Evaluation Metrics

The project emphasizes metrics that reflect business impact, not just overall accuracy:

* Precision
* Recall
* F2-Score (to prioritize catching churners)
* Confusion Matrix
* Cost–Benefit Analysis

## Tools and Libraries

  * Python
  * Pandas
  * NumPy
  * Matplotlib / Seaborn
  * Scikit-learn
  * Jupyter Notebook

## How to Run
  * Clone the repository
  * Install required Python libraries
  * Open the notebook in Jupyter or JupyterLab
  * Run the notebook cells sequentially

## Key Takeaways
* Certain customer characteristics and service types show strong association with churn. Customers with monthly subscription shows a tendency in churn.
* Model evaluation should prioritize recall-oriented metrics when the cost of missing churners is high
* Cost-based evaluation helps align technical results with business objectives

# Notes

This project is intended for analytical and educational purposes. The modeling approach and assumptions should be adjusted when applied to real-world production systems.
