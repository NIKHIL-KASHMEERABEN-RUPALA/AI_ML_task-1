import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("=== Step 1: Loading and Exploring Dataset ===\n")
df = pd.read_csv('train.csv')
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\nData Types and Null Counts:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nStatistical Summary (Numerical Features):")
print(df.describe())

print("\n=== Step 2: Handling Missing Values ===\n")
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['HasCabin'] = df['Cabin'].apply(lambda x: 0 if pd.isna(x) else 1)
df.drop('Cabin
