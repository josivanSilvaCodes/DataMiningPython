import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data as pdr
from datetime import datetime, timedelta
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlsxwriter

# tive que instalar
#pip install xlrd
 
df = pd.read_excel('(20, 0).xlsx')

print(" ")
print("Base: (20, 0).xlsx")
print("Colunas/objetos:")
#print(df.columns)

# COLUNAS:
#ID  |	NOME  |	CPF  |	CLASSE_CARGO  |	JORNADA | SALARIO

# VALOR MÍNIMO DE HONORÁRIOS ===================================
idmin = np.where(df['SALARIO']==df['SALARIO'].min())[0]
print(" ")
print("Valor mínimo de Honorários: ")
print(df['SALARIO'][idmin])
print(" ")

# VALOR MÉDIO DE HONORÁRIOS =========================================================
soma = 0
for i in df.index:
    soma = soma + df['SALARIO'][i]

media = (soma/len(df['SALARIO']))
print("Média: ")
print(round(media, 2))
print(" ")
idmedia= np.where(df['SALARIO']==df['SALARIO'].mean())[0]
# ===================================================================================
# VALOR MÁXIMO DE SALARIO ========================================================
idmax = np.where(df['SALARIO']==df['SALARIO'].max())[0]
print("Valor máximo de SALARIO: ")
print(df['SALARIO'][idmax])
print(" ")
# Cálculo daAmplitude dos dados: ====================================================
amplitude = (df['SALARIO'][idmax[0]] - df['SALARIO'][idmin[0]])
print("Amplitude: ")
print(amplitude)
print(" ")
# Intervalo Interquartil = amplitude entre o primeiro e o terceiro quartil ==========
dadosValores = []
for k in df.index:
    dadosValores.append(df['SALARIO'][k])
dadosValores.sort()
qtd = int(len(dadosValores)/4)
iq = (dadosValores[(3*qtd)-1] - dadosValores[qtd-1])
print("Interquartil: ")
print(round(iq, 2))
print(" ")

#=====================================================================================

##print("-------- Todos os campos com valores mínimos de honorários --------------------------------")
##
##i = idmin
##for j in i:
##    print(df['ANO'][i][j],"| ", df['MES'][i][j],"| ", df['ID_SERVIDOR_PORTAL'][i][j],"| ",
##          df['CPF'][i][j],"| ", df['NOME'][i][j],"| ", df['VALOR'][i][j])
##    
###======================================================================================
##print(" ")
##print("-------- Todos os campos com valores máximos de honorários --------------------------------")
##
##i = idmax
##for j in i:
##    print(df['ANO'][i][j],"| ", df['MES'][i][j],"| ", df['ID_SERVIDOR_PORTAL'][i][j],"| ",
##          df['CPF'][i][j],"| ", df['NOME'][i][j],"| ", df['VALOR'][i][j])

print ("qtde:", len(dadosValores))
    

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from random import *
style.use("ggplot")

from sklearn.cluster import KMeans

#X = np.array([ [1,2],[5,8],[1.5,1.8],[1,0.6],[9,11], [19,21], [29,11]  ])
X = []

for n in range(0,len(dadosValores)):
    #X.insert(n,[  dadosValores[n], randint(1, 320)  ])
    X.insert(n,[  df['SALARIO'][n], df['JORNADA'][n]  ])


##p1 =  X[idmin[0]]
##p2 =  [randint(1, 320), media]
##p3 =  X[idmax[0]]

p1 =  X[(qtd)-1]
p2 =  X[(2*qtd)-1]
p3 =  X[(3*qtd)-1]

Y = np.array([
               p1,
               p2,
               p3               
             ])

kmeans = KMeans(n_clusters=3, init = Y, max_iter=15)
kmeans.fit(X)

centroid = kmeans.cluster_centers_
labels = kmeans.labels_

print (centroid)
print(labels)

colors = ["g.","r.","c."]

for i in range(0, len(X), 5):
   #print ("coordinate:" , X[i], "label:", labels[i])
   plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
##plt.scatter(X[:,0], X[:,1], c=labels.astype(np.float), edgecolor="k")

plt.scatter(centroid[:,0],centroid[:,1], marker = "x", s=150, linewidths = 5, zorder =10)

plt.show()

