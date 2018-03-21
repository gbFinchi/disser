import os
import pandas as pd


def csv_from_excel(name):
    xl = pd.ExcelFile(name+".xlsx")
    df = xl.parse('report', skiprows=2)

    df.to_csv(name+'.csv')


def xlx_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.xlsx':
                csv_from_excel(path+'/'+os.path.splitext(file)[0])

xlx_dir('data/mining')
xlx_dir('data/building')

