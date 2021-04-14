import csv
import time
import pandas as pd

if __name__ == '__main__':
    i = 0
    j = 0
    dic = {}
    t1 = time.time()
    file = open("msr-cambridge2/MSR-Cambridge/src1_0.csv")
    csvfile = csv.reader(file)
    for row in csvfile:
        if i == 1000:
            t2 = time.time()
            print(t2-t1)
        offset = row[4]
        dic[offset] = 1
        i += 1

    t3 = time.time()
    pd_reader = pd.read_csv(
        "msr-cambridge2/MSR-Cambridge/src1_0.csv",
        names=[
            'Timestamp', 'Hostname', 'DiskNumber', 'Type', 'Offset', 'Size', 'ResponseTime'
        ],
        header=None)
    dict = {}
    for row in pd_reader.iterrows():
        if j == 1000:
            t4 = time.time()
            print(t4-t3)
        offset = row[1]['Offset']
        dict[offset] = 1
        j += 1
