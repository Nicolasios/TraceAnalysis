from HelpClass.DataReader import *
import time
import matplotlib.pyplot as plt


reader = DataReader("msr-cambridge2/MSR-Cambridge/web_4.csv")
reader.getPara()

reader.getSliceTrace()
