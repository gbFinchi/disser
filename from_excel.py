import pandas as pd
xl = pd.ExcelFile("./data/mining/mining_2008.xlsx")
print(xl.sheet_names)
df = xl.parse('report', skiprows=2)

temp_df = pd.DataFrame([])

for i in df['Наименование']:
    temp_df[i] = []

for index, item in enumerate(df["Наименование"]):
    for vals in df:
        if vals != 'Наименование':
            temp_df[item][vals] = df[vals][index];

temp_df.to_csv('mining.csv')



