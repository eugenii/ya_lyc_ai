def groundhog_day(data):
    template = data[0]
    res = []
    for line in data[1:]:
        res.append(data.index(line))
        for i in range(len(template)):
            if template[i] != line[i]:
                res.append(i)
        if len(res) > 3:
            return tuple(res)
        res.clear()
        template = line
    return (0, 0)


data = ["Groundhog Festival in Punxsutawney.",
        "Groundhog Festival in Punksutawney.",
        "Groundhog Festivel in Punxsutowney."]
print(groundhog_day(data))