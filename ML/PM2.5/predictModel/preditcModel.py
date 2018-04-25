import csv
import numpy as np
import pandas as pd

'''Load train data'''
filename = "train.csv"
data = pd.read_csv(filename)    #DataFrame type
del data['Datetime']
del data['Testmaterial']
#print(data)

'''Sort train data'''
ItemNum = 18
x_train = []        # train data's features set
y_train = []        # train data's target set
for i in range(int(len(data)/ItemNum)):
    day = data[i*ItemNum:(i+1)*ItemNum]     # train data in one day
    for j in range(15):
        x = day.iloc[:, j:j+9]
        y = int(day.iloc[9, j+9])
        x_train.append(x)
        y_train.append(y)
        print(x)
        print(y)