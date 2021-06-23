def checkEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def fibonacciNum():
    n1 = 1
    n2 = total = 2
    temp = 0
    valuesList = []
    while temp < 4000000:
        # print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        if checkEven(temp) is True and temp < 4000000:
            total += temp
            # print("Total = {}".format(total))
            valuesList.append(temp)
    # print(valuesList)
    return total


