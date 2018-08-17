

```python
import pandas as pd
import matplotlib.pyplot as plt
```


```python
# Abre o arquivo de cadastro
df = pd.read_csv("20170131_Remuneracao.csv", sep=";", encoding='ISO-8859-1')
# Lista as primeiras 50 linhas
df.head(50)
```

    /home/thiago/desenv/venv3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2785: DtypeWarning: Columns (0) have mixed types. Specify dtype option on import or set low_memory=False.
      interactivity=interactivity, compiler=compiler, result=result)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ANO</th>
      <th>MES</th>
      <th>Id_SERVIDOR_PORTAL</th>
      <th>CPF</th>
      <th>NOME</th>
      <th>REMUNERAÇÃO BÁSICA BRUTA (R$)</th>
      <th>REMUNERAÇÃO BÁSICA BRUTA (U$)</th>
      <th>ABATE-TETO (R$)</th>
      <th>ABATE-TETO (U$)</th>
      <th>GRATIFICAÇÃO NATALINA (R$)</th>
      <th>...</th>
      <th>REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (R$)</th>
      <th>REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (U$)</th>
      <th>VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (R$)(*)</th>
      <th>VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (U$)(*)</th>
      <th>VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (R$)(*)</th>
      <th>VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (U$)(*)</th>
      <th>VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (R$)</th>
      <th>VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (U$)</th>
      <th>TOTAL DE VERBAS INDENIZATÓRIAS (R$)(*)</th>
      <th>TOTAL DE VERBAS INDENIZATÓRIAS (U$)(*)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5116961.0</td>
      <td>***.017.623-**</td>
      <td>AARAO CARLOS LUZ MACAMBIRA</td>
      <td>6333,60</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>5157,51</td>
      <td>0,00</td>
      <td>1002,58</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>1002,58</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017</td>
      <td>1.0</td>
      <td>201964.0</td>
      <td>***.056.281-**</td>
      <td>AARAO DIAMANTINO OLIVEIRA</td>
      <td>27491,08</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>159,55</td>
      <td>...</td>
      <td>19246,26</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017</td>
      <td>1.0</td>
      <td>4405000.0</td>
      <td>***.116.132-**</td>
      <td>AARAO FERREIRA LIMA NETO</td>
      <td>12199,49</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>9832,67</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017</td>
      <td>1.0</td>
      <td>4915841.0</td>
      <td>***.031.184-**</td>
      <td>AARAO PEREIRA DE ARAUJO JUNIOR</td>
      <td>19265,92</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>13457,11</td>
      <td>0,00</td>
      <td>901,09</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>901,09</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5105492.0</td>
      <td>***.859.807-**</td>
      <td>AARAO SOARES</td>
      <td>5855,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>6393,67</td>
      <td>0,00</td>
      <td>1032,99</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>1032,99</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017</td>
      <td>1.0</td>
      <td>8114023.0</td>
      <td>***.086.942-**</td>
      <td>AARAO TEIXEIRA DOS SANTOS</td>
      <td>4318,28</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>3153,06</td>
      <td>0,00</td>
      <td>691,45</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>691,45</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2017</td>
      <td>1.0</td>
      <td>2671.0</td>
      <td>***.291.814-**</td>
      <td>AARON DE SOUSA ALVES</td>
      <td>7031,31</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>9047,23</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2017</td>
      <td>1.0</td>
      <td>912539.0</td>
      <td>***.873.832-**</td>
      <td>AARON JONATHAN EDWARDS</td>
      <td>6724,29</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>5427,67</td>
      <td>0,00</td>
      <td>1219,19</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>1219,19</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6806485.0</td>
      <td>***.624.556-**</td>
      <td>AARON JORDAN DA SILVA PENIDO</td>
      <td>3058,70</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>2660,89</td>
      <td>0,00</td>
      <td>1004,95</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>1004,95</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2017</td>
      <td>1.0</td>
      <td>2404623.0</td>
      <td>***.724.317-**</td>
      <td>AARON SILVA DE LIMA</td>
      <td>1250,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>1705,18</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5710805.0</td>
      <td>***.201.086-**</td>
      <td>ABADIA ADENISIA ROCHA E SILVA</td>
      <td>3037,78</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>88,56</td>
      <td>...</td>
      <td>2801,73</td>
      <td>0,00</td>
      <td>495,77</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>495,77</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2017</td>
      <td>1.0</td>
      <td>1713121.0</td>
      <td>***.240.302-**</td>
      <td>ABADIA ALVES DA SILVA</td>
      <td>2916,34</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>2543,69</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5309978.0</td>
      <td>***.834.461-**</td>
      <td>ABADIA CANDIDA LEMES</td>
      <td>5810,91</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4264,77</td>
      <td>0,00</td>
      <td>526,40</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>526,40</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6403578.0</td>
      <td>***.772.411-**</td>
      <td>ABADIA DA GLORIA ARAUJO SPEZIA</td>
      <td>4898,93</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4015,17</td>
      <td>0,00</td>
      <td>32,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>32,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5113978.0</td>
      <td>***.611.031-**</td>
      <td>ABADIA DE FATIMA RESENDE</td>
      <td>4317,87</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>3641,65</td>
      <td>0,00</td>
      <td>591,90</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>591,90</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6118494.0</td>
      <td>***.391.966-**</td>
      <td>ABADIA DE FATIMA ROSA MACEDO</td>
      <td>8006,38</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>6035,48</td>
      <td>0,00</td>
      <td>579,14</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>579,14</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2017</td>
      <td>1.0</td>
      <td>1617447.0</td>
      <td>***.316.491-**</td>
      <td>ABADIA DE MELO COUTINHO</td>
      <td>5029,08</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4535,05</td>
      <td>0,00</td>
      <td>802,31</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>802,31</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2017</td>
      <td>1.0</td>
      <td>7505648.0</td>
      <td>***.922.001-**</td>
      <td>ABADIA DOS REIS NASCIMENTO</td>
      <td>12269,51</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>9237,38</td>
      <td>0,00</td>
      <td>675,94</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>675,94</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5414482.0</td>
      <td>***.945.416-**</td>
      <td>ABADIA GILDA BUSO MATOSO</td>
      <td>4976,23</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4301,26</td>
      <td>0,00</td>
      <td>715,44</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>715,44</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2017</td>
      <td>1.0</td>
      <td>4611397.0</td>
      <td>***.080.181-**</td>
      <td>ABADIA LEDA PRENCE BELLIARD</td>
      <td>6734,23</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>5722,34</td>
      <td>0,00</td>
      <td>845,02</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>845,02</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2017</td>
      <td>1.0</td>
      <td>406342.0</td>
      <td>***.890.176-**</td>
      <td>ABADIA MARIA APARECIDA TEIXEIRA</td>
      <td>5317,20</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>663,32</td>
      <td>0,00</td>
      <td>828,03</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>828,03</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2017</td>
      <td>1.0</td>
      <td>7300875.0</td>
      <td>***.622.206-**</td>
      <td>ABADIA MARIA DE ALMEIDA DANTAS</td>
      <td>4094,22</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4505,64</td>
      <td>0,00</td>
      <td>732,18</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>732,18</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2017</td>
      <td>1.0</td>
      <td>7802383.0</td>
      <td>***.499.931-**</td>
      <td>ABADIA MARIA FREIRE</td>
      <td>6388,25</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>5534,16</td>
      <td>0,00</td>
      <td>780,31</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>780,31</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6908546.0</td>
      <td>***.539.541-**</td>
      <td>ABADIA PEREIRA DA SILVA</td>
      <td>4814,56</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4078,35</td>
      <td>0,00</td>
      <td>908,82</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>908,82</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5210013.0</td>
      <td>***.296.501-**</td>
      <td>ABADIA RODRIGUES DA SILVA</td>
      <td>5615,09</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>2807,54</td>
      <td>...</td>
      <td>9671,67</td>
      <td>0,00</td>
      <td>885,83</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>885,83</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2017</td>
      <td>1.0</td>
      <td>7406431.0</td>
      <td>***.348.951-**</td>
      <td>ABADIA SIQUEIRA GOMES</td>
      <td>3143,27</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>2730,51</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2017</td>
      <td>1.0</td>
      <td>1711106.0</td>
      <td>***.976.801-**</td>
      <td>ABADIA VIEIRA CALACIA</td>
      <td>5526,48</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4453,49</td>
      <td>0,00</td>
      <td>745,34</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>745,34</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2017</td>
      <td>1.0</td>
      <td>1513349.0</td>
      <td>***.327.601-**</td>
      <td>ABADIA VIEIRA DE ABREU</td>
      <td>3143,27</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>2732,23</td>
      <td>0,00</td>
      <td>614,49</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>614,49</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6412792.0</td>
      <td>***.220.502-**</td>
      <td>ABADIAS CARDOSO MORAIS</td>
      <td>9669,52</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>8103,04</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2017</td>
      <td>1.0</td>
      <td>3804316.0</td>
      <td>***.808.901-**</td>
      <td>ABADIAS EDESIO DE PAIVA</td>
      <td>7293,10</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>6209,00</td>
      <td>0,00</td>
      <td>889,46</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>889,46</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2017</td>
      <td>1.0</td>
      <td>4413304.0</td>
      <td>***.257.141-**</td>
      <td>ABADICO JOSE FRANCISCO</td>
      <td>6003,98</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>5274,39</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2017</td>
      <td>1.0</td>
      <td>8414882.0</td>
      <td>***.494.471-**</td>
      <td>ABADIO ALVES LIMA</td>
      <td>5918,17</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4857,58</td>
      <td>0,00</td>
      <td>707,16</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>707,16</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2017</td>
      <td>1.0</td>
      <td>7907862.0</td>
      <td>***.968.426-**</td>
      <td>ABADIO DOS REIS SILVA LEITE</td>
      <td>10122,72</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>7749,78</td>
      <td>0,00</td>
      <td>920,01</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>920,01</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2017</td>
      <td>1.0</td>
      <td>7011242.0</td>
      <td>***.123.811-**</td>
      <td>ABADIO DOS SANTOS</td>
      <td>5214,06</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4787,52</td>
      <td>0,00</td>
      <td>716,23</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>716,23</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6203095.0</td>
      <td>***.924.806-**</td>
      <td>ABADIO FELIX</td>
      <td>6154,15</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>5281,68</td>
      <td>0,00</td>
      <td>610,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>610,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2017</td>
      <td>1.0</td>
      <td>4311612.0</td>
      <td>***.811.056-**</td>
      <td>ABADIO GONCALVES CAETANO</td>
      <td>31612,85</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>22652,35</td>
      <td>0,00</td>
      <td>706,66</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>706,66</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2017</td>
      <td>1.0</td>
      <td>4414745.0</td>
      <td>***.523.496-**</td>
      <td>ABADIO JOSE VITAL</td>
      <td>15121,30</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>7560,65</td>
      <td>...</td>
      <td>23198,97</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2017</td>
      <td>1.0</td>
      <td>906745.0</td>
      <td>***.128.531-**</td>
      <td>ABADIO MENDES FERREIRA</td>
      <td>707,12</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>707,12</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6804597.0</td>
      <td>***.520.391-**</td>
      <td>ABADIO PEREIRA DAS VIRGES</td>
      <td>5593,16</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4589,09</td>
      <td>0,00</td>
      <td>834,72</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>834,72</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2017</td>
      <td>1.0</td>
      <td>1103461.0</td>
      <td>***.563.531-**</td>
      <td>ABADIO SOARES DOS SANTOS</td>
      <td>3136,23</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>2724,71</td>
      <td>0,00</td>
      <td>785,49</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>785,49</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>40</th>
      <td>2017</td>
      <td>1.0</td>
      <td>2006768.0</td>
      <td>***.518.923-**</td>
      <td>ABAETE PINHEIRO DE HOLANDA</td>
      <td>4793,10</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4008,84</td>
      <td>0,00</td>
      <td>1164,61</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>1164,61</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>41</th>
      <td>2017</td>
      <td>1.0</td>
      <td>8008272.0</td>
      <td>***.553.790-**</td>
      <td>ABAITE TOUPA DA SILVA</td>
      <td>8225,99</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>6593,95</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>42</th>
      <td>2017</td>
      <td>1.0</td>
      <td>8608224.0</td>
      <td>***.531.136-**</td>
      <td>ABAPORANG PAES LEME ALBERTO</td>
      <td>4315,96</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>3777,81</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>43</th>
      <td>2017</td>
      <td>1.0</td>
      <td>8707266.0</td>
      <td>***.734.992-**</td>
      <td>ABDA ANTONY RICCIARDI</td>
      <td>4970,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>4696,67</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>44</th>
      <td>2017</td>
      <td>1.0</td>
      <td>1611634.0</td>
      <td>***.301.106-**</td>
      <td>ABDALA UNTAR</td>
      <td>8425,48</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>6919,38</td>
      <td>0,00</td>
      <td>683,89</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>683,89</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2017</td>
      <td>1.0</td>
      <td>9116248.0</td>
      <td>***.672.871-**</td>
      <td>ABDALAH ALI ABDEL CADER</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>10911,56</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>46</th>
      <td>2017</td>
      <td>1.0</td>
      <td>5616967.0</td>
      <td>***.890.691-**</td>
      <td>ABDALLA ANTONIOS KAYED ELIAS</td>
      <td>11709,64</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>8703,81</td>
      <td>0,00</td>
      <td>574,38</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>574,38</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>47</th>
      <td>2017</td>
      <td>1.0</td>
      <td>1704099.0</td>
      <td>***.217.678-**</td>
      <td>ABDALLA DANIEL CURI</td>
      <td>7804,01</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>6396,05</td>
      <td>0,00</td>
      <td>582,33</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>582,33</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2017</td>
      <td>1.0</td>
      <td>8616449.0</td>
      <td>***.735.184-**</td>
      <td>ABDALLAH SALOMAO ARCOVERDE</td>
      <td>11308,31</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>...</td>
      <td>8539,57</td>
      <td>0,00</td>
      <td>801,39</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>801,39</td>
      <td>0,00</td>
    </tr>
    <tr>
      <th>49</th>
      <td>2017</td>
      <td>1.0</td>
      <td>6914642.0</td>
      <td>***.747.011-**</td>
      <td>ABDEILDES NASCIMENTO DOS SANTOS</td>
      <td>12328,66</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>6164,33</td>
      <td>...</td>
      <td>21122,34</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>458,00</td>
      <td>0,00</td>
    </tr>
  </tbody>
