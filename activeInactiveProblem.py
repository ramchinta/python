def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    states1 = list(states)

    for j in range(days):
        for i in range(len(states)):
            states.append(0)
            if states[i-1] == 0 and states[i+1] == 0:
                states1[i] = 0
            elif states[i-1] == 1 and states[i+1] == 1:
                states1[i] = 0
            else:
                states1[i] = 1
        states = list(states1)
    return states1
print(cellCompete([1,0,0,0,0,1,0,0],1))

