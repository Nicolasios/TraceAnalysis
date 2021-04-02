import pandas as pd


class DataReader():

    def __init__(self, filename):
        self.filename = filename
        self.pd_reader = None
        self.IONums = 0
        self.AddressAccessNum = {}
        self.UniqueAddressAccess = []

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

    def TimeDistance():
        pass

    def ReuseDistance():
        pass