</table>
<p>50 rows × 39 columns</p>
</div>




```python
# Exibe todas as colunas
df.columns
```




    Index(['ANO', 'MES', 'Id_SERVIDOR_PORTAL', 'CPF', 'NOME',
           'REMUNERAÇÃO BÁSICA BRUTA (R$)', 'REMUNERAÇÃO BÁSICA BRUTA (U$)',
           'ABATE-TETO (R$)', 'ABATE-TETO (U$)', 'GRATIFICAÇÃO NATALINA (R$)',
           'GRATIFICAÇÃO NATALINA (U$)',
           'ABATE-TETO DA GRATIFICAÇÃO NATALINA (R$)',
           'ABATE-TETO DA GRATIFICAÇÃO NATALINA (U$)', 'FÉRIAS (R$)',
           'FÉRIAS (U$)', 'OUTRAS REMUNERAÇÕES EVENTUAIS (R$)',
           'OUTRAS REMUNERAÇÕES EVENTUAIS (U$)', 'IRRF (R$)', 'IRRF (U$)',
           'PSS/RPGS (R$)', 'PSS/RPGS (U$)', 'DEMAIS DEDUÇÕES (R$)',
           'DEMAIS DEDUÇÕES (U$)', 'PENSÃO MILITAR (R$)', 'PENSÃO MILITAR (U$)',
           'FUNDO DE SAÚDE (R$)', 'FUNDO DE SAÚDE (U$)',
           'TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (R$)',
           'TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (U$)',
           'REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (R$)',
           'REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (U$)',
           'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (R$)(*)',
           'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (U$)(*)',
           'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (R$)(*)',
           'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (U$)(*)',
           'VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (R$)',
           'VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (U$)',
           'TOTAL DE VERBAS INDENIZATÓRIAS (R$)(*)',
           'TOTAL DE VERBAS INDENIZATÓRIAS (U$)(*)'],
          dtype='object')




