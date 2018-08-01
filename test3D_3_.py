import numpy as np
import seaborn as sns
import pandas_datareader.data as pdr
from datetime import datetime, timedelta
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#%matplotlib inline
from sklearn import datasets
import random as rand

# tive que instalar
# pip install xlrd
 
df = pd.read_excel('merge_test_2.xlsx')

# COLUNAS:
#ID  |	NOME  |	CPF  |	CLASSE_CARGO  |	JORNADA | SALARIO


# VALOR MÍNIMO DE SALÁRIOS ========================================================
idmin = np.where(df['SALARIO']==df['SALARIO'].min())[0]


# VALOR MÉDIO DE SALÁRIOS =========================================================
soma = 0
for i in df.index:
    soma = soma + df['SALARIO'][i]

media = (soma/len(df['SALARIO']))

#idmedia= np.where(df['VALOR']==df['VALOR'].mean())[0]

# ===================================================================================
# VALOR MÁXIMO DE SALÁRIOS ==========================================================
idmax = np.where(df['SALARIO']==df['SALARIO'].max())[0]

# Cálculo daAmplitude dos dados: ====================================================
amplitude = (df['SALARIO'][idmax[0]] - df['SALARIO'][idmin[0]])

# Intervalo Interquartil = amplitude entre o primeiro e o terceiro quartil ==========
dadosValores = []
for k in df.index:
    dadosValores.append(df['SALARIO'][k])
dadosValores.sort()
qtd = int(len(dadosValores)/4)
iq = (dadosValores[(3*qtd)-1] - dadosValores[qtd-1])

#=====================================================================================

#Dataset

X = []

for n in range(0,len(dadosValores)):
    X.insert(n,[  df['SALARIO'][n], df['CLASSE_CARGO'][n], df['JORNADA'][n]  ])

X = np.array(X)

p1 =  X[idmin[0]]
p2 =  X[int((idmax[0] - idmin[0])/2)]
p3 =  X[idmax[0]]

Y = np.array([
               p1,
               p2,
               p3               
             ])

#KMeans
km = KMeans(n_clusters=3, init=Y, n_init=1, max_iter=15)
km.fit(X)
#km.predict(X)
labels = km.labels_

centroid = km.cluster_centers_

#Plotting
fig = plt.figure(1, figsize=(7,7))

ax = Axes3D(fig, rect=[0, 0, 1, 1])
ax.scatter(X[:,0], X[:,1], X[:,2], c=labels.astype(np.float), edgecolor="k")

ax.scatter(centroid[:,0], centroid[:,1], centroid[:,2], marker = "x", s=150, linewidths = 5, zorder =10)

# anomalia pintar de vermelho
ax.scatter(X[0][0], X[0][1], X[0][2],   c='r', edgecolor="k", s=200)
ax.scatter(X[50][0], X[50][1], X[50][2], c='r', edgecolor="k", s=200)
ax.scatter(X[100][0], X[100][1], X[100][2], c='r', edgecolor="k", s=200)

ax.set_xlabel("X - Salário Normalizado ")
ax.set_ylabel("Y - Categoria/Cargo")
ax.set_zlabel("Z - Carga Horária")
plt.title("Salário dos servidores da união por K Means", fontsize=14)
plt.show()

#===============================================================================================
