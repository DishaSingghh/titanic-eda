import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

# Survival distribution
sns.countplot(data=df, x="Survived")
plt.title("Survival Count")
plt.show()

# Passenger class distribution
sns.countplot(data=df, x="Pclass")
plt.title("Passenger Class Distribution")
plt.show()

# Survival by sex
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Sex")
plt.show()

# Age distribution
sns.histplot(data=df, x="Age", kde=True)
plt.title("Age Distribution")
plt.show()

# Fare distribution
sns.histplot(data=df, x="Fare", kde=True)
plt.title("Fare Distribution")
plt.show()

# Age distribution by survival
sns.boxplot(data=df, x="Survived", y="Age")
plt.title("Age vs Survival")
plt.show()

# Fare distribution by survival
sns.boxplot(data=df, x="Survived", y="Fare")
plt.title("Fare vs Survival")
plt.show()

# Fare vs Age
sns.scatterplot(data=df, x="Age", y="Fare")
plt.title("Age vs Fare")
plt.show()

# Survival rate by class
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.show()

# Survival rate by embarkation port
sns.barplot(data=df, x="Embarked", y="Survived")
plt.title("Survival Rate by Embarked")
plt.show()

# Correlation heatmap
corr = df.select_dtypes(include="number").corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Pairplot (can be slow)
sns.pairplot(
    df[["Age", "Fare", "Pclass", "Survived"]].dropna(),
    hue="Survived"
)
plt.show()