import pandas as pd
from HelpClass.BalanceTree import AVTree
import csv

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
        self.Address = {}
        self.ReadNum = 0
        self.WriteNum = 0
        self.SumNum = 0

    def getPara(self):
        file = open(self.filename)
        csvfile = csv.reader(file)
        for row in csvfile:
            # IOnums:切分之后
            self.IONums += (int)(row[5])/512
            # io个数
            self.SumNum = self.WriteNum+self.ReadNum
            # 切分之后的地址
            blocks = (int)(row[5])/512
            offset = (int)(row[4])
            for i in range(int(blocks)):
                if offset+i*512 in self.AddressAccessNum.keys():
                    self.AddressAccessNum[offset+i*512] += 1
                else:
                    self.AddressAccessNum[offset+i*512] = 1
            # SliceTrace
            for k in range(int(int(row[5])/512)):
                self.SliceTrace.append(int(row[4])+k*512)

    def getSliceTrace(self):
        file = open(self.filename)
        csvfile = csv.reader(file)
        for row in csvfile:
            for k in range(int(int(row[5])/512)):
                self.SliceTrace.append(int(row[4])+k*512)

    def NoSliceTrace(self):
        file = open(self.filename)
        csvfile = csv.reader(file)
        for row in csvfile:
            # IOnums:切分之后
            self.IONums += (int)(row[5])/512
            # Address :切分前的地址
            offset = int(row[4])
            self.Address[offset] = 1
            # 读写数
            if(row[3] == "Write"):
                self.WriteNum += 1
            if(row[3] == "Read"):
                self.ReadNum += 1
        self.SumNum = self.WriteNum + self.ReadNum

    def sub_trace_deal(self):
        pass

    def getUniqueAddress(self):
        for key in self.AddressAccessNum:
            if self.AddressAccessNum[key] == 1:
                self.UniqueAddressAccess.append(key)

    def getFrequenceClass(self):
        for key, value in self.AddressAccessNum.items():
            if value in self.FrequenceClass.keys():
                self.FrequenceClass[value] += 1
            else:
                self.FrequenceClass[value] = 1

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
