def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    GCD = min(arr)
    count = 0
    for i in range(GCD,0,-1):
        print(i)
        for j in arr:
            print(j)
            if j%i != 0:
                count = 0
                print('abc')
                break
            count = count + 1
        print('count ' + str(count))
        if count == num:
            return i

print(generalizedGCD(5,[2,3,4,5,6]))
