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
 
df = pd.read_excel('merge.xlsx')

print(" ")
print("Base: merge.xls")
print("Colunas/objetos:")
print(df.columns)

##Base: merge.xls
##Colunas/objetos:
##Index(['ID', 'NOME', 'CPF', 'Unnamed: 3', 'CLASSE_CARGO', 'Unnamed: 5',
##       'Unnamed: 6', 'JORNADA', 'SALARIO'],
##      dtype='object')

print(" ")
print("Valor 1: ")
print(df['CLASSE_CARGO'][1])
print(" ")

# VALOR MÉDIO DE HONORÁRIOS =========================================================

texto = ''
x, y = 0, 0
workbook = xlsxwriter.Workbook('merge_test_.xlsx')
worksheet = workbook.add_worksheet()
#for i in df.index:
##for i in range(0,11):
i = 0
j = 0
while (i<110077):
    if(df['CLASSE_CARGO'][i]!='nan' and df['SALARIO'][i]!='undefined'):
        worksheet.write(j, 0, df['ID'][i])
        worksheet.write(j, 1, df['NOME'][i])
        worksheet.write(j, 2, df['CPF'][i])
        worksheet.write(j, 3, str(df['CLASSE_CARGO'][i]))
        worksheet.write(j, 4, df['JORNADA'][i])
        worksheet.write(j, 5, df['SALARIO'][i])
        #print("i", i, "C: ", str(df['CLASSE_CARGO'][i]))
        print(...)
        j=j+1
    i=i+1


print("------------------------------------------------")
workbook.close()
