import xlrd
import csv
import os



def csv_from_excel(name):
    wb = xlrd.open_workbook(name+'.xlsx')
    sh = wb.sheet_by_name('report')
    your_csv_file = open(name+'.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(2, sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


def xlx_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.xlsx':
                csv_from_excel(path+'/'+os.path.splitext(file)[0])

#xlx_dir('data/добыча полезныз ископаемых')
xlx_dir('data/строительство зданий')
#csv_from_excel('./data/добыча полезныз ископаемых/Добыча полезный ископаемых_2008')