```python
#contagem, média, desvio padrão (STD), min, quartis e máximo
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MES</th>
      <th>Id_SERVIDOR_PORTAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>567937.0</td>
      <td>5.679370e+05</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.0</td>
      <td>4.765669e+06</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>2.784763e+06</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.0</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.0</td>
      <td>2.400957e+06</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.0</td>
      <td>4.800022e+06</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.0</td>
      <td>7.202422e+06</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.0</td>
      <td>4.790161e+07</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Número total de linhas ou objetos
df.shape
```




    (567938, 39)




```python
# Quantidade de itens faltantes de cada coluna
df.count()
```




    ANO                                                                           567938
    MES                                                                           567937
    Id_SERVIDOR_PORTAL                                                            567937
    CPF                                                                           567937
    NOME                                                                          567937
    REMUNERAÇÃO BÁSICA BRUTA (R$)                                                 567937
    REMUNERAÇÃO BÁSICA BRUTA (U$)                                                 567937
    ABATE-TETO (R$)                                                               567937
    ABATE-TETO (U$)                                                               567937
    GRATIFICAÇÃO NATALINA (R$)                                                    567937
    GRATIFICAÇÃO NATALINA (U$)                                                    567937
    ABATE-TETO DA GRATIFICAÇÃO NATALINA (R$)                                      567937
    ABATE-TETO DA GRATIFICAÇÃO NATALINA (U$)                                      567937
    FÉRIAS (R$)                                                                   567937
    FÉRIAS (U$)                                                                   567937
    OUTRAS REMUNERAÇÕES EVENTUAIS (R$)                                            567937
    OUTRAS REMUNERAÇÕES EVENTUAIS (U$)                                            567937
    IRRF (R$)                                                                     567937
    IRRF (U$)                                                                     567937
    PSS/RPGS (R$)                                                                 567937
    PSS/RPGS (U$)                                                                 567937
    DEMAIS DEDUÇÕES (R$)                                                          567937
    DEMAIS DEDUÇÕES (U$)                                                          567937
    PENSÃO MILITAR (R$)                                                           567937
    PENSÃO MILITAR (U$)                                                           567937
    FUNDO DE SAÚDE (R$)                                                           567937
    FUNDO DE SAÚDE (U$)                                                           567937
    TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (R$)                                        567937
    TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (U$)                                        567937
    REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (R$)                                   567937
    REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (U$)                                   567937
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (R$)(*)      567937
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (U$)(*)      567937
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (R$)(*)    567937
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (U$)(*)    567937
    VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (R$)     567937
    VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (U$)     567937
    TOTAL DE VERBAS INDENIZATÓRIAS (R$)(*)                                        567937
    TOTAL DE VERBAS INDENIZATÓRIAS (U$)(*)                                        567937
    dtype: int64




