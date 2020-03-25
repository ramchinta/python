def fun(inputList):
    for input in inputList:
        input = input[:len(input)-4]
        temp = input.split('_')
        out = ''
        for i in temp:
            if i.isdigit():
                print(out)
                break
            out = out + i +'_'

(fun(['abc_def_ghi_123.txt','abc_345.txt','abc_576.txt']))

