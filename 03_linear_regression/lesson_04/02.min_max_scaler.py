# 02 Ручной MinMaxScaler


class MinMaxScaler:
    def __init__(self, data=None):
        self.data = data

    def transform(self, data):
        trans_data = [(i - min(data)) / (max(data) - min(data)) for i in data]
        return trans_data


data = [float(i) for i in input().split()]
scaler = MinMaxScaler()
scaled = scaler.transform(data)
res = []
for i in scaled:
    res.append("{:.4f}".format(i))
print(" ".join(res))

assert " ".join(res) == "0.8000 1.0000 0.2000 0.0000 0.0000 0.8000 0.2000 0.2000 0.8000 0.6000"
# 4 5 1 0 0 4 1 1 4 3

# 0.8000 1.0000 0.2000 0.0000 0.0000 0.8000 0.2000 0.2000 0.8000 0.6000