# Import library

import pandas as pd

# Load dataset

df = pd.read_csv("train.csv")

# Dataset overview

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset info:")
df.info()

print("\nSummary statistics:")
print(df.describe())

# Missing values

print("\nMissing values:")
print(df.isnull().sum())

# Data cleaning

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop(columns=["Cabin"], inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Question 1: Total passengers

print("\nTotal passengers:")
print(df["PassengerId"].count())

# Question 2: Overall survival rate

print("\nOverall survival rate:")
print(df["Survived"].mean())

# Question 3: Survival rate by gender
print("\nSurvival rate by gender:")
print(df.groupby("Sex")["Survived"].mean())

# Question 4: Survival rate by passenger class

print("\nSurvival rate by passenger class:")
print(df.groupby("Pclass")["Survived"].mean())

# Question 5: Average fare by embarkation port

print("\nAverage fare by embarkation port:")
print(df.groupby("Embarked")["Fare"].mean())

# Question 6: Average age by class

print("\nAverage age by passenger class:")
print(df.groupby("Pclass")["Age"].mean())

# Question 7: Passenger count by class

print("\nPassenger count by class:")
print(df["Pclass"].value_counts())

# Question 8: Male vs female passenger count

print("\nPassenger count by gender:")
print(df["Sex"].value_counts())

# Question 9: Oldest passenger

print("\nOldest passenger:")
print(df.loc[df["Age"].idxmax(), ["Name", "Age"]])

# Question 10: Highest fare paid

print("\nPassenger who paid highest fare:")
print(df.loc[df["Fare"].idxmax(), ["Name", "Fare"]])