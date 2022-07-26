def multiply_numbers(inputs):
    inputs = list(str(inputs))
    inputsfix = []
    for i in range(len(inputs)):
        try:
            inputsfix.append(int(inputs[i]))
        except ValueError:
            continue
    otvet = 1
    schet = 0
    for i in range(len(inputsfix)):
            otvet *= inputsfix[i]
            schet += 1
    if schet > 0:
        return otvet