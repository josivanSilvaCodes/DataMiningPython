

```python
import pandas as pd
import matplotlib.pyplot as plt
```


```python
# Abre o arquivo de cadastro
df = pd.read_csv("cadastro.csv", sep=";", encoding='ISO-8859-1')
# Lista as primeiras 50 linhas
df.head(50)
```

    /home/thiago/desenv/venv3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2785: DtypeWarning: Columns (23,29,30) have mixed types. Specify dtype option on import or set low_memory=False.
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
      <th>Id_SERVIDOR_PORTAL</th>
      <th>NOME</th>
      <th>CPF</th>
      <th>MATRICULA</th>
      <th>DESCRICAO_CARGO</th>
      <th>CLASSE_CARGO</th>
      <th>REFERENCIA_CARGO</th>
      <th>PADRAO_CARGO</th>
      <th>NIVEL_CARGO</th>
      <th>SIGLA_FUNCAO</th>
      <th>...</th>
      <th>JORNADA_DE_TRABALHO</th>
      <th>DATA_INGRESSO_CARGOFUNCAO</th>
      <th>DATA_NOMEACAO_CARGOFUNCAO</th>
      <th>DATA_INGRESSO_ORGAO</th>
      <th>DOCUMENTO_INGRESSO_SERVICOPUBLICO</th>
      <th>DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO</th>
      <th>DIPLOMA_INGRESSO_CARGOFUNCAO</th>
      <th>DIPLOMA_INGRESSO_ORGAO</th>
      <th>DIPLOMA_INGRESSO_SERVICOPUBLICO</th>
      <th>UF_EXERCICIO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4806495</td>
      <td>AARAO CARAJAS DIAS DOS SANTOS</td>
      <td>***.182.892-**</td>
      <td>022****</td>
      <td>Inválido</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>60 HORAS SEMANAIS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>02/03/2015</td>
      <td>S/N</td>
      <td>02/03/2015</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5116961</td>
      <td>AARAO CARLOS LUZ MACAMBIRA</td>
      <td>***.017.623-**</td>
      <td>016****</td>
      <td>BIBLIOTECARIO-DOCUMENTALISTA</td>
      <td>E</td>
      <td>0.0</td>
      <td>204</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>11/02/2009</td>
      <td>NaN</td>
      <td>29/12/2008</td>
      <td>699</td>
      <td>11/02/2009</td>
      <td>NaN</td>
      <td>LEI</td>
      <td>PORTARIA</td>
      <td>CE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>201964</td>
      <td>AARAO DIAMANTINO OLIVEIRA</td>
      <td>***.056.281-**</td>
      <td>000****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>FBC</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>31/08/2016</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>000000000</td>
      <td>05/01/1998</td>
      <td>NaN</td>
      <td>Inválido</td>
      <td>Inválido</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>201964</td>
      <td>AARAO DIAMANTINO OLIVEIRA</td>
      <td>***.056.281-**</td>
      <td>000****</td>
      <td>ANALISTA DO BANCO CENTRAL</td>
      <td>E</td>
      <td>NaN</td>
      <td>IV</td>
      <td>NaN</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>05/01/1998</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>000000000</td>
      <td>05/01/1998</td>
      <td>NaN</td>
      <td>Inválido</td>
      <td>Inválido</td>
      <td>DF</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4405000</td>
      <td>AARAO FERREIRA LIMA NETO</td>
      <td>***.116.132-**</td>
      <td>014****</td>
      <td>PROFESSOR DO MAGISTERIO SUPERIOR</td>
      <td>6</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>602.0</td>
      <td>-1</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>01/03/2013</td>
      <td>NaN</td>
      <td>24/07/2006</td>
      <td>2475</td>
      <td>16/08/2006</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4405000</td>
      <td>AARAO FERREIRA LIMA NETO</td>
      <td>***.116.132-**</td>
      <td>014****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>FG</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>13/04/2016</td>
      <td>NaN</td>
      <td>24/07/2006</td>
      <td>2475</td>
      <td>16/08/2006</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4915841</td>
      <td>AARAO PEREIRA DE ARAUJO JUNIOR</td>
      <td>***.031.184-**</td>
      <td>002****</td>
      <td>PROFESSOR ENS BASICO TECN TECNOLOGICO</td>
      <td>D</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>501.0</td>
      <td>-1</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>01/03/2013</td>
      <td>NaN</td>
      <td>29/12/2008</td>
      <td>000000124</td>
      <td>03/05/1993</td>
      <td>NaN</td>
      <td>LEI</td>
      <td>PORTARIA</td>
      <td>PB</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5105492</td>
      <td>AARAO SOARES</td>
      <td>***.859.807-**</td>
      <td>014****</td>
      <td>AGENTE DE COMBATE AS ENDEMIAS</td>
      <td>S</td>
      <td>0.0</td>
      <td>IV</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>03/12/2014</td>
      <td>NaN</td>
      <td>03/09/2014</td>
      <td>957/2006</td>
      <td>01/12/2014</td>
      <td>NaN</td>
      <td>LEI</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8114023</td>
      <td>AARAO TEIXEIRA DOS SANTOS</td>
      <td>***.086.942-**</td>
      <td>019****</td>
      <td>AGENTE ADMINISTRATIVO</td>
      <td>A</td>
      <td>0.0</td>
      <td>IV</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>02/04/2012</td>
      <td>NaN</td>
      <td>23/02/2012</td>
      <td>56</td>
      <td>02/04/2012</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>AP</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2671</td>
      <td>AARON DE SOUSA ALVES</td>
      <td>***.291.814-**</td>
      <td>022****</td>
      <td>PROFESSOR ENS BASICO TECN TECNOLOGICO</td>
      <td>D</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>101.0</td>
      <td>-1</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>12/11/2015</td>
      <td>NaN</td>
      <td>19/10/2015</td>
      <td>2410</td>
      <td>12/11/2015</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>PI</td>
    </tr>
    <tr>
      <th>10</th>
      <td>16237</td>
      <td>AARON INACIO FREIRE</td>
      <td>***.321.857-**</td>
      <td>022****</td>
      <td>ESP SUP DE ESTRATEGIA NUCLEAR - ESEN</td>
      <td>E</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>42.0</td>
      <td>-1</td>
      <td>...</td>
      <td>44 HORAS SEMANAIS</td>
      <td>01/08/2016</td>
      <td>NaN</td>
      <td>03/08/2015</td>
      <td>4372</td>
      <td>03/08/2015</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>912539</td>
      <td>AARON JONATHAN EDWARDS</td>
      <td>***.873.832-**</td>
      <td>028****</td>
      <td>PROFESSOR DO MAGISTERIO SUPERIOR</td>
      <td>4</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>502.0</td>
      <td>-1</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>08/01/2014</td>
      <td>NaN</td>
      <td>05/12/2013</td>
      <td>685</td>
      <td>08/01/2014</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>RR</td>
    </tr>
    <tr>
      <th>12</th>
      <td>6806485</td>
      <td>AARON JORDAN DA SILVA PENIDO</td>
      <td>***.624.556-**</td>
      <td>022****</td>
      <td>TEC DE TECNOLOGIA DA INFORMACAO</td>
      <td>D</td>
      <td>0.0</td>
      <td>101</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>18/11/2015</td>
      <td>NaN</td>
      <td>28/04/2014</td>
      <td>2345</td>
      <td>18/11/2015</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>13</th>
      <td>7703888</td>
      <td>AARON RAFAEL ERMEL GOMES</td>
      <td>***.750.040-**</td>
      <td>021****</td>
      <td>AGENTE METROV - OPERACAO DE ESTACAO</td>
      <td>1</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/07/2014</td>
      <td>NaN</td>
      <td>01/07/2014</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>Inválido</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2404623</td>
      <td>AARON SILVA DE LIMA</td>
      <td>***.724.317-**</td>
      <td>028****</td>
      <td>CONTRATADO LEI 8745-93 - NI</td>
      <td>A</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/04/2015</td>
      <td>NaN</td>
      <td>01/04/2015</td>
      <td>22</td>
      <td>01/04/2015</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>CONTRATO</td>
      <td>ES</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5710805</td>
      <td>ABADIA ADENISIA ROCHA E SILVA</td>
      <td>***.201.086-**</td>
      <td>022****</td>
      <td>ASSISTENTE EM ADMINISTRACAO</td>
      <td>D</td>
      <td>0.0</td>
      <td>202</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>18/06/2015</td>
      <td>NaN</td>
      <td>21/05/2015</td>
      <td>1055</td>
      <td>18/06/2015</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1713121</td>
      <td>ABADIA ALVES DA SILVA</td>
      <td>***.240.302-**</td>
      <td>023****</td>
      <td>AUXILIAR EM ENFERMAGEM</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>04/08/2016</td>
      <td>NaN</td>
      <td>04/08/2016</td>
      <td>NI</td>
      <td>29/06/1983</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>CONTRATO</td>
      <td>RO</td>
    </tr>
    <tr>
      <th>17</th>
      <td>5309978</td>
      <td>ABADIA CANDIDA LEMES</td>
      <td>***.834.461-**</td>
      <td>010****</td>
      <td>GUARDA DE ENDEMIAS</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>02/01/2007</td>
      <td>NaN</td>
      <td>29/06/2010</td>
      <td>000000019</td>
      <td>25/05/1987</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2206005</td>
      <td>ABADIA CRISTINA SOUZA SILVA</td>
      <td>***.839.371-**</td>
      <td>012****</td>
      <td>TECNICO</td>
      <td>3</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>26.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/07/2009</td>
      <td>NaN</td>
      <td>02/12/1985</td>
      <td>CCS DP 01</td>
      <td>02/12/1985</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6403578</td>
      <td>ABADIA DA GLORIA ARAUJO SPEZIA</td>
      <td>***.772.411-**</td>
      <td>014****</td>
      <td>ASSISTENTE ADMINISTRATIVO</td>
      <td>D</td>
      <td>0.0</td>
      <td>001</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/04/2013</td>
      <td>NaN</td>
      <td>01/12/2008</td>
      <td>357</td>
      <td>29/12/2008</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5113978</td>
      <td>ABADIA DE FATIMA RESENDE</td>
      <td>***.611.031-**</td>
      <td>018****</td>
      <td>TECNICO EM ENFERMAGEM</td>
      <td>D</td>
      <td>0.0</td>
      <td>405</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>09/08/2010</td>
      <td>NaN</td>
      <td>29/07/2010</td>
      <td>715</td>
      <td>30/07/2010</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MS</td>
    </tr>
    <tr>
      <th>21</th>
      <td>6118494</td>
      <td>ABADIA DE FATIMA ROSA MACEDO</td>
      <td>***.391.966-**</td>
      <td>014****</td>
      <td>PSICOLOGO-AREA</td>
      <td>E</td>
      <td>0.0</td>
      <td>408</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/03/2005</td>
      <td>NaN</td>
      <td>07/07/2004</td>
      <td>755</td>
      <td>15/07/2004</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1617447</td>
      <td>ABADIA DE MELO COUTINHO</td>
      <td>***.316.491-**</td>
      <td>000****</td>
      <td>AGENTE DE PORTARIA</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>15/12/1999</td>
      <td>NaN</td>
      <td>22/11/1984</td>
      <td>000153DPC</td>
      <td>26/12/1984</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>DF</td>
    </tr>
    <tr>
      <th>23</th>
      <td>7505648</td>
      <td>ABADIA DOS REIS NASCIMENTO</td>
      <td>***.922.001-**</td>
      <td>018****</td>
      <td>PROFESSOR DO MAGISTERIO SUPERIOR</td>
      <td>6</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>603.0</td>
      <td>-1</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>20/05/2011</td>
      <td>NaN</td>
      <td>29/04/2011</td>
      <td>1401</td>
      <td>20/05/2011</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>GO</td>
    </tr>
    <tr>
      <th>24</th>
      <td>5414482</td>
      <td>ABADIA GILDA BUSO MATOSO</td>
      <td>***.945.416-**</td>
      <td>031****</td>
      <td>PROFESSOR DO MAGISTERIO SUPERIOR</td>
      <td>5</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>501.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/07/2013</td>
      <td>NaN</td>
      <td>18/06/2013</td>
      <td>1936</td>
      <td>08/11/2012</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>25</th>
      <td>4611397</td>
      <td>ABADIA LEDA PRENCE BELLIARD</td>
      <td>***.080.181-**</td>
      <td>071****</td>
      <td>AGENTE ADMINISTRATIVO</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>02/01/2003</td>
      <td>NaN</td>
      <td>31/07/1986</td>
      <td>000000731</td>
      <td>31/07/1986</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MS</td>
    </tr>
    <tr>
      <th>26</th>
      <td>406342</td>
      <td>ABADIA MARIA APARECIDA TEIXEIRA</td>
      <td>***.890.176-**</td>
      <td>003****</td>
      <td>AUXILIAR DE SAUDE</td>
      <td>C</td>
      <td>0.0</td>
      <td>415</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>31/05/2001</td>
      <td>NaN</td>
      <td>31/07/1985</td>
      <td>162</td>
      <td>01/08/1985</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7300875</td>
      <td>ABADIA MARIA DE ALMEIDA DANTAS</td>
      <td>***.622.206-**</td>
      <td>011****</td>
      <td>AUXILIAR DE ENFERMAGEM</td>
      <td>C</td>
      <td>0.0</td>
      <td>212</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>31/05/2001</td>
      <td>NaN</td>
      <td>08/12/1995</td>
      <td>266</td>
      <td>13/12/1995</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>28</th>
      <td>7802383</td>
      <td>ABADIA MARIA FREIRE</td>
      <td>***.499.931-**</td>
      <td>004****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>FGR</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>14/03/2016</td>
      <td>NaN</td>
      <td>17/04/1991</td>
      <td>001</td>
      <td>27/08/1974</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>29</th>
      <td>7802383</td>
      <td>ABADIA MARIA FREIRE</td>
      <td>***.499.931-**</td>
      <td>004****</td>
      <td>AGENTE ADMINISTRATIVO</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/03/2006</td>
      <td>NaN</td>
      <td>17/04/1991</td>
      <td>001</td>
      <td>27/08/1974</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>6908546</td>
      <td>ABADIA PEREIRA DA SILVA</td>
      <td>***.539.541-**</td>
      <td>005****</td>
      <td>AUX OPERAC SERVICOS DIVERSOS</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/03/2006</td>
      <td>NaN</td>
      <td>30/01/1985</td>
      <td>GOAP-1620</td>
      <td>01/02/1985</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>31</th>
      <td>5210013</td>
      <td>ABADIA RODRIGUES DA SILVA</td>
      <td>***.296.501-**</td>
      <td>004****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>FGR</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>09/12/2016</td>
      <td>NaN</td>
      <td>14/05/1992</td>
      <td>00</td>
      <td>01/10/1981</td>
      <td>NaN</td>
      <td>LEI</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>32</th>
      <td>5210013</td>
      <td>ABADIA RODRIGUES DA SILVA</td>
      <td>***.296.501-**</td>
      <td>004****</td>
      <td>DATILOGRAFO</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>22/08/2005</td>
      <td>NaN</td>
      <td>14/05/1992</td>
      <td>00</td>
      <td>01/10/1981</td>
      <td>NaN</td>
      <td>LEI</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>33</th>
      <td>7406431</td>
      <td>ABADIA SIQUEIRA GOMES</td>
      <td>***.348.951-**</td>
      <td>035****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>DAS</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>03/05/2016</td>
      <td>NaN</td>
      <td>02/03/2015</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>Inválido</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>34</th>
      <td>1711106</td>
      <td>ABADIA VIEIRA CALACIA</td>
      <td>***.976.801-**</td>
      <td>011****</td>
      <td>AUXILIAR DE ENFERMAGEM</td>
      <td>C</td>
      <td>0.0</td>
      <td>313</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>31/05/2001</td>
      <td>NaN</td>
      <td>19/01/1995</td>
      <td>000001969</td>
      <td>19/01/1995</td>
      <td>NaN</td>
      <td>LEI</td>
      <td>LEI</td>
      <td>DF</td>
    </tr>
    <tr>
      <th>35</th>
      <td>1513349</td>
      <td>ABADIA VIEIRA DE ABREU</td>
      <td>***.327.601-**</td>
      <td>011****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>DAS</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>24/11/2016</td>
      <td>NaN</td>
      <td>06/03/1996</td>
      <td>117</td>
      <td>07/03/1996</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>36</th>
      <td>9013186</td>
      <td>ABADIANA FERREIRA MATIAS</td>
      <td>***.664.161-**</td>
      <td>022****</td>
      <td>TECNICO EM ENFERMAGEM - 36H</td>
      <td>T</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>101.0</td>
      <td>-1</td>
      <td>...</td>
      <td>36 HORAS SEMANAIS</td>
      <td>03/08/2015</td>
      <td>NaN</td>
      <td>03/08/2015</td>
      <td>000000000</td>
      <td>03/08/2015</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>37</th>
      <td>6412792</td>
      <td>ABADIAS CARDOSO MORAIS</td>
      <td>***.220.502-**</td>
      <td>009****</td>
      <td>ARTIFICE DE MECANICA</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>10/06/1999</td>
      <td>NaN</td>
      <td>20/03/1980</td>
      <td>S/N</td>
      <td>20/03/1980</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>CONTRATO</td>
      <td>PA</td>
    </tr>
    <tr>
      <th>38</th>
      <td>3804316</td>
      <td>ABADIAS EDESIO DE PAIVA</td>
      <td>***.808.901-**</td>
      <td>007****</td>
      <td>MOTORISTA OFICIAL</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/07/2006</td>
      <td>NaN</td>
      <td>01/01/1996</td>
      <td>SN</td>
      <td>02/03/1988</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>39</th>
      <td>3804316</td>
      <td>ABADIAS EDESIO DE PAIVA</td>
      <td>***.808.901-**</td>
      <td>007****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>GR</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>02/03/2011</td>
      <td>NaN</td>
      <td>01/01/1996</td>
      <td>SN</td>
      <td>02/03/1988</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>40</th>
      <td>4413304</td>
      <td>ABADICO JOSE FRANCISCO</td>
      <td>***.257.141-**</td>
      <td>004****</td>
      <td>AGENTE DE SAUDE PUBLICA</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>30/12/2006</td>
      <td>NaN</td>
      <td>29/06/2010</td>
      <td>326</td>
      <td>01/10/1982</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>41</th>
      <td>8414882</td>
      <td>ABADIO ALVES LIMA</td>
      <td>***.494.471-**</td>
      <td>004****</td>
      <td>GUARDA DE ENDEMIAS</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/03/2006</td>
      <td>NaN</td>
      <td>19/12/2010</td>
      <td>000000000</td>
      <td>01/09/1987</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>CONTRATO</td>
      <td>MS</td>
    </tr>
    <tr>
      <th>42</th>
      <td>7907862</td>
      <td>ABADIO DOS REIS SILVA LEITE</td>
      <td>***.968.426-**</td>
      <td>000****</td>
      <td>ASSISTENTE EM ADMINISTRACAO</td>
      <td>D</td>
      <td>0.0</td>
      <td>416</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/03/2005</td>
      <td>NaN</td>
      <td>29/12/2008</td>
      <td>107</td>
      <td>23/01/1984</td>
      <td>NaN</td>
      <td>LEI</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>43</th>
      <td>7011242</td>
      <td>ABADIO DOS SANTOS</td>
      <td>***.123.811-**</td>
      <td>000****</td>
      <td>MOTORISTA OFICIAL</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/07/2006</td>
      <td>NaN</td>
      <td>03/07/1979</td>
      <td>1726DPC</td>
      <td>01/08/1979</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MS</td>
    </tr>
    <tr>
      <th>44</th>
      <td>6203095</td>
      <td>ABADIO FELIX</td>
      <td>***.924.806-**</td>
      <td>004****</td>
      <td>AGENTE DE SAUDE PUBLICA</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/03/2006</td>
      <td>NaN</td>
      <td>29/06/2010</td>
      <td>SN</td>
      <td>06/10/1975</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>45</th>
      <td>4311612</td>
      <td>ABADIO GONCALVES CAETANO</td>
      <td>***.811.056-**</td>
      <td>063****</td>
      <td>PROFESSOR DO MAGISTERIO SUPERIOR</td>
      <td>6</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>604.0</td>
      <td>-1</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>01/08/2011</td>
      <td>NaN</td>
      <td>09/10/2009</td>
      <td>397</td>
      <td>27/10/2009</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>46</th>
      <td>4311612</td>
      <td>ABADIO GONCALVES CAETANO</td>
      <td>***.811.056-**</td>
      <td>003****</td>
      <td>PROFESSOR DO MAGISTERIO SUPERIOR</td>
      <td>7</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>701.0</td>
      <td>-1</td>
      <td>...</td>
      <td>DEDICACAO EXCLUSIVA</td>
      <td>12/12/1990</td>
      <td>NaN</td>
      <td>01/02/1979</td>
      <td>17</td>
      <td>01/02/1979</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>47</th>
      <td>7415752</td>
      <td>ABADIO HERMES VIEIRA</td>
      <td>***.425.701-**</td>
      <td>012****</td>
      <td>PESQUISADOR-B</td>
      <td>B</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>16.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/07/2015</td>
      <td>NaN</td>
      <td>01/11/1989</td>
      <td>SN</td>
      <td>01/11/1989</td>
      <td>NaN</td>
      <td>CONTRATO</td>
      <td>CONTRATO</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>48</th>
      <td>4414745</td>
      <td>ABADIO JOSE VITAL</td>
      <td>***.523.496-**</td>
      <td>010****</td>
      <td>POLICIAL RODOVIARIO FEDERAL</td>
      <td>S</td>
      <td>0.0</td>
      <td>III</td>
      <td>0.0</td>
      <td>-1</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>01/08/2006</td>
      <td>NaN</td>
      <td>04/05/2004</td>
      <td>000000441</td>
      <td>13/07/1994</td>
      <td>NaN</td>
      <td>DECRETO</td>
      <td>PORTARIA</td>
      <td>MG</td>
    </tr>
    <tr>
      <th>49</th>
      <td>906745</td>
      <td>ABADIO MENDES FERREIRA</td>
      <td>***.128.531-**</td>
      <td>015****</td>
      <td>Sem informação</td>
      <td>NaN</td>
      <td>-1.0</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>RGA</td>
      <td>...</td>
      <td>40 HORAS SEMANAIS</td>
      <td>04/01/2016</td>
      <td>NaN</td>
      <td>18/05/2007</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PORTARIA</td>
      <td>Inválido</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>50 rows × 42 columns</p>
