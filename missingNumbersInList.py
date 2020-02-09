def missing(lst):
    lst = sorted(lst)
    return (set(range(lst[0],lst[-1]))-set(lst))

lst = [5,2,3,9,1,6,8,4]
print(missing(lst))

