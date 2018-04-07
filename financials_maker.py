import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
import math
import collections

currentDate = 2015
dataRaw = pd.read_csv('./data/building.csv')

data = dataRaw.copy(deep=True)
data['Bankrupt'].fillna('0-0-0', inplace=True)
data['Year'] = data['Bankrupt'].str.split('-', expand=True)[0].astype(int)
data.drop(['Bankrupt'], axis =1, inplace=True)
data=data[((data['Year'] >= 2016)&(data['Year']<=2017))|(data['Year']==0)]

mainData = pd.DataFrame()
mainData['Year'] = data['Year']
mainData['Alive'] = 1
mainData['Alive'].loc[mainData['Year'] != 0] = 0
mainData.drop(['Year'], axis = 1, inplace=True)

f = collections.Counter(mainData['Alive'])

ratios = [
    ('NI', 'TA'),
    ('WC', 'TA'),
    ('RE', 'TA'),
    ('EBIT','TA'),
    ('Sales','TA'),
    ('Cash')

]
print(f )