</div>




```python
# Exibe todas as colunas
df.columns
```




    Index(['Id_SERVIDOR_PORTAL', 'NOME', 'CPF', 'MATRICULA', 'DESCRICAO_CARGO',
           'CLASSE_CARGO', 'REFERENCIA_CARGO', 'PADRAO_CARGO', 'NIVEL_CARGO',
           'SIGLA_FUNCAO', 'NIVEL_FUNCAO', 'FUNCAO', 'CODIGO_ATIVIDADE',
           'ATIVIDADE', 'OPCAO_PARCIAL', 'COD_UORG_LOTACAO', 'UORG_LOTACAO',
           'COD_ORG_LOTACAO', 'ORG_LOTACAO', 'COD_ORGSUP_LOTACAO',
           'ORGSUP_LOTACAO', 'COD_UORG_EXERCICIO', 'UORG_EXERCICIO',
           'COD_ORG_EXERCICIO', 'ORG_EXERCICIO', 'COD_ORGSUP_EXERCICIO',
           'ORGSUP_EXERCICIO', 'TIPO_VINCULO', 'SITUACAO_VINCULO',
           'DATA_INICIO_AFASTAMENTO', 'DATA_TERMINO_AFASTAMENTO',
           'REGIME_JURIDICO', 'JORNADA_DE_TRABALHO', 'DATA_INGRESSO_CARGOFUNCAO',
           'DATA_NOMEACAO_CARGOFUNCAO', 'DATA_INGRESSO_ORGAO',
           'DOCUMENTO_INGRESSO_SERVICOPUBLICO',
           'DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO', 'DIPLOMA_INGRESSO_CARGOFUNCAO',
           'DIPLOMA_INGRESSO_ORGAO', 'DIPLOMA_INGRESSO_SERVICOPUBLICO',
           'UF_EXERCICIO'],
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
      <th>Id_SERVIDOR_PORTAL</th>
      <th>REFERENCIA_CARGO</th>
      <th>NIVEL_CARGO</th>
      <th>OPCAO_PARCIAL</th>
      <th>COD_UORG_LOTACAO</th>
      <th>COD_ORG_LOTACAO</th>
      <th>COD_ORGSUP_LOTACAO</th>
      <th>COD_UORG_EXERCICIO</th>
      <th>COD_ORGSUP_EXERCICIO</th>
      <th>TIPO_VINCULO</th>
      <th>DATA_NOMEACAO_CARGOFUNCAO</th>
      <th>DIPLOMA_INGRESSO_CARGOFUNCAO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7.856980e+05</td>
      <td>781661.000000</td>
      <td>781661.000000</td>
      <td>0.0</td>
      <td>7.856980e+05</td>
      <td>785698.000000</td>
      <td>785698.000000</td>
      <td>7.856980e+05</td>
      <td>785698.000000</td>
      <td>785698.000000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4.838464e+06</td>
      <td>-0.134013</td>
      <td>92.338761</td>
      <td>NaN</td>
      <td>2.788247e+13</td>
      <td>30333.764856</td>
      <td>16387.997192</td>
      <td>2.600247e+13</td>
      <td>16123.824406</td>
      <td>1.930552</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.251733e+06</td>
      <td>0.340667</td>
      <td>204.342546</td>
      <td>NaN</td>
      <td>1.461801e+13</td>
      <td>12996.185654</td>
      <td>14580.239951</td>
      <td>1.577518e+13</td>
      <td>14500.771733</td>
      <td>0.438610</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000e+00</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>NaN</td>
      <td>-3.000000e+00</td>
      <td>101.000000</td>
      <td>-1.000000</td>
      <td>-3.000000e+00</td>
      <td>-1.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.401668e+06</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>2.500000e+13</td>
      <td>25000.000000</td>
      <td>13000.000000</td>
      <td>2.300000e+13</td>
      <td>-1.000000</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.800826e+06</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>2.625300e+13</td>
      <td>26262.000000</td>
      <td>15000.000000</td>
      <td>2.624600e+13</td>
      <td>15000.000000</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.204446e+06</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>2.644302e+13</td>
      <td>29205.000000</td>
      <td>17000.000000</td>
      <td>2.643600e+13</td>
      <td>17000.000000</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.794119e+07</td>
      <td>0.000000</td>
      <td>814.000000</td>
      <td>NaN</td>
      <td>9.907220e+13</td>
      <td>99993.000000</td>
      <td>70000.000000</td>
      <td>9.901340e+13</td>
      <td>70000.000000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Número total de linhas ou objetos
df.shape
```




    (785698, 42)




```python
# Quantidade de itens faltantes de cada coluna
df.count()
```




    Id_SERVIDOR_PORTAL                      785698
    NOME                                    785698
    CPF                                     785698
    MATRICULA                               785698
    DESCRICAO_CARGO                         785698
    CLASSE_CARGO                            627734
    REFERENCIA_CARGO                        781661
    PADRAO_CARGO                            527763
    NIVEL_CARGO                             781661
    SIGLA_FUNCAO                            785698
    NIVEL_FUNCAO                            784684
    FUNCAO                                  785698
    CODIGO_ATIVIDADE                        785698
    ATIVIDADE                               785698
    OPCAO_PARCIAL                                0
    COD_UORG_LOTACAO                        785698
    UORG_LOTACAO                            785698
    COD_ORG_LOTACAO                         785698
    ORG_LOTACAO                             785698
    COD_ORGSUP_LOTACAO                      785698
    ORGSUP_LOTACAO                          785698
    COD_UORG_EXERCICIO                      785698
    UORG_EXERCICIO                          785698
    COD_ORG_EXERCICIO                       785698
    ORG_EXERCICIO                           785698
    COD_ORGSUP_EXERCICIO                    785698
    ORGSUP_EXERCICIO                        785698
    TIPO_VINCULO                            785698
    SITUACAO_VINCULO                        785698
    DATA_INICIO_AFASTAMENTO                    430
    DATA_TERMINO_AFASTAMENTO                   408
    REGIME_JURIDICO                         785698
    JORNADA_DE_TRABALHO                     785698
    DATA_INGRESSO_CARGOFUNCAO               735510
    DATA_NOMEACAO_CARGOFUNCAO                    0
    DATA_INGRESSO_ORGAO                     783229
    DOCUMENTO_INGRESSO_SERVICOPUBLICO       737779
    DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO    743446
    DIPLOMA_INGRESSO_CARGOFUNCAO                 0
    DIPLOMA_INGRESSO_ORGAO                  785698
    DIPLOMA_INGRESSO_SERVICOPUBLICO         785698
    UF_EXERCICIO                            785698
    dtype: int64




```python
# Função que mostra a quantidade de itens faltantes por coluna, zero não falta nenhuma informação
df.apply(lambda x: sum(x.isnull()),axis=0)
```




    Id_SERVIDOR_PORTAL                           0
    NOME                                         0
    CPF                                          0
    MATRICULA                                    0
    DESCRICAO_CARGO                              0
    CLASSE_CARGO                            157964
    REFERENCIA_CARGO                          4037
    PADRAO_CARGO                            257935
    NIVEL_CARGO                               4037
    SIGLA_FUNCAO                                 0
    NIVEL_FUNCAO                              1014
    FUNCAO                                       0
    CODIGO_ATIVIDADE                             0
    ATIVIDADE                                    0
    OPCAO_PARCIAL                           785698
    COD_UORG_LOTACAO                             0
    UORG_LOTACAO                                 0
    COD_ORG_LOTACAO                              0
    ORG_LOTACAO                                  0
    COD_ORGSUP_LOTACAO                           0
    ORGSUP_LOTACAO                               0
    COD_UORG_EXERCICIO                           0
    UORG_EXERCICIO                               0
    COD_ORG_EXERCICIO                            0
    ORG_EXERCICIO                                0
    COD_ORGSUP_EXERCICIO                         0
    ORGSUP_EXERCICIO                             0
    TIPO_VINCULO                                 0
    SITUACAO_VINCULO                             0
    DATA_INICIO_AFASTAMENTO                 785268
    DATA_TERMINO_AFASTAMENTO                785290
    REGIME_JURIDICO                              0
    JORNADA_DE_TRABALHO                          0
    DATA_INGRESSO_CARGOFUNCAO                50188
    DATA_NOMEACAO_CARGOFUNCAO               785698
    DATA_INGRESSO_ORGAO                       2469
    DOCUMENTO_INGRESSO_SERVICOPUBLICO        47919
    DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO     42252
    DIPLOMA_INGRESSO_CARGOFUNCAO            785698
    DIPLOMA_INGRESSO_ORGAO                       0
    DIPLOMA_INGRESSO_SERVICOPUBLICO              0
    UF_EXERCICIO                                 0
    dtype: int64




```python
# Faz uma análise da frequencia de uma coluna especifica mostrando quais variaveis tem maior frequencia
df['DESCRICAO_CARGO'].value_counts()
```




    Sem informação                              104753
    PROFESSOR DO MAGISTERIO SUPERIOR             84066
    Inválido                                     50188
    PROFESSOR ENS BASICO TECN TECNOLOGICO        42643
    ASSISTENTE EM ADMINISTRACAO                  33171
    AGENTE ADMINISTRATIVO                        24619
    TECNICO DO SEGURO SOCIAL                     23423
    AUXILIAR DE ENFERMAGEM                       16610
    AUDITOR-FISCAL DA RECEITA FEDERAL BRASIL     10044
    AGENTE DE SAUDE PUBLICA                       9561
    TECNICO DE LABORATORIO AREA                   9276
    MEDICO                                        8922
    POLICIAL RODOVIARIO FEDERAL                   8790
    TECNICO EM ENFERMAGEM - 36H                   7543
    ANALISTA TRIBUTARIO REC FEDERAL BRASIL        6995
    PROFESSOR MAGISTERIO SUPERIOR-SUBSTITUTO      6922
    MEDICO-AREA                                   6763
    ADMINISTRADOR                                 6554
    AUX EM ADMINISTRACAO                          6152
    GUARDA DE ENDEMIAS                            5587
    TECNICO                                       5468
    DATILOGRAFO                                   5072
    TECNICO EM ENFERMAGEM                         5038
    TECNICO EM ASSUNTOS EDUCACIONAIS              4988
    AGENTE DE COMBATE AS ENDEMIAS                 4826
    AGENTE DE PORTARIA                            4686
    MEDICO - 24H                                  4631
    ANALISTA DO SEGURO SOCIAL                     4529
    ANALISTA                                      4197
    CONTRATADO LEI 8745-93 - NI                   4176
                                                 ...  
    ASSISTENTE DE SUPRIMENTO                         1
    OPERADOR DE TELEPROMPTER                         1
    ANALISTA DE CONTRATO                             1
    ANALISTA DESEMPENHO EMPRESARIAL SUPERIOR         1
    AUX EM PROGRAMACAO VISUAL III                    1
    PINTOR ESPECIALIZADO                             1
    MEDICO-PROFISSIONAL TECNICO SUPERIOR II          1
    CONFERENTE DE CAPATAZIAS                         1
    TEC EM PROGRAMACAO VISUAL III                    1
    TECNICO DE PROCESSAMENTO DADOS                   1
    AGENTE DE DEFESA FLORESTAL                       1
    OPERADOR DE GERADOR DE CARACTERES                1
    ARTIF ESPEC DE ELETR E COMUNICACOES              1
    BOMBEIRO 2 0                                     1
    TECNICO EM SERVICOS DE ESCRITORIO                1
    ANALISTA JUNIOR                                  1
    ANALISTA DE CADASTRO DE EMPRESA                  1
    TNS - ARQUIVISTA                                 1
    AGENTE ANALISTA SIST SOCIO ECONOMICO             1
    ANALISTA DE SISTEMAS E METODOS                   1
    SERRALHEIRO II                                   1
    TECNICO DE DISTRIBUICAO I                        1
    ESPECIALISTA V                                   1
    MEDICO DE SAUDE PUBLICA                          1
    ANALISTA CADASTRO EMPRESA                        1
    OFICIAL ADMINISTRATIVO                           1
    PROIND - AJUDANTE                                1
    ASS ADMINISTRATIVO III                           1
    ASSISTENTE ADMINISTRTIVO                         1
    LABORATORISTA JORNADA 8HORAS                     1
    Name: DESCRICAO_CARGO, Length: 2219, dtype: int64




```python
df['DESCRICAO_CARGO'].describe()
```




    count             785698
    unique              2219
    top       Sem informação
    freq              104753
    Name: DESCRICAO_CARGO, dtype: object




```python
df['UORG_EXERCICIO'].value_counts()
```




    Inválido                                    115227
    COORDENADORIA DE GESTAO DE PESSOAS            5968
    BANCO CENTRAL DO BRASIL                       5205
    SEC DE GESTAO DO TRAB E DA EDUC NA SAUDE      4882
    UNIDADE PAGADORA/SP                           4713
    COORDENACAO ASSISTENCIAL                      2758
    SERVICO DE ENFERMAGEM                         2535
    SECRETARIA DE ESTADO DA EDUCACAO              2182
    UNIDADE PAGADORA/RJ                           2165
    HOSPITAL DAS CLINICAS                         1790
    UNIDADE PAGADORA/MG                           1475
    RESIDENCIA MEDICA ALUNO                       1473
    SECD DE RR EM BOA VISTA                       1389
    SECRETARIA DE ESTADO DA SAUDE                 1318
    REITORIA                                      1271
    COORDENACAO DE ENFERMAGEM                     1250
    SERVICO DE GESTAO ADMINISTRATIVA              1226
    SEPLAD/RO EM PORTO VELHO                      1214
    DIRETORIA DE DESENVOLVIMENTO AO ENSINO        1147
    HOSPITAL FEDERAL DE BONSUCESSO (UPAG)         1135
    Divisao de Financas - HFA                     1109
    HOSPITAL UNIVERSITARIO WALTER CANTIDIO        1101
    SEC DE SAUDE DO TRABALHADOR                   1056
    SEC DE LOG,LIC E CONTRATOS E ENGENHARIA       1022
    DIVISAO DE ENFERMAGEM                         1016
    DIVISAO MEDICO-ASSISTENCIAL                   1004
    COORDENACAO ASSISTENCIAL/HFCF                  990
    HC - HOSPITAL DE CLINICAS                      911
    UNIDADE PAGADORA/RS                            887
    HOSP-HOSPITAL UNIVERSITARIO DE BRASILIA        876
                                                 ...  
    COORD PROG ACADEMICOS DA FAC DE DIREITO          1
    SEINT/VIAMAO-RS                                  1
    RESTAURANTE UNIVERSITARIO - CAMPUS JUA           1
    FAF-COLEG 1 CICLO CIEN SOC                       1
    SERVICO DE ATENDIMENTO AO VISITANTE              1
    SERV DE SECRET EXECUTIVA DAS MEMORIAS            1
    DIV DE PROG CONTROLE AVAL ORCAMENTARIA           1
    APS - CATALAO                                    1
    COORD DE LEGISLACAO E NORMAS                     1
    EEF-NUC ASSESSORAMENTO A PESQUISA                1
    COORD TEC LOC EM ALTA FLORESTA                   1
    NUCLEO - ESTACOES_TRECHO B 2 TURNO               1
    COORD1/CGRAP/GAB/SAJ/CC                          1
    NUCLEO MOV.PENSÃO, APOS.E BENEFICIOS-REI         1
    COORDENACAO GERAL DE COOP E ARTIC DE POL         1
    COORD PROC AGRARIOS,LEGISL,NORMAS E PESQ         1
    NUCLEO DE PESQ EM ANIMAIS DE LABORATORIO         1
    SERVIÇO DE ADM DE PESSOAL                        1
    SERT/IJUI-RS                                     1
    SSP EM JAMARI                                    1
    ASSESSOR ADM CAMPUS CENTROS EDU PROF-RE          1
    Coord.Saude e Qualidade de Vida                  1
    Hosp. Secao de Farmacia                          1
    HOSP-SEC PAGAMENTOS/DIV FINANC 1o L/HSV          1
    NÚCLEO CONTAB.E PRESTAÇÃO DE CONTAS-RV           1
    UNIDADE DE DOCUMENAçãO E INFORMAçãO              1
    SDT. EM CONSELHEIRO LAFAIETE-MG                  1
    SETOR DE AUDITORIA - SFS                         1
    COORD-GERAL AN JUR LIC CON INST CONGENER         1
    SEC CON EMED PARL  CADASTRAMENTO                 1
    Name: UORG_EXERCICIO, Length: 54316, dtype: int64




```python
df['UORG_EXERCICIO'].describe()
df['UORG_EXERCICIO'].mean()
```


```python
df['ORG_LOTACAO'].value_counts()
```




    MINISTERIO DA SAUDE                         89991
    INSTITUTO NACIONAL DE SEGURO SOCIAL         42538
    MINISTERIO DA FAZENDA                       37394
    EMPRESA BRAS. DE SERVICOS HOSPITALARES      23003
    UNIVERSIDADE FEDERAL DO RIO DE JANEIRO      16818
    FUND. INST. BRASIL. GEOG. E ESTATISTICA     12816
    MINIST.DA AGRICULTURA,PECUARIA E ABAST.     12464
    SERVICO FED. DE PROCESSAMENTO DE DADOS      11517
    DEPTO. DE POLICIA RODOVIARIA FEDERAL        10088
    EMPRESA BRASILEIRA DE PESQ. AGROPECUARIA     9779
    ADVOCACIA-GERAL DA UNIAO                     9696
    UNIVERSIDADE FEDERAL DE MINAS GERAIS         9321
    MINISTERIO DO TRABALHO E EMPREGO             9266
    UNIVERSIDADE FEDERAL FLUMINENSE              8997
    MINISTERIO DO PLANEJ. DESENV. E GESTAO       8871
    UNIVERSIDADE FEDERAL DE PERNAMBUCO           8557
    FUNDACAO NACIONAL DE SAUDE                   7967
    UNIVERSIDADE FEDERAL DO PARANA               7961
    UNIVERSIDADE FEDERAL DO CEARA                7765
    UNIVERSIDADE FEDERAL DA PARAIBA              7584
    UNIVERSIDADE FEDERAL DE SAO PAULO            7562
    FUNDACAO UNIVERSIDADE DE BRASILIA            7513
    UNIVERSIDADE FEDERAL DA BAHIA                7217
    UNIVERSIDADE FED. DO RIO GRANDE DO NORTE     7165
    COMANDO DO EXERCITO                          7057
    UNIVERSIDADE FEDERAL DE SANTA CATARINA       7046
    HOSPITAL DE CLINICAS DE PORTO ALEGRE         7010
    UNIVERSIDADE FEDERAL DO PARA                 6777
    UNIVERSIDADE FED. DO RIO GRANDE DO SUL       6696
    FUNDACAO UNIV. FEDERAL DE UBERLANDIA         6499
                                                ...  
    GOVERNO DO ESTADO DO CEARA                      4
    GOVERNO DO ESTADO DO MATO GROSSO DO SUL         3
    TRIBUNAL REGIONAL FEDERAL 1A REGIAO / DF        3
    PREFEITURA MUNICIPAL DE RECIFE/PE               3
    SUPREMO TRIBUNAL FEDERAL                        3
    TRIBUNAL DE JUSTICA                             3
    GOVERNO DO ESTADO DO ESPIRITO SANTO             3
    GOVERNO DO ESTADO DE SANTA CATARINA             2
    COMPANHIA DE COLONIZACAO DO NORDESTE            2
    CAMARA LEGISLATIVA DO DF                        2
    EMPRESAS PUBLICAS/CLT                           2
    TRIBUNAL SUPERIOR DO TRABALHO                   2
    GOVERNO DO ESTADO DE SERGIPE                    2
    MINISTERIO PUBLICO DO TRABALHO                  2
    PROCURADORIA GERAL DA REPUBLICA                 2
    FINANCIADORA DE ESTUDOS E PROJETOS              2
    BANCO DO NORDESTE DO BRASIL                     2
    PREFEITURA MUNICIPAL DE PORTO VELHO-RO          1
    PREFEITURA MUNICIPAL DE VITORIA/ES              1
    TRIBUNAL REGIONAL ELEITORAL - MA                1
    TRIBUNAL REGIONAL FEDERAL                       1
    PREFEITURA MUNICIPAL DE FORTALEZA / CE          1
    TRIBUNAL DE CONTAS DA UNIAO                     1
    TRIBUNAL REGIONAL DO TRABALHO-MT                1
    TRIBUNAL REGIONAL FEDERAL 3A REGIAO/SP          1
    PREFEITURA DE SAO LUIZ/MA                       1
    TRIBUNAL REGIONAL ELEITORAL - CE                1
    VICE-PRESIDENCIA DA REPUBLICA                   1
    MINIST. PUBLICO DO DF E TERRITORIOS             1
    TRIBUNAL REGIONAL ELEITORAL - SP                1
    Name: ORG_LOTACAO, Length: 292, dtype: int64




```python
df['ORGSUP_LOTACAO'].value_counts()
```




    MINISTERIO DA EDUCACAO                      369365
    Sem informação                              195132
    MINISTERIO DO DESENVOLVIMENTO SOCIAL         42538
    MINISTERIO DO PLANEJ. DESENV. E GESTAO       27876
    PRESIDENCIA DA REPUBLICA                     22992
    MINISTERIO DA DEFESA                         19245
    MINISTERIO DA SAUDE                          17703
    MINIST.DA AGRICULTURA,PECUARIA E ABAST.      15926
    MINISTERIO DA JUSTIÇA                        13209
    MINISTERIO DA FAZENDA                        12782
    MINIST.DA CIÊNCIA,TEC. INOV.E COMUNIÇÕES      8100
    MINISTERIO DO MEIO AMBIENTE                   7536
    MINISTERIO DE MINAS E ENERGIA                 6694
    MINIST.TRANSP.,PORTOS E AVIACAO CIVIL         6565
    MINISTERIO DAS CIDADES                        6056
    MINISTERIO DA INTEGRACAO NACIONAL             5009
    MINISTERIO DA CULTURA                         3463
    MINISTERIO IND. COM. EXTERIOR E SERVIçOS      2924
    COMANDO DA MARINHA                            1684
    MINISTERIO DO TRABALHO E EMPREGO               370
    MINISTERIO DO TURISMO                          204
    COMANDO DO EXERCITO                            112
    MINISTERIO DAS RELACOES EXTERIORES              88
    MINISTERIO DA PREVIDENCIA SOCIAL                65
    MINISTERIO DO ESPORTE                           50
    COMANDO DA AERONAUTICA                          10
    Name: ORGSUP_LOTACAO, dtype: int64




```python
df['ORG_LOTACAO'].value_counts()
```




    MINISTERIO DA SAUDE                         89991
    INSTITUTO NACIONAL DE SEGURO SOCIAL         42538
    MINISTERIO DA FAZENDA                       37394
    EMPRESA BRAS. DE SERVICOS HOSPITALARES      23003
    UNIVERSIDADE FEDERAL DO RIO DE JANEIRO      16818
    FUND. INST. BRASIL. GEOG. E ESTATISTICA     12816
    MINIST.DA AGRICULTURA,PECUARIA E ABAST.     12464
    SERVICO FED. DE PROCESSAMENTO DE DADOS      11517
    DEPTO. DE POLICIA RODOVIARIA FEDERAL        10088
    EMPRESA BRASILEIRA DE PESQ. AGROPECUARIA     9779
    ADVOCACIA-GERAL DA UNIAO                     9696
    UNIVERSIDADE FEDERAL DE MINAS GERAIS         9321
    MINISTERIO DO TRABALHO E EMPREGO             9266
    UNIVERSIDADE FEDERAL FLUMINENSE              8997
    MINISTERIO DO PLANEJ. DESENV. E GESTAO       8871
    UNIVERSIDADE FEDERAL DE PERNAMBUCO           8557
    FUNDACAO NACIONAL DE SAUDE                   7967
    UNIVERSIDADE FEDERAL DO PARANA               7961
    UNIVERSIDADE FEDERAL DO CEARA                7765
    UNIVERSIDADE FEDERAL DA PARAIBA              7584
    UNIVERSIDADE FEDERAL DE SAO PAULO            7562
    FUNDACAO UNIVERSIDADE DE BRASILIA            7513
    UNIVERSIDADE FEDERAL DA BAHIA                7217
    UNIVERSIDADE FED. DO RIO GRANDE DO NORTE     7165
    COMANDO DO EXERCITO                          7057
    UNIVERSIDADE FEDERAL DE SANTA CATARINA       7046
    HOSPITAL DE CLINICAS DE PORTO ALEGRE         7010
    UNIVERSIDADE FEDERAL DO PARA                 6777
    UNIVERSIDADE FED. DO RIO GRANDE DO SUL       6696
    FUNDACAO UNIV. FEDERAL DE UBERLANDIA         6499
                                                ...  
    GOVERNO DO ESTADO DO CEARA                      4
    GOVERNO DO ESTADO DO MATO GROSSO DO SUL         3
    TRIBUNAL REGIONAL FEDERAL 1A REGIAO / DF        3
    PREFEITURA MUNICIPAL DE RECIFE/PE               3
    SUPREMO TRIBUNAL FEDERAL                        3
    TRIBUNAL DE JUSTICA                             3
    GOVERNO DO ESTADO DO ESPIRITO SANTO             3
    GOVERNO DO ESTADO DE SANTA CATARINA             2
    COMPANHIA DE COLONIZACAO DO NORDESTE            2
    CAMARA LEGISLATIVA DO DF                        2
    EMPRESAS PUBLICAS/CLT                           2
    TRIBUNAL SUPERIOR DO TRABALHO                   2
    GOVERNO DO ESTADO DE SERGIPE                    2
    MINISTERIO PUBLICO DO TRABALHO                  2
    PROCURADORIA GERAL DA REPUBLICA                 2
    FINANCIADORA DE ESTUDOS E PROJETOS              2
    BANCO DO NORDESTE DO BRASIL                     2
    PREFEITURA MUNICIPAL DE PORTO VELHO-RO          1
    PREFEITURA MUNICIPAL DE VITORIA/ES              1
    TRIBUNAL REGIONAL ELEITORAL - MA                1
    TRIBUNAL REGIONAL FEDERAL                       1
    PREFEITURA MUNICIPAL DE FORTALEZA / CE          1
    TRIBUNAL DE CONTAS DA UNIAO                     1
    TRIBUNAL REGIONAL DO TRABALHO-MT                1
    TRIBUNAL REGIONAL FEDERAL 3A REGIAO/SP          1
    PREFEITURA DE SAO LUIZ/MA                       1
    TRIBUNAL REGIONAL ELEITORAL - CE                1
    VICE-PRESIDENCIA DA REPUBLICA                   1
    MINIST. PUBLICO DO DF E TERRITORIOS             1
    TRIBUNAL REGIONAL ELEITORAL - SP                1
    Name: ORG_LOTACAO, Length: 292, dtype: int64




```python
df['ORG_EXERCICIO'].value_counts()
```




    MINISTERIO DA SAUDE                         54235
    INSTITUTO NACIONAL DE SEGURO SOCIAL         40840
    ESTADOS / MUNICIPIOS / EMPRESAS             39659
    MINISTERIO DA FAZENDA                       37227
    EMPRESA BRAS. DE SERVICOS HOSPITALARES      25683
    UNIVERSIDADE FEDERAL DO RIO DE JANEIRO      16783
    MINIST.DA AGRICULTURA,PECUARIA E ABAST.     12950
    FUND. INST. BRASIL. GEOG. E ESTATISTICA     12689
    ADVOCACIA-GERAL DA UNIAO                    10592
    SERVICO FED. DE PROCESSAMENTO DE DADOS      10404
    DEPTO. DE POLICIA RODOVIARIA FEDERAL        10046
    MINISTERIO DO TRABALHO E EMPREGO             9793
    EMPRESA BRASILEIRA DE PESQ. AGROPECUARIA     9567
    UNIVERSIDADE FEDERAL DE MINAS GERAIS         9260
    UNIVERSIDADE FEDERAL FLUMINENSE              9153
    UNIVERSIDADE FEDERAL DE PERNAMBUCO           8456
    UNIVERSIDADE FEDERAL DO PARANA               7877
    UNIVERSIDADE FEDERAL DO CEARA                7594
    UNIVERSIDADE FEDERAL DE SAO PAULO            7584
    UNIVERSIDADE FEDERAL DA PARAIBA              7530
    FUNDACAO UNIVERSIDADE DE BRASILIA            7292
    UNIVERSIDADE FEDERAL DE SANTA CATARINA       7051
    UNIVERSIDADE FEDERAL DA BAHIA                7023
    HOSPITAL DE CLINICAS DE PORTO ALEGRE         7017
    UNIVERSIDADE FED. DO RIO GRANDE DO NORTE     6937
    COMANDO DO EXERCITO                          6856
    UNIVERSIDADE FED. DO RIO GRANDE DO SUL       6706
    UNIVERSIDADE FEDERAL DO PARA                 6635
    FUNDACAO UNIV. FEDERAL DE UBERLANDIA         6511
    GOVERNO DO EX-TERRITORIO DO AMAPA            6406
                                                ...  
    COMPANHIA DE COLONIZACAO DO NORDESTE            2
    GOVERNO DO ESTADO DE SERGIPE                    2
    FUND.PREV.COMPL.SERV.PUBLICO FEDERAL            2
    TELEBRAS - HOLDING                              2
    ASSEMBLEIA LEGISLATIVA - CE                     2
    COMPANHIA ENERGETICA DE BRASILIA                2
    MINISTERIO DA EDUCACAO E DO DESPORTO            1
    PREFEITURA MUNICIPAL DE ARACAJU - SE            1
    ASSEMBLEIA LEGISLATIVA - MG                     1
    SUPERINTENDENCIA NAC.PREV.COMPLEMENTAR          1
    PREFEITURA MUNICIPAL DO RIO DE JANEIRO          1
    TRIBUNAL REGIONAL ELEITORAL - PR                1
    MINISTERIO TRABALHO PREVIDÊNCIA SOCIAL          1
    FUND.BCO.CENTRAL DE PREVIDENCIA PRIVADA         1
    TRIBUNAL REGIONAL FEDERAL 3A REGIAO/SP          1
    PETROBRAS - HOLDING                             1
    ASSOC.DE COMUNICACAO EDUCATIVA ROQ.PINTO        1
    TRIBUNAL REGIONAL DO TRABALHO - AL              1
    CENTRO DE PESQUISAS DE ENERGIA ELETRICA         1
    JUSTICA FEDERAL - AP                            1
    TRIBUNAL DE CONTAS DA UNIAO                     1
    BANCO NAC. DE DESENV. ECONOMICO E SOCIAL        1
    COMPANHIA DOCAS DE SAO PAULO                    1
    MINISTERIO DAS COMUNICACOES                     1
    EX-MINISTERIO DO BEM-ESTAR SOCIAL               1
    BANCO DO NORDESTE DO BRASIL                     1
    COMP DOCAS DO ESTADO DO RIO DE JANEIRO          1
    GOVERNO DO ESTADO DE PERNAMBUCO - PE            1
    FINANCIADORA DE ESTUDOS E PROJETOS              1
    CENTRAIS ELETRICAS NORTE BRASIL                 1
    Name: ORG_EXERCICIO, Length: 333, dtype: int64




```python
df['TIPO_VINCULO'].value_counts()
```




    2    630757
    1    104753
    3     50188
    Name: TIPO_VINCULO, dtype: int64




```python
df['SITUACAO_VINCULO'].value_counts()
```




    ATIVO PERMANENTE        572212
    CELETISTA/EMPREGADO      71710
    CEDIDO SUS/LEI 8270      39764
    SEM VINCULO              33630
    CONT.PROF.SUBSTITUTO     11676
    CEDIDO                   11294
    CONTRATO TEMPORARIO      11164
    REQUISITADO               7635
    NOMEADO CARGO COMIS.      6904
    EXERC DESCENT CARREI      3776
    CLT ANS -DEC 6657/08      3638
    EXERC..7º ART93 8112      3442
    APOSENTADO                3306
    REQ.DE OUTROS ORGAOS      2141
    EXERCICIO PROVISORIO       722
    EXCEDENTE A LOTACAO        638
    CONT.PROF.TEMPORARIO       438
    CONTR.PROF.VISITANTE       375
    QUADRO ESPEC.-QE/MRE       242
    COLAB PCCTAE E MAGIS       230
    EMPREGO PUBLICO            180
    REQUIS. MILITAR GDF        105
    CELETISTA                  101
    APRENDIZ                    85
    COLABORADOR ICT             59
    REQ. MILITAR F. ARM         45
    NATUREZA ESPECIAL           34
    CLT ANS DEC JUDICIAL        32
    EXCEDENTE A LOT/MRE         24
    CELETISTA DEC.JUDIC.        20
    ATIVO - DEC. JUDIC          17
    CDT PROF/TUT.MMEDICO        16
    ANISTIADO ADCT CF           12
    TABELISTA(ESP/EMERG)         9
    CLT ANS JUD. CEDIDO          9
    QE/MRE - CEDIDO              6
    CONTR.TEMPORARIO CLT         4
    APOSENTADO TCU733/94         2
    ESTAGIARIO EMPRESA           1
    Name: SITUACAO_VINCULO, dtype: int64




```python
df['REGIME_JURIDICO'].value_counts()
```




    REGIME JURIDICO UNICO                643247
    CONSOLIDACAO DAS LEIS DO TRABALHO     84420
    CONTRATO TEMPORARIO                   23669
    MEDICO RESIDENTE                      18894
    RESIDENCIA MULTIPROFISSIONAL           9291
    MEDICO - PROGRAMA MAIS MEDICO          4820
    REGIME MILITAR                          947
    NATUREZA ESPECIAL                       409
    ESTAGIO EMPRESA                           1
    Name: REGIME_JURIDICO, dtype: int64




```python
df['JORNADA_DE_TRABALHO'].value_counts()
```




    40 HORAS SEMANAIS      565251
    DEDICACAO EXCLUSIVA    137146
    60 HORAS SEMANAIS       22061
    20 HORAS SEMANAIS       20940
    36 HORAS SEMANAIS       15750
    24 HORAS SEMANAIS        8034
    30 HORAS SEMANAIS        7724
    44 HORAS SEMANAIS        7048
    25 HORAS SEMANAIS        1246
    66 HORAS SEMANAIS         412
    12 HORAS SEMANAIS          80
    18 HORAS SEMANAIS           3
    Inválido                    2
    32,5 HORAS SEMANAIS         1
    Name: JORNADA_DE_TRABALHO, dtype: int64




```python
df['DATA_INGRESSO_ORGAO'].value_counts()
```




    29/12/2008    24097
    29/06/2010    12798
    01/03/2016    10008
    02/03/2015     7877
    03/09/2014     4970
    06/07/1978     4876
    02/05/2007     4704
    04/05/2004     4367
    01/07/2010     4010
    11/12/1990     3913
    17/04/1991     3763
    05/01/2016     2275
    10/04/1987     2048
    02/07/2002     1854
    01/12/2016     1847
    06/03/2014     1750
    30/12/2009     1687
    28/06/2006     1684
    03/11/2014     1554
    16/10/2009     1454
    11/05/1994     1426
    10/04/2002     1398
    28/08/2007     1323
    26/05/2008     1321
    01/04/2015     1296
    31/12/2009     1219
    10/04/2013     1210
    19/10/2016     1168
    08/08/2012     1148
    03/08/2015     1134
                  ...  
    05/01/1974        1
    30/01/1983        1
    07/01/1978        1
    09/03/2003        1
    30/08/2015        1
    06/07/1972        1
    23/11/1972        1
    27/01/1971        1
    07/09/1989        1
    20/04/2008        1
    03/03/2007        1
    02/07/1989        1
    06/12/1973        1
    07/01/1970        1
    29/12/1974        1
    16/11/1985        1
    04/08/1991        1
    26/12/1981        1
    23/04/1988        1
    31/03/1991        1
    11/05/1970        1
    12/06/1977        1
    17/09/1977        1
    19/06/1968        1
    23/04/1971        1
    05/07/1987        1
    08/09/1971        1
    25/12/1983        1
    03/07/2016        1
    18/06/2011        1
    Name: DATA_INGRESSO_ORGAO, Length: 13762, dtype: int64




```python
df['DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO'].value_counts()
```




    01/03/2016    12017
    02/03/2015     8605
    04/10/1988     5183
    01/12/2014     5089
    06/03/2014     1978
    01/12/2016     1796
    29/06/2006     1722
    01/09/1981     1705
    01/06/1982     1554
    01/03/2015     1462
    03/11/2014     1371
    01/03/1985     1344
    21/12/1981     1319
    02/01/1989     1294
    01/10/2014     1196
    01/10/1981     1189
    01/07/2010     1165
    01/04/2015     1152
    01/10/1987     1131
    01/09/2015     1088
    01/09/2014     1066
    02/01/1995     1062
    03/08/2015     1047
    02/01/1985     1031
    04/08/2014     1008
    01/02/2010      939
    01/07/1987      939
    01/02/2016      908
    01/09/1987      882
    01/02/1995      881
                  ...  
    14/09/1996        1
    05/10/1968        1
    16/02/2003        1
    10/11/1970        1
    12/10/1967        1
    11/09/1982        1
    12/04/1979        1
    20/04/1986        1
    01/01/2000        1
    14/01/1970        1
    23/03/2014        1
    23/05/1968        1
    26/08/1971        1
    15/07/1966        1
    07/05/2011        1
    08/07/1968        1
    25/08/1969        1
    16/02/2008        1
    26/04/2001        1
    20/12/1999        1
    08/03/2000        1
    19/12/2015        1
    31/03/1994        1
    18/08/1979        1
    05/10/1986        1
    15/06/1967        1
    10/11/2002        1
    10/12/1978        1
    20/11/2011        1
    29/04/1970        1
    Name: DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO, Length: 13905, dtype: int64




```python
df['DIPLOMA_INGRESSO_ORGAO'].value_counts()
```




    PORTARIA                530199
    CONTRATO                124810
    LEI                      69305
    DECRETO                  12274
    OFICIO                    7073
    DECRETO-LEI               7065
    CARTA                     5882
    PROCESSO                  5748
    MEMORANDO                 4625
    OUTROS                    3012
    EDITAL                    2696
    Inválido                  2451
    EXP. MOTIVOS              2187
    ATO                       1939
    MEDIDA PROVISORIA         1503
    PAPELETA                  1115
    BOLETIM INTERNO           1078
    DECISAO JUDICIAL           917
    ORDEM DE SERVICO           706
    TELEX                      297
    INSTRUCAO NORMATIVA        191
    PARECER                    141
    CERTIDAO                   117
    DESPACHO                    87
    DECRETO-LEGISLATIVO         71
    ATA                         44
    APOSTILA                    44
    RESOLUCAO                   40
    AVISO                       32
    RELATORIO                    7
    AçãO CIVIL                   6
    LEI COMPLEMENTAR             5
    REQUERIMENTO                 5
    NORMA COMPLEMENTAR           5
    OFICIO CIRCULAR              4
    EMEND CONSTITUCIONAL         4
    TERMO DE OPCAO               3
    CONSTITUICAO FEDERAL         3
    DEC.ADMINIST. MARE           2
    ATO DE CONCESSAO             1
    ATESTADO MEDICO              1
    FORMULARIO                   1
    ATO DO CONGRESSO             1
    NOTA                         1
    Name: DIPLOMA_INGRESSO_ORGAO, dtype: int64




```python
df['DIPLOMA_INGRESSO_SERVICOPUBLICO'].value_counts()
```




    PORTARIA                527687
    CONTRATO                132565
    Inválido                 50194
    LEI                      21556
    PROCESSO                 12965
    DECRETO-LEI               6818
    OFICIO                    6563
    EXP. MOTIVOS              4866
    CARTA                     4810
    MEMORANDO                 3962
    ATO                       2651
    EDITAL                    1916
    BOLETIM INTERNO           1809
    OUTROS                    1717
    DECRETO                   1520
    DECISAO JUDICIAL           759
    ORDEM DE SERVICO           749
    TELEX                      521
    INSTRUCAO NORMATIVA        499
    CERTIDAO                   434
    PAPELETA                   386
    AVISO                      157
    PARECER                    151
    DESPACHO                   106
    DECRETO-LEGISLATIVO         72
    APOSTILA                    55
    MEDIDA PROVISORIA           45
    RESOLUCAO                   44
    REQUERIMENTO                41
    TERMO DE OPCAO              13
    AçãO CIVIL                  12
    RELATORIO                    9
    EMEND CONSTITUCIONAL         8
    CONSTITUICAO FEDERAL         8
    NORMA COMPLEMENTAR           6
    DEC.ADMINIST. MARE           6
    LEI COMPLEMENTAR             5
    ATO DO CONGRESSO             3
    ATO DE CONCESSAO             3
    OFICIO CIRCULAR              2
    ATA                          2
    FORMULARIO                   1
    COMUNICA SIAPE               1
    ATESTADO MEDICO              1
    Name: DIPLOMA_INGRESSO_SERVICOPUBLICO, dtype: int64




```python
df['UF_EXERCICIO'].value_counts()
```




    -1    363883
    RJ     76706
    MG     42051
    DF     34808
    RS     31686
    SP     30197
    BA     17498
    PR     17205
    PE     17103
    PA     13434
    CE     13361
    PB     13027
    RN     10668
    GO     10514
    SC      9760
    ES      8363
    AP      8144
    MA      8117
    AM      7578
    MS      7218
    RO      7051
    PI      6856
    MT      6815
    RR      6727
    AL      5940
    SE      4897
    TO      3466
    AC      2625
    Name: UF_EXERCICIO, dtype: int64


