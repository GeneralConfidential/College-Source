import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

dataset = pd.read_csv('datasets/salary_data.csv') 
dataset.dropna(inplace=True)
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 1].values 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0) 

regressor = LinearRegression() 
regressor.fit(X_train, y_train) 

y_pred = regressor.predict(X_test) 

#Training
plt.scatter(X_train, y_train, color='red') 
plt.plot(X_train, regressor.predict(X_train), color='blue') 
plt.title('Salary VS Experience (Training set)') 
plt.xlabel('Year of Experience') 
plt.ylabel('Salary') 
plt.savefig("salaryTraining.png")

#Testing
plt.scatter(X_test, y_test, color='red') 
plt.plot(X_train, regressor.predict(X_train), color='blue') 
plt.title('Salary VS Experience (Test set)') 
plt.xlabel('Year of Experience') 
plt.ylabel('Salary') 
plt.savefig("salaryTest.png")