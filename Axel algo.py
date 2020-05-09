# Write your code here
def fun(a,b):
    out = -1
    for i in range(a[0]):
        if a[1]== b[i]:
            out = i + 1
    print(out)
fun([5,1],[1,2,3,4,1])

#LinearSearch