import pandas as pd
from HelpClass.BalanceTree import AVTree

MAX = 0


class DataReader():

    def __init__(self, filename):
        self.filename = filename
        self.pd_reader = None
        self.IONums = 0
        self.AddressAccessNum = {}
        self.UniqueAddressAccess = []
        self.FrequenceClass = {}
        self.SliceTrace = []
        self.TimeDistance = []
        self.ReuseDistance = []
        self.ReadNum = 0
        self.WriteNum = 0
        self.SumNum = 0

    def read(self):
        self.pd_reader = pd.read_csv(
            self.filename,
            names=[
                'Timestamp', 'Hostname', 'DiskNumber', 'Type', 'Offset', 'Size', 'ResponseTime'
            ],
            header=None)

    def getPdReader(self):
        return self.pd_reader

    def sub_trace_deal(self):
        pass

    def getIONums(self):
        for row in self.pd_reader.iterrows():
            self.IONums += row[1]['Size']/512
        return self.IONums

    def getAddress(self):
        dict = {}
        for row in self.pd_reader.iterrows():
            offset = row[1]['Offset']
            dict[offset] = 1
        return dict

    def getAddressAccessNums(self):
        for row in self.pd_reader.iterrows():
            blocks = row[1]['Size']/512
            offset = row[1]['Offset']
            for i in range(int(blocks)):
                if offset+i*512 in self.AddressAccessNum.keys():
                    self.AddressAccessNum[offset+i*512] += 1
                else:
                    self.AddressAccessNum[offset+i*512] = 1
        return self.AddressAccessNum

    def getUniqueAddress(self):
        for key in self.AddressAccessNum:
            if self.AddressAccessNum[key] == 1:
                self.UniqueAddressAccess.append(key)
        return self.UniqueAddressAccess

    def getFrequenceClass(self):
        for key, value in self.AddressAccessNum.items():
            if value in self.FrequenceClass.keys():
                self.FrequenceClass[value] += 1
            else:
                self.FrequenceClass[value] = 1
        return self.FrequenceClass

    def getSliceTrace(self):
        SliceTrace = self.pd_reader['Offset'].values.tolist()
        TraceSize = self.pd_reader['Size'].values.tolist()
        size = len(TraceSize)
        for i in range(size):
            for k in range(int(TraceSize[i]/521)):
                self.SliceTrace.append(SliceTrace[i]+k*512)
        return self.SliceTrace

    def getTimeDistance(self):
        AppearIndex = {}
        for i in range(len(self.SliceTrace)):
            if self.SliceTrace[i] in AppearIndex.keys():
                self.TimeDistance.append(i-AppearIndex[self.SliceTrace[i]])
                AppearIndex[self.SliceTrace[i]] = i
            else:
                self.TimeDistance.append(MAX)
                AppearIndex[self.SliceTrace[i]] = i
        return self.TimeDistance

    def getReuseDistance(self):
        Hashmap = {}
        tree = AVTree()
        AppearIndex = {}
        for i in range(len(self.SliceTrace)):
            if self.SliceTrace[i] in AppearIndex.keys():
                self.ReuseDistance.append(
                    self.distance(tree, AppearIndex[self.SliceTrace[i]]))
                tree.removeFromTree(AppearIndex[self.SliceTrace[i]])
                tree.addToTree(i, self.SliceTrace[i])
                AppearIndex[self.SliceTrace[i]] = i
            else:
                tree.addToTree(i, self.SliceTrace[i])
                self.ReuseDistance.append(MAX)
                AppearIndex[self.SliceTrace[i]] = i
        return self.ReuseDistance

    def distance(self, tree, timestamp):
        temp = tree.root
        d = 0
        while temp is not None:
            if temp.key < timestamp:
                temp = temp.right
            elif temp.key > timestamp:
                d += 1
                if temp.right:
                    d += tree.getWeight(temp.right)
                temp = temp.left
            else:
                d += tree.getWeight(temp.right)
                return d + 1

    def ReaderAndWriteNum(self):
        for row in self.pd_reader.iterrows():
            if(row[1]['Type'] == "Write"):
                self.WriteNum += 1
            if(row[1]['Type'] == "Read"):
                self.ReadNum += 1
        return (self.WriteNum, self.ReadNum)

    def IoNumSum(self):
        self.SumNum = self.WriteNum + self.ReadNum
        return self.SumNum
