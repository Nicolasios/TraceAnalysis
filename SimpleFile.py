from HelpClass.DataReader import *

rootname = ["msr-cambridge1/MSR-Cambridge/", "msr-cambridge2/MSR-Cambridge/"]
filename = [
    # rootname[0]+"hm_0.csv",
    # rootname[0]+"hm_1.csv",
    # rootname[0]+"mds_0.csv",
    # rootname[0]+"mds_1.csv",
    # rootname[1]+"rsrch_0.csv",
    # rootname[1]+"rsrch_1.csv",
    # rootname[1]+"rsrch_2.csv",
    # rootname[1]+"src1_0.csv",
    # rootname[1]+"src1_1.csv",
    # rootname[1]+"src1_2.csv",
    # rootname[1]+"src2_0.csv",
    # rootname[1]+"src2_1.csv",
    # rootname[1]+"src2_2.csv",
    rootname[1]+"web_4.csv"
]


if __name__ == '__main__':
    for item in filename:
        reader = DataReader(item)
        reader.read()
        WriteNum, ReadNum = reader.ReaderAndWriteNum()
        Sum = reader.IoNumSum()
        SumSize = reader.getSumSize()
