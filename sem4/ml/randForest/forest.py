import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
import graphviz

train = pd.read_csv('./madfhantr.csv')

train.dropna(inplace=True)

train = train[['Gender','Married','Education','Self_Employed','Credit_History','Loan_Status']]

train['Gender']=train['Gender'].replace(to_replace='Male',value='1')
train['Gender']=train['Gender'].replace(to_replace='Female',value='0')

train['Married']=train['Married'].replace(to_replace='Yes',value='1')
train['Married']=train['Married'].replace(to_replace='No',value='0')

train['Self_Employed']=train['Self_Employed'].replace(to_replace='No',value='0')
train['Self_Employed']=train['Self_Employed'].replace(to_replace='Yes',value='1')

train['Education']=train['Education'].replace(to_replace='Graduate',value='1')
train['Education']=train['Education'].replace(to_replace='Not Graduate',value='0')

X = train.drop(columns=['Loan_Status'])
y = train.Loan_Status

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

classifier = RandomForestClassifier(n_estimators= 10, criterion="entropy")  
print(classifier.fit(X_train,y_train))  

print(classifier.score(X_test,y_test))
