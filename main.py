from reader.Reader import Reader

a = Reader()
data = a.read("../test.csv")

print(data.head(2))
