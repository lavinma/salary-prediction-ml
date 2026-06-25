Salary Prediction Using Machine Learning

Project Overview

In this project, I built a machine learning pipeline to predict salaries from LinkedIn job postings using structured job market data.

The objective of this project is to explore how job characteristics—such as title, location, work type, experience level, company, and other posting attributes—can be used to estimate annual salary. Throughout the project, I focus on building a complete machine learning workflow, including data cleaning, exploratory data analysis, feature engineering, model development, and evaluation.

This project builds upon my previous Career Market Analytics project by moving from descriptive analytics to predictive modeling.

⸻

Dataset

The dataset contains over 120,000 LinkedIn job postings collected from Kaggle, including information such as:

* Job title
* Company
* Location
* Experience level
* Work type
* Salary information
* Job descriptions
* Skills
* Posting metadata

Since salary information is only available for a subset of postings, I first cleaned and filtered the data to create a modeling-ready dataset for supervised machine learning.

⸻

Project Goals

Throughout this project, I aim to:

* Build a clean machine learning dataset from raw LinkedIn job postings
* Explore relationships between job characteristics and salary
* Engineer meaningful predictive features
* Train and evaluate multiple regression models
* Compare model performance using standard regression metrics

⸻

Repository Structure

salary-prediction-ml/
│
├── data/
├── notebooks/
├── src/
├── visuals/
├── README.md
└── requirements.txt

Notebooks

* 01 – Data Cleaning and Preparation
* 02 – Exploratory Data Analysis
* 03 – Feature Engineering
* 04 – Salary Prediction Models
* 05 – Model Evaluation and Conclusions

⸻

Technologies

* Python
* pandas
* NumPy
* scikit-learn
* Matplotlib
* Jupyter Notebook

⸻

Current Status

🚧 This project is currently in progress.

Completed:

* Project setup
* Data acquisition
* Data cleaning
* Initial preprocessing

Next steps:

* Exploratory data analysis
* Feature engineering
* Model training
* Model evaluation
* Performance comparison

⸻

Future Improvements

Future versions of this project may include:

* Natural language processing using job descriptions
* TF-IDF feature extraction
* Gradient Boosting and XGBoost models
* Hyperparameter tuning
* Model deployment with a web application