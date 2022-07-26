def connect_dicts(dict1, dict2):
    dc1keysum = 0
    dc2keysum = 0
    max1 = max(dict1.values())
    max2 = max(dict2.values())
    dict = {}
    for i in dict1.values():
        dc1keysum += i
    for i in dict2.values():
        dc2keysum += i
    if dc2keysum >= dc1keysum:
        dict.update({k: v for k, v in dict2.items() if v >= 10 and k not in dict.keys()})
        dict.update({k: v for k, v in dict1.items() if v >= 10 and k not in dict.keys()})
    else:
        dict.update({k: v for k, v in dict1.items() if v >= 10 and k not in dict.keys()})
        dict.update({k: v for k, v in dict2.items() if v >= 10 and k not in dict.keys()})

    sorted_values = sorted(dict.values())
    sort_dict = {}
    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sort_dict[k] = dict[k]
                break
    return sort_dict