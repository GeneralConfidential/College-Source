import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

dataset = pd.read_csv('datasets/winequality-red.csv',sep=';') 
dataset.dropna(inplace=True)
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 11].values.reshape(-1,1)

for i in range(11):
    X_train, X_test, y_train, y_test = train_test_split(X.iloc[:,i].values, y, test_size=1/3, random_state=0) 

    regressor = LinearRegression() 
    regressor.fit(X_train.reshape(-1,1), y_train) 

    y_pred = regressor.predict(X_test.reshape(-1,1)) 

    #Training
    plt = plt 
    plt.scatter(X_train, y_train, color='red') 
    plt.plot(X_train, regressor.predict(X_train.reshape(-1,1)), color='blue')  
    plt.title('Wine Quality Training Set')
    plt.xlabel('X'+str(i+1)) 
    plt.ylabel('Quality') 
    plt.savefig("wine" + str(i+1) + "Train.png")

    #Testing 
    plt = plt 
    plt.scatter(X_test, y_test, color='red') 
    plt.plot(X_train, regressor.predict(X_train.reshape(-1,1)), color='blue') 
    plt.title('Wine Quality Test Set') 
    plt.xlabel('X'+str(i+1)) 
    plt.ylabel('Quality') 
    plt.savefig("wine" + str(i+1) + "Test.png")