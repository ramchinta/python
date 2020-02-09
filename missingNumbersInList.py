def missing(lst):
    return (sorted(set(range(lst[0],lst[-1]))-set(lst)))

lst = [1,2,3,4,5,6,8,9]
print(missing(lst))