def coincidence(list, range):
    if not list or not range:
        return []
    a = []
    i = 0
    while i < len(list):
        if type(list[i]) == int or type(list[i]) == float:
            if range[0] <= list[i] <= range[-1]:
                a.append(list[i])
        i += 1
    a.sort()
    return a
