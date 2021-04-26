from HelpClass.DataReader import *
from HelpClass.TwoQueue import *
import time
import matplotlib.pyplot as plt

OneM = 512
MaxCacheSize = 1000
blockSize = 512000000

reader = DataReader("msr-cambridge2/MSR-Cambridge/rsrch_0.csv")
reader.getSliceTrace()
print(len(reader.SliceTrace))
TwoQ = TwoQueue(reader.SliceTrace)

missrate = []
for cacheSize in range(1000, 10000000, 200000):
    t1 = time.time()
    miss, hit = TwoQ.getMissRate(cacheSize * OneM, blockSize)
    t2 = time.time()
    print(t2-t1)
    missrate.append(miss/(miss+hit))

x_list = range(1000, 10000000, 200000)
y_list = missrate
# 创建图并命名
plt.figure('Line fig')
ax = plt.gca()
# 设置x轴、y轴名称
ax.set_xlabel('x')
ax.set_ylabel('y')

# 画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
# 参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
ax.plot(x_list, y_list, color='r', linewidth=1, alpha=0.6)

plt.show()
