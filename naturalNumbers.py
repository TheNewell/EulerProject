
def mulThreeAndFives():
    totalSum = counter = 0
    while counter < 1000:
        if counter % 3 == 0 or counter % 5 == 0:
            totalSum += counter
            #print(counter)
        counter += 1
    #print('From naturalNumber: {}'.format(totalSum))
    return totalSum

