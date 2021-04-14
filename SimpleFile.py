from HelpClass.DataReader import *
import pandas as pd
import time

rootname = ["msr-cambridge1/MSR-Cambridge/", "msr-cambridge2/MSR-Cambridge/"]
filename = [
    # rootname[0]+"hm_0.csv",
    # rootname[0]+"hm_1.csv",
    # rootname[0]+"mds_0.csv",
    # rootname[0]+"mds_1.csv",
    rootname[1]+"src1_0.csv",
    rootname[1]+"src1_1.csv",
    # rootname[1]+"src1_2.csv",
    # rootname[1]+"src2_0.csv",
    # rootname[1]+"src2_1.csv",
    # rootname[1]+"src2_2.csv",
    # rootname[1]+"rsrch_0.csv",
    # rootname[1]+"rsrch_1.csv",
    # rootname[1]+"rsrch_2.csv",
    # rootname[1]+"web_4.csv"
]


if __name__ == '__main__':
    # TraceList = ['hm_0', 'hm_1',
    #              'mds_0', 'mds_1',
    #              'src1_2', 'src2_0', 'src2_1', 'src2_2',
    #              'rsrch_0', 'rsrch_1', 'rsrch_2']
    TraceList = ['src1_0', 'src1_1']
    SumIONumList = []
    ReadNumList = []
    WriteNumList = []
    ReadRateList = []
    AverageSizeList = []
    MaxAddressList = []
    MinAddressList = []
    t3 = time.time()
    for item in filename:
        print("begin:"+item)
        t1 = time.time()
        reader = DataReader(item)
        reader.read()
        print("read ok")
        address = reader.getAddress()
        print("address ok")
        WriteNum, ReadNum = reader.ReaderAndWriteNum()
        SumIONum = reader.IoNumSum()
        ReadRate = ReadNum/SumIONum
        AverageSize = reader.getIONums()/SumIONum
        MaxAddress = max(address)
        MinAddress = min(address)
        SumIONumList.append(SumIONum)
        ReadNumList.append(ReadNum)
        WriteNumList.append(WriteNum)
        ReadRateList.append(ReadRate)
        AverageSizeList.append(AverageSize)
        MaxAddressList.append(MaxAddress)
        MinAddressList.append(MinAddress)
        t2 = time.time()
        print(t2-t1)
        print(SumIONum, ReadNum, WriteNum, ReadRate,
              AverageSize, MaxAddress, MinAddress)
    t4 = time.time()
    print(t4-t3)
    df = pd.DataFrame({
        'Trace': TraceList,
        'SumIONum': SumIONumList,
        'ReadNum': ReadNumList,
        'WriteNum': WriteNumList,
        'ReadNum': ReadNumList,
        'ReadRate': ReadRateList,
        'AverafeSize': AverageSizeList,
        'MaxAddress': MaxAddressList,
        'MinAddress': MinAddressList
    })
    df.to_csv("source/SimpleFile.csv", index=False)
