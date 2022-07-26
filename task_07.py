def combine_anagrams(words_array):
    otvet = []
    for i1 in range(len(words_array)):
        mas1 = sorted(list(words_array[i1]))
        freemas = []
        for i2 in range(len(words_array)):
            mas2 = sorted(list(words_array[i2]))
            if mas1 == mas2:
                freemas.append(words_array[i2])
        if freemas not in otvet:
            otvet.extend([freemas])
    return otvet
