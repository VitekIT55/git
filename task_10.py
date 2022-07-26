def count_words(string):
    import re
    text = string.lower()
    text = re.split(r'\W+', text)
    dictionary = dict()
    for word in text:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary