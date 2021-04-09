from HelpClass.DataReader import *
import time

reader = DataReader("msr-cambridge2/MSR-Cambridge/rsrch_0.csv")
reader.read()
reader.getSliceTrace()

AddressAccessNums = reader.getAddressAccessNums()

# FrequenceClass = reader.getFrequenceClass()

# UniqueAddress = reader.getUniqueAddress()

# IONums = reader.getIONums()

# ReuseDistance = reader.getReuseDistance()

# Time = reader.getTimeDistance()

print("AddressAccessNums")
print(AddressAccessNums)

# print("------------------------------------------------------------")

# print("FrequenceClass")
# print(FrequenceClass)

# print("------------------------------------------------------------")

# print("UniqueAddress")
# print(UniqueAddress)

# print("------------------------------------------------------------")

# print("IONums")
# print(IONums)

# print("------------------------------------------------------------")

# print("ReuseDistance")
# print(ReuseDistance)

# print("------------------------------------------------------------")

# print("Time")
# print(Time)
