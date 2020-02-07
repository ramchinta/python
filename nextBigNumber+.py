def num():
    number = int(input("Enter Number:"))
    number = [i for i in str(number)]
    n = len(number)

    for i in range(n-1,0,-1):
        if number[i] > number[i-1]:
            break
    if i == 0 :
        print("No bigger number is possible")
        return

    x = number[i-1]
    smallest = i
    for j in range (i+1,n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j

    number[smallest],number[i-1]=number[i-1],number[smallest]

    y = 0
    for j in range(i):
        y = y * 10 + int(number[j])

    number = sorted(number[i:])

    for j in range(n-i):
        y = y * 10 + int(number[j])

    print("Next biggest number is: "+str(y))









num()