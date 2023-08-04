import csv


with open('HuaWei_DAG_Data/111.csv', 'r+') as myFile:
    lines = csv.reader(myFile)
    a = list(lines)
    print(a)
    # for line in lines:
    #     print(line)