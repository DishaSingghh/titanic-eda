import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

np.random.seed(42)

num_samples = 500

year_of_experience = np.random.randint(2, 21, num_samples)

slope = (60000 - 20000) / 18
intercept = 20000 - slope * 2

salary = slope * year_of_experience + intercept + np.random.normal(0, 10000, num_samples)

data = pd.DataFrame({
    'YearExperience': year_of_experience,
    'Salary': salary
})

print(data.describe())

plt.figure(figsize=(10, 6))
sns.scatterplot(x='YearExperience', y='Salary', data=data)
plt.title('Salary vs Year of Experience')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.show()

from sklearn.model_selection import train_test_split

x = data[['YearExperience']]
y = data['Salary']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

lr = LinearRegression()

lr.fit(x_train, y_train)

print(lr.score(x_test, y_test))
print(lr.score(x_train, y_train))

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred = lr.predict(x_test)

print(mean_absolute_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

coefficient = lr.coef_[0]
intercept = lr.intercept_

print(coefficient)
print(intercept)

x = np.linspace(2, 20, 100)
y = coefficient * x + intercept

plt.figure(figsize=(10, 6))
plt.scatter(data['YearExperience'], data['Salary'], alpha=0.6, label='Actual Data')
plt.plot(x, y, color='red', label=f'y={coefficient:.2f}x+{intercept:.2f}')
plt.title('Linear Regression: Salary vs Year of Experience')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()