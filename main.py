from HelpClass.DataReader import *

reader = DataReader("msr-cambridge2/MSR-Cambridge/web_4.csv")
reader.read()
reader.getSliceTrace()
print(reader.getTimeDistance())
