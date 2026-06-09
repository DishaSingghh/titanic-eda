# Titanic EDA — Data Science Foundations

Exploratory data analysis on the Titanic dataset (Kaggle) to build and apply core data science fundamentals: NumPy, Pandas, Matplotlib, and Seaborn.

This is Week 1–2 of a self-directed ML roadmap I'm working through before starting core ML (logistic regression, decision trees, ensembles) in Week 3.
## What this covers

| Topic | Files | Concepts practiced |
|---|---|---|
| NumPy | `numpy/` | ndarray, indexing, slicing, broadcasting, axis ops, normalization |
| Pandas | `pandas/titanic_eda.py` | Series/DataFrame, groupby, null handling, filtering, feature engineering |
| Matplotlib | `matplotlib/` | bar, histogram, scatter, subplots, log scale |
| Seaborn | `seaborn/` | histplot+KDE, boxplot, countplot, heatmap |

Dataset: `train.csv` from [Kaggle Titanic competition](https://www.kaggle.com/c/titanic). Not included in this repo — download and place in the relevant folder before running.

---

## Key findings

The analysis focused on what factors predicted survival among the 891 passengers.

**Overall survival rate: 38.4%**

**Gender was the strongest predictor.**
Female passengers survived at 74.2% vs 18.9% for male passengers — a gap of over 55 percentage points. This reflects the "women and children first" evacuation protocol.

**Passenger class was the second strongest predictor.**

| Class | Survival rate |
| 1st   | 63.0%         |
| 2nd   | 47.3%         |
| 3rd   | 24.2%         |

First-class passengers were 2.6× more likely to survive than third-class passengers. Likely a combination of cabin location (closer to deck) and preferential lifeboat access.

**Age varied by class.**
Average age in 1st class (36.8) was notably higher than 3rd class (25.9), suggesting wealthier, older passengers booked higher classes.

**Fare varied significantly by embarkation port.**
Passengers boarding at Cherbourg (C) paid an average fare of £59.95 vs £13.28 at Queenstown (Q) — likely because Cherbourg had more first-class passengers.


## Data cleaning decisions

Three columns had missing values:
- **Age** (177 missing): filled with median (28.0) rather than mean — Age has right skew from a few elderly passengers, so median is a more robust central estimate.
- **Embarked** (2 missing): filled with mode ('S') — only 2 rows, negligible impact.
- **Cabin** (687 missing, 77% of data): dropped entirely — too sparse to impute meaningfully.


## Feature engineering (for ML prep)

Built a clean feature matrix `X` (891 × 7) and target vector `y` ready for Week 3 logistic regression:

- `FamilySize` = SibSp + Parch + 1
- `IsAlone` = 1 if FamilySize == 1, else 0
- `Title` extracted from Name using regex (Mr, Mrs, Miss, Master, Rare)
- `Sex` encoded: female=0, male=1
- `Embarked` encoded: S=0, C=1, Q=2
- `AgeBin` = Age bucketed into 5 categories using `pd.cut()`

---

## How to run

git clone https://github.com/YOUR_USERNAME/titanic-eda
cd titanic-eda
pip install numpy pandas matplotlib seaborn

# Download train.csv from Kaggle and place it in the repo root
# Then run any file:
python pandas/titanic_eda.py

