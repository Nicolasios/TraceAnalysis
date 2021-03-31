import pandas as pd


class Reader:
    def __init__(self):
        pass

    def read(self, filename):
        pd_reader = pd.read_csv(
            filename,
            names=[
                'Timestamp', 'Hostname', 'DiskNumber', 'Type', 'Offset', 'Size', 'ResponseTime'
            ],
            header=None)
        return pd_reader
