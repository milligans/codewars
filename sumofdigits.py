def digital_root(n):

    strnum = str(n)
    arraynums=[]
    if len(strnum)==1:
        return int(strnum)

    while len(strnum)>1:
        for char in strnum:
            arraynums.append(int(char))
            # print(arraynums)
            strnum = str(sum(arraynums))
            # print(strnum)
        arraynums=[]

    return int(strnum)












