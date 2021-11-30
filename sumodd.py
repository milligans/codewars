def row_sum_odd_numbers(n):
    tot=0
    secondtot=0
    flop=1
    row_num=0
    # first work out the number of items in the row that are produced for n
    for num in range(1, n+1):
        # print(num)
        tot = num + tot
        # print(tot , " is the total number of iterations to get to row ", num)
    for num in range(1, n):
        secondtot = num + secondtot
        # print(secondtot, ' is the total number of iterations to get to row', num)

    if n==1:
        return flop

    # so we need the number of odd numbers between these two tot and secondtot
    for num in range(secondtot +1, tot+1):
        row_num = ((num *2)-1) + row_num

    return row_num


