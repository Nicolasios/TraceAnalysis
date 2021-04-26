from HelpClass.DataReader import *
from HelpClass.TwoQueue import *
import time
import matplotlib.pyplot as plt


reader = DataReader("msr-cambridge2/MSR-Cambridge/rsrch_0.csv")
reader.getSliceTrace()
print(len(reader.SliceTrace))
TwoQ = TwoQueue(reader.SliceTrace)
cacheSize = 10000000000
blockSize = 100000000
print(TwoQ.getMissRate(cacheSize, blockSize))
