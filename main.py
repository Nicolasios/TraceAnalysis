from HelpClass.DataReader import *
import time
import json

filename = "rsrch_0"

reader = DataReader("msr-cambridge2/MSR-Cambridge/"+filename+".csv")
reader.getPara()


with open("output/" + filename + "/"+filename+"_IoNums.txt", 'w') as f:
    f.write(str(reader.IONums))

AddressAccessNums = reader.AddressAccessNum
jsObj = json.dumps(AddressAccessNums, indent=4)
fileObject = open("output/" + filename + "/"+filename+"_AdressNums.json", 'w')
fileObject.write(jsObj)
fileObject.close()  # 最终写入的json文件格式:

reader.getFrequenceClass()
FrequenceClass = reader.FrequenceClass
jsObj = json.dumps(FrequenceClass)
fileObject = open("output/" + filename + "/" +
                  filename+"_FrequenceClass.json", 'w')
fileObject.write(jsObj)
fileObject.close()  # 最终写入的json文件格式:

with open("output/" + filename + "/"+filename+"_UniqueAddress.txt", 'w') as f:
    a = 0
    reader.getUniqueAddress()
    for line in reader.UniqueAddressAccess:
        a += 1
        f.write(str(line)+" ")
        if a == 10:
            a = 0
            f.write("\n")

# with open("output/" + filename + "/"+filename+"_ReuseDistance.txt", 'w') as f:
#     a = 0
#     for line in reader.getReuseDistance():
#         a += 1
#         f.write(str(line)+" ")
#         if a == 10:
#             a = 0
#             f.write("\n")

# with open("output/" + filename + "/"+filename+"_TimeDistance.txt", 'w') as f:
#     a = 0
#     for line in reader.getTimeDistance():
#         a += 1
#         f.write(str(line)+" ")
#         if a == 10:
#             a = 0
#             f.write("\n")
