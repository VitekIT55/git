def max_odd(array):
    chisl = 0
    for i in range(len(array)):
        if type(array[i]) == int or type(array[i]) == float:
            if array[i] / 2 != array[i] // 2:
                schet = i
                if array[i] >= array[schet]:
                    chisl = array[schet]
            if chisl != 0:
                return int(chisl)