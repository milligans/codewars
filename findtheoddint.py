def find_it(seq):
    number_items =len(seq)
    i=0
    dict=[]
    while (i<number_items):
        number_i =seq.count(seq[i])
        dict.append((number_i , seq[i]))
        i+=1
    # print(dict)
    for item in dict:
        # print(item)
        # print(item[0])
        if item[0]%2 !=0:
            # print(item)
            return item[1]


