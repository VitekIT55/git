def is_palindrome(string):
    string = str(string)
    import re
    string = string.lower()
    string = re.split(r'\W+', string)
    line = ''
    rev = ''
    a = []
    for i in range(len(string)):
        line += string[i]
    for i in range(len(string)-1, -1, -1):
        a = string[i]
        for i1 in range(len(a)-1, -1, -1):
            rev += a[i1]
    return rev == line