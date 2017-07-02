# -*- coding: utf-8 -*-
'''
by HanLiu
input: mannually split data: data_train.csv and data_test.csv

'''
import sys
import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')


#training data 80%
df = pd.read_csv('data_train.csv')
#print(df.shape)
#df.replace('?', np.nan, inplace=True)  # data cleaning
#df.dropna(inplace=True)
#print(df.shape)
df.drop(['id'], 1, inplace=True)
X_train = np.array(df.drop(['class'], 1))
Y_train= np.array(df['class'])


#test data 20%
df2 = pd.read_csv('data_test.csv')
#print(df2.shape)
df2.drop(['id'], 1, inplace=True)
X_test = np.array(df2.drop(['class'], 1))
Y_test= np.array(df2['class'])


#manually split already done
#X_trian, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)

accuracy = clf.score(X_test, Y_test)
print(accuracy)




