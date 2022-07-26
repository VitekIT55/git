def sort_list(list):
    if not list:
        return []
    maximum = max(list)
    minimum = min(list)
    i = 0
    while i < len(list):
        if i < len(list) and list[i] != maximum and list[i] != minimum:
            i += 1
        if i < len(list) and list[i] == maximum:
            list[i] = minimum
            i += 1
        if i < len(list) and list[i] == minimum:
            list[i] = maximum
            i += 1
    list.append(minimum)
    return list
