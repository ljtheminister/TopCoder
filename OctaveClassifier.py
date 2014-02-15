import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.lda import LDA


def read_csv(datafile):
    return pd.read_csv(datafile)

def PCA(X, n_components):
    X_pca = PCA(n_components=n_components)
    X_pca.fit(X)
    return X_pca

def LDA_classifier(X,y):
    
	

data = pd.read_csv('TrainingData.csv', header=None)
X = data.ix[:,:5]
y = data.ix[:,5]

