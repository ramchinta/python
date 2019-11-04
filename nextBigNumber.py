def next_num():
    a = input("Enter Number:")
    b = [int(i) for i in str(a)]
    if (sorted(b,reverse=True)) == b:
        print("Can't have bigger number")
    else:
        c = (b[::-1])
        print(c)
        for i in range(len(c)-1):
            print(len(c))
            if c[i] > c[i+1]:
                t = c[i]
                c[i] = c[i+1]
                c[i+1] = t
                break
        out = sum(d * 10 ** i for i, d in enumerate(c))
        print(out)

next_num()