```python
# Função que mostra a quantidade de itens faltantes por coluna, zero não falta nenhuma informação
df.apply(lambda x: sum(x.isnull()),axis=0)
```




    ANO                                                                           0
    MES                                                                           1
    Id_SERVIDOR_PORTAL                                                            1
    CPF                                                                           1
    NOME                                                                          1
    REMUNERAÇÃO BÁSICA BRUTA (R$)                                                 1
    REMUNERAÇÃO BÁSICA BRUTA (U$)                                                 1
    ABATE-TETO (R$)                                                               1
    ABATE-TETO (U$)                                                               1
    GRATIFICAÇÃO NATALINA (R$)                                                    1
    GRATIFICAÇÃO NATALINA (U$)                                                    1
    ABATE-TETO DA GRATIFICAÇÃO NATALINA (R$)                                      1
    ABATE-TETO DA GRATIFICAÇÃO NATALINA (U$)                                      1
    FÉRIAS (R$)                                                                   1
    FÉRIAS (U$)                                                                   1
    OUTRAS REMUNERAÇÕES EVENTUAIS (R$)                                            1
    OUTRAS REMUNERAÇÕES EVENTUAIS (U$)                                            1
    IRRF (R$)                                                                     1
    IRRF (U$)                                                                     1
    PSS/RPGS (R$)                                                                 1
    PSS/RPGS (U$)                                                                 1
    DEMAIS DEDUÇÕES (R$)                                                          1
    DEMAIS DEDUÇÕES (U$)                                                          1
    PENSÃO MILITAR (R$)                                                           1
    PENSÃO MILITAR (U$)                                                           1
    FUNDO DE SAÚDE (R$)                                                           1
    FUNDO DE SAÚDE (U$)                                                           1
    TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (R$)                                        1
    TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (U$)                                        1
    REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (R$)                                   1
    REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (U$)                                   1
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (R$)(*)      1
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (U$)(*)      1
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (R$)(*)    1
    VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (U$)(*)    1
    VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (R$)     1
    VERBAS INDENIZATÓRIAS PROGRAMA DESLIGAMENTO VOLUNTÁRIO  MP 792/2017 (U$)     1
    TOTAL DE VERBAS INDENIZATÓRIAS (R$)(*)                                        1
    TOTAL DE VERBAS INDENIZATÓRIAS (U$)(*)                                        1
    dtype: int64




