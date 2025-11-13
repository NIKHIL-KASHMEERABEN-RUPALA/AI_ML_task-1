# AI_ML_task-1

This task demonstrates a complete data cleaning and preprocessing workflow using the Titanic dataset from Kaggle. The goal is to prepare the raw data for machine learning by handling missing values, encoding categorical variables, scaling numerical features, and removing outliers.



What I Learned  -----


1. Data Exploration
Loaded and examined the dataset structure (shape, info(), describe()).
Identified missing values and data types.
Visualized basic distributions using Matplotlib and Seaborn.

2. Handling Missing Values
Imputed missing Age values with the median (robust to outliers).
Filled missing Embarked values with the mode.
Created a new binary feature HasCabin to indicate whether a cabin was listed, then removed the original Cabin column.

3. Encoding Categorical Variables
Applied Label Encoding to Sex (male=1, female=0).
Used One-Hot Encoding for Embarked to convert categories into numeric format.

4. Feature Scaling
Standardized Age and Fare using StandardScaler from scikit-learn to normalize feature ranges (mean = 0, std = 1).

5. Outlier Detection and Removal
Detected and visualized outliers using boxplots.
Removed extreme outliers in Fare using the Interquartile Range (IQR) method.



Tools & Libraries
Python, Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn (for scaling and encoding)


Key Takeaway
This workflow builds a strong foundation for data preprocessing, a crucial step before applying any machine learning algorithm. Clean and standardized data leads to better model performance and more reliable insights.
