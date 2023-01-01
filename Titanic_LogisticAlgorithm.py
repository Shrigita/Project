import math
import numpy as np 
import pandas as pd 
import seaborn as sns 
from seaborn import countplot
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def TitanicLogistic():
    #Step 1: Load Data
    titanic_data =pd.read_csv("TitanicDataset.csv")

    print("First 5 Entries From loaded dataset")
    print(titanic_data.head())

    print("Number of Passenger are "+str(len(titanic_data)))

    #Step 2 :Anlyse the Data
    print("Visualisation : Supervised and Non Supervised Passenger ")
    figure()
    target ="Survived"

    countplot(data=titanic_data,x =target).set_title("Supervised and Non Supervised Passengers")
    show()

    print("Visualisation : Supervised and Non Supervised Passenger based on Gender ")
    figure()
    target ="Survived"

    countplot(data=titanic_data,x =target,hue="Sex").set_title("Supervised and Non Supervised Passengers based on Gender")
    show()

    print("Visualisation : Supervised and Non Supervised Passenger based on the Passenger Class ")
    figure()
    target ="Survived"

    countplot(data=titanic_data,x =target,hue="Pclass").set_title("Supervised and Non Supervised Passengers based on Passenger class")
    show()

    print("Visualisation : Supervised and Non Supervised Passenger based on Age ")
    figure()
    target ="Survived"

    titanic_data["Age"].plot.hist().set_title("Supervised and Non Supervised Passengers based on Age")
    show()

    print("Visualisation : Supervised and Non Supervised Passenger based on Fare ")
    figure()
    target ="Survived"

    titanic_data["Fare"].plot.hist().set_title("Supervised and Non Supervised Passengers based on Fare")
    show()

    #step 3:Data Cleaning
    titanic_data.drop("zero",axis =1, inplace =True)

    print("First 5 Entries From loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Values of Sex Column ")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex Column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"],drop_first = True)
    print(Sex.head(5))

    print("Values of Pclass Column after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"],drop_first = True)
    print(Pclass.head(5))

    print("Values of data set after concatenation new colummn")
    titanic_data =pd.concat([titanic_data,Sex,Pclass],axis = 1)
    print(titanic_data.head(5))

    print("Values of Data set after Removing irrelevent Colummn")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis = 1,inplace =True)
    print(titanic_data.head(5))


    X = titanic_data.drop("Survived",axis = 1)
    Y = titanic_data["Survived"]

    #Step 4 :Data Traning
    xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.5)

    logmodel = LogisticRegression()

    logmodel.fit(xtrain,ytrain)

    #Data Testing
    prediction = logmodel.predict(xtest)

    #Step 5 : Calculate Accuracy

    print("Classification Report of Logistic Regression is :")
    print(classification_report(ytest,prediction))

    print("Confusion Matrix of Logistic Regression is :")
    print(confusion_matrix(ytest,prediction))

    print("Accuraccy of Logistic Regression is :")
    print(accuracy_score(ytest,prediction))



def main():
    print("Supervised Machine Learning")
    
    print("Logistic Regression on Titanic DataSet ")

    TitanicLogistic()

if __name__ =="__main__":
    main()