```python
df['REMUNERAÇÃO BÁSICA BRUTA (R$)'].value_counts()
```




    9570,41     8815
    32443,07    7652
    12132,29    6541
    0,00        6399
    11709,64    5758
    11085,51    4652
    5855,00     4560
    6586,66     4531
    24943,14    4479
    1250,00     3983
    11308,31    3939
    19368,90    3703
    9768,47     3612
    15413,91    3135
    15121,30    2818
    7994,01     2724
    5896,72     2571
    5867,05     2252
    7178,00     2086
    5982,53     2081
    4209,12     2062
    3301,93     2016
    3058,70     1852
    15860,21    1833
    7244,18     1810
    4220,04     1660
    2446,96     1594
    22058,99    1548
    3117,22     1542
    6724,29     1430
                ... 
    7328,88        1
    9100,54        1
    5481,04        1
    4155,21        1
    5002,81        1
    4818,53        1
    5249,39        1
    6232,31        1
    9172,80        1
    5074,88        1
    6545,95        1
    10645,72       1
    14367,08       1
    3836,70        1
    6277,70        1
    7646,18        1
    3731,80        1
    6046,79        1
    9731,73        1
    6930,83        1
    10016,52       1
    16359,25       1
    8556,69        1
    6462,48        1
    10320,09       1
    5755,78        1
    11180,37       1
    11237,51       1
    10897,88       1
    25478,49       1
    Name: REMUNERAÇÃO BÁSICA BRUTA (R$), Length: 125105, dtype: int64




