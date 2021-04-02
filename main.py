from HelpClass.DataReader import *

reader = DataReader("msr-cambridge2/MSR-Cambridge/web_4.csv")
reader.read()
# pd_reader = reader.getPdReader()
# ionum = reader.get_IONums()

dic = reader.getAddressAccessNums()
list = reader.getUniqueAddress()
print(dic)
print('------------------------------------------')
print(list)
