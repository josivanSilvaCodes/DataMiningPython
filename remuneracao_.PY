import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader.data as pdr
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlsxwriter

print("-----------------------------------------------")
import csv
texto = ''
x, y = 0, 0
workbook = xlsxwriter.Workbook('2018_remuneracao_5.xlsx')
worksheet = workbook.add_worksheet()

with open('20180131_Remuneracao.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    while (i<(408428)):
        row1 = next(reader)  # gets the first line
        print("...")
        texto = str(row1)
        texto = texto[2:(len(texto)-2)]
        texto = str(texto).split("\\t")
        for x in range(0, len(texto)):
            worksheet.write(y, x, texto[x])
        y = y + 1
        i = i + 1        
print("------------------------------------------------")
workbook.close()


# tive que instalar
# pip install xlrd
# pip install xlsxwriter

# o valor do salário mínimo: R$ 954,00 ===========================
# idabaixomin = np.where(df['VALOR']<=954)[0]
# print(df['VALOR'][idabaixomin])















    