```python
df['REMUNERAÇÃO BÁSICA BRUTA (U$)'].value_counts()
```




    0,00       567935
    5661,21         1
    6000,88         1
    Name: REMUNERAÇÃO BÁSICA BRUTA (U$), dtype: int64




```python
df['ABATE-TETO (R$)'].value_counts()
```




    0,00         566019
    -566,03         395
    -160,81         266
    -1796,48        137
    -6076,22         37
    -4365,94         12
    -1796,47         11
    -2825,22          8
    -9554,31          8
    -677,89           6
    -160,80           6
    -566,02           5
    -468,09           5
    -656,60           3
    -468,08           3
    -3134,69          2
    -1103,51          2
    -573,08           2
    -3218,16          2
    -1985,13          2
    -4296,68          2
    -2340,90          2
    -17257,23         2
    -7467,34          2
    -6147,40          2
    -4981,08          2
    -6076,34          2
    -2664,81          2
    -1166,26          2
    -4231,22          1
                  ...  
    -17736,44         1
    -7716,22          1
    -6807,80          1
    -490,13           1
    -2712,88          1
    -5728,40          1
    -3249,23          1
    -4669,09          1
    -246,00           1
    -9049,24          1
    -1562,26          1
    -2102,01          1
    -4778,33          1
    -920,05           1
    -884,36           1
    -4475,01          1
    -2479,74          1
    -3747,60          1
    -4228,53          1
    -32686,09         1
    -865,53           1
    -2330,46          1
    -3977,28          1
    -4119,56          1
    -8895,88          1
    -5802,47          1
    -3865,78          1
    -1042,91          1
    -2616,68          1
    -416,21           1
    Name: ABATE-TETO (R$), Length: 1017, dtype: int64


