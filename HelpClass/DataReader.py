import pandas as pd


class DataReader():

    def __init__(self, filename):
        self.filename = filename
        self.pd_reader = None
        self.IONums = 0
        self.AddressAccessNum = {}
        self.UniqueAddressAccess = []
        self.FrequenceClass = {}
        self.SliceTrace = []

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

    def TimeDistance(self):
        pass

    def ReuseDistance(self):
        pass


'''
a b c a c b 
'''
