def palindrome():
        temp = 0
        largestPalindrom = 0
        for y in range(100, 1000):
            for x in range(100, 1000):
                temp = y * x
                if isPalindrome(str(temp)) == True:
                    if largestPalindrom < temp:
                        largestPalindrom = temp
        return largestPalindrom


def isPalindrome(number):
    list = []
    validation = None
    for x in number:
        list.append(x)
    length = int(len(list)/2)
    for i in range(int(len(list)/2)):
        var1 = list[i]
        var2 = list[(len(list)-1)-i]
        if var1 == var2:
            validation = True
        else:
            validation = False
            break
    return validation
