def selection(data, k):
    if not data:
        return []
    return [i for i in data if i % k == 0]