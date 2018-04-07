import os
import pandas as pd
import collections


def csv_from_excel(name):
    xl = pd.ExcelFile(name+".xlsx")

    df = xl.parse('report', skiprows=2)
    #data = df.copy(deep=True)
    df.to_csv(name + '.csv')
    dataRaw = pd.read_csv(name+'.csv')
    data = dataRaw.copy(deep=True)
    data['Дата ликвидации'].fillna('0-0-0', inplace=True)
    data['Year'] = data['Дата ликвидации'].str.split('-', expand=True)[0].astype(int)
    f = collections.Counter(data['Статус'])
    print(name,' ',f)
    df.to_csv(name+'.csv')


def xlx_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.xlsx':
                csv_from_excel(path+'/'+os.path.splitext(file)[0])

xlx_dir('./data/mining')
xlx_dir('./data/building')

