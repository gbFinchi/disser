import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy

import math

current_date = '2014'
bankruptDateTab = 'Дата ликвидации'

data_raw = pd.read_csv('./data/mining_2014.csv')

data = data_raw.copy(deep=True)

data['Дата ликвидации'].fillna('0-0-0', inplace=True)
data['Year'] = data[bankruptDateTab].str.split('-', expand=True)[0].astype(int)
data = data[(data['Year'] == 2015) | (data['Year'] == 0)]
data['Alive'] = 0
data['Alive'].loc[data['Year'] == 0] = 1
data = data[data['Активы'] > 1000000]
data = data[data['Баланс'] == 0]
data = data[(data['Рентабельность активов (ROA)'] >= -0.75) & (data['Рентабельность активов (ROA)'] <= 0.75)]
columns_to_delete = ['Year', bankruptDateTab, 'Активы','Статус', 'Долгосрочные обязательства', 'Капитал и резервы','Чистая прибыль','Баланс','Прибыль до налогообложения','Нераспределенная прибыль','Прибыль от продажи','Краткосрочные обязательства']
data.drop(columns_to_delete, axis=1, inplace=True)
for item in data:
    data[item].fillna(data[item].median(), inplace=True)

Target=['Alive']


def correlation_heatmap(df):
    _, ax = plt.subplots(figsize=(15, 15))
    colormap = sns.diverging_palette(220, 10, as_cmap=True)

    _ = sns.heatmap(
        df.corr(),
        cmap=colormap,
        square=True,
        cbar_kws={'shrink': .9},
        ax=ax,
        annot=True,
        linewidths=0.1, vmax=1.0, linecolor='white',
        annot_kws={'fontsize': 12}
    )

    plt.title('Pearson Correlation of Features', y=1.05, size=15)


#correlation_heatmap(data)

plt.figure(figsize=[16,12])
plt.subplot(231)
plt.boxplot(x=data['Рентабельность активов (ROA)'], showmeans=True, meanline=True)
plt.title('Current liquidity ratio')
plt.ylabel('%')

plt.subplot(234)
plt.hist(x = data['Рентабельность активов (ROA)'], stacked=True, color = 'r', label='Current liquidity ratio')
plt.title('Current liquidity ratio')
#plt.show()

# тест на нормальность
x = data['Рентабельность активов (ROA)']
shapiro_results = scipy.stats.shapiro(x)
print('Shapiro test =',shapiro_results)

test = [data['Alive'], data['Рентабельность активов (ROA)']]
test = data[['Alive','Рентабельность активов (ROA)']].copy()
groups = test.groupby('Alive').groups
alive = data['Рентабельность активов (ROA)'][groups[1]]
dead = data['Рентабельность активов (ROA)'][groups[0]]
result = scipy.stats.f_oneway(alive, dead)
print('ANOVA =', result)
print('Means =', alive.mean(), ', ', dead.mean())
