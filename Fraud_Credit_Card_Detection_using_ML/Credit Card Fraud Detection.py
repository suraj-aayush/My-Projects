# -*- coding: utf-8 -*-
"""credit_card.ipynb

Importing the requirements
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading the dataset to a Panda Dataframe
credit_card_data = pd.read_csv('/content/creditcard.csv')
credit_card_data.head() #gives the first 5 rows of data

credit_card_data.tail() #gives the last 5 rows of data

#getting some dataset information
credit_card_data.info()

#checking the number of missing values in each column
credit_card_data.isnull().sum()
# 0 --> represent real and legit transactions
# 1 --> represent fake and fraud transactions

#distribution of legit transcaction & fraud transaction
credit_card_data['Class'].value_counts()

# separating the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class ==1]

# here if class value is 0 then entire row is stored in legit variable 
# here if class value is 1 then entire row is stored in fraud variable

print(legit.shape)
print(fraud.shape)

#statistical measure of our data
legit.Amount.describe()

fraud.Amount.describe()

# comparing the values for both transaction
credit_card_data.groupby('Class').mean()

"""Here the difference is very important for our model

Here we will build a sample dataset from the main dataset containing similar distribution of legit and fraud transactions

UNDER SAMPLING

building a sample dataset containing similar distribution of normal distributions
"""

legit_sample = legit.sample(n=492)

new_dataset = pd.concat ([ legit_sample, fraud ],axis=0)
#here we concatinate legit_sample and fraud for further evaluation
#and when axis is 0 , dataframe is added one by one
#it means that fruad values are added below legit sample...
#axis 0 is row wise
#axis 1 is column wise

new_dataset.head()

new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

#since  we have the approx same mean it tells that the nature of the dataset is not changed
#it is same as the original dataset

"""splitting the data into features and targets"""

X=new_dataset.drop(columns='Class',axis=1) #axis 1 is column
Y=new_dataset['Class']

print(X)
print(Y)

#splitting the data into Training Data & Testing Data
X_train, X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=0)
#random state describe how our data will split

#test size if amount of testing data

print(X.shape, X_train.shape, X_test.shape)

"""MODEL TRAINING

LOGISTIC REGRESSION

"""

model = LogisticRegression()

#training the logistic regression model with training data

model.fit(X_train,Y_train)

Y_predict = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_predict)

print("acuuracy of the model is -> ",accuracy)

