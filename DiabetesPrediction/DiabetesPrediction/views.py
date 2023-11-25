from django.shortcuts import render
import time

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
random_seed = 42



def my_view(request):
    timestamp = int(time.time())
    return render(request, 'my_template.html', {'timestamp': timestamp})

def home(request):
    return render(request,'medico.html')

def medico(request):
    return render(request, 'medico.html')

def diabetes(request):
    return render(request,'diabetes.html')

def result(request):
    data = pd.read_csv(r"D:\Vit\Semester 3\EDAI3\Dataset of Diabetes.csv")

    data.drop_duplicates(['Gender','AGE','Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL','VLDL', 'BMI', 'CLASS'], keep='first', inplace=True)
    data.drop(['ID', 'No_Pation'], axis=1, inplace=True)
    
    X = data.drop("CLASS", axis = 1)
    Y = data["CLASS"]

    X_train, X_test, Y_train, Y_test =  train_test_split(X, Y, test_size= 0.2,shuffle=True )
    model =  LogisticRegression(solver='newton-cg' , class_weight='balanced')
    model.fit(X_train, Y_train)

    gender = float(request.GET['field1'])
    age= float(request.GET['field2'])
    urea= float(request.GET['field3'])
    cr= float(request.GET['field4'])
    hba1c= float(request.GET['field5'])
    bmi= float(request.GET['field6'])
    cholestrol= float(request.GET['field7'])
    tg= float(request.GET['field8'])
    hdl= float(request.GET['field9'])
    ldl= float(request.GET['field10'])
    vldl= float(request.GET['field11'])

    pred = model.predict([[gender, age, urea, cr, hba1c , bmi, cholestrol, tg, hdl, ldl, vldl ]])

    result1 = ""
    if pred==[1]:
        result1 = "Positive"
    else:
        result1 = "Negative"

    return render(request, 'diabetes.html', {"result2" : result1})

