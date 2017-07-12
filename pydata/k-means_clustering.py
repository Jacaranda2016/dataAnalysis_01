# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale


X=pd.read_csv("data_total.csv")#data_total contains all the data both paid and unpaid



kmeans=KMeans(n_clusters=2,random_state=25)
results=kmeans.fit(X)

X["cluster"]=results.predict(X)
X["target"]=np.array(X['class'])
X["c"] = ""

classification_result = X[["cluster","target","c" ]].groupby(["cluster", "target"]).agg("count")

print(classification_result)


