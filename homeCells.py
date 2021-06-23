def cellCompete(states, days):
    currentStates = states

    neighL = neighR = 0
    for x in range(days):
        newStates = [0, 0, 0, 0, 0, 0, 0, 0]
        for y in range(len(currentStates)):
            #3print('y = {}'.format(y))
            if y == 0:
                #print('if')
                neighL = 0
                neighR = currentStates[y+1]
            elif y == 7:
                #print('elif')
                neighL = currentStates[y-1]
                neighR = 0
            else:
                #print('else')
                #print(currentStates)
                neighL = currentStates[y-1]
                neighR = currentStates[y+1]
            #print('Current state: {}'.format(currentStates[y]))
            #print('neighL: {} neighR: {}'.format(neighL, neighR))
            if neighL != neighR:
                newState = 1
            else:
                newState = 0
            #print('New state: {}'.format(newState))
            newStates[y] = newState
        #print('Day: {}'.format(x))
        currentStates = newStates
        #print(currentStates)
    return currentStates
