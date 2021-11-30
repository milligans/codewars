def get_sum(a,b):
    tots = 0
    if a==b:
        return a
    if a>b:
        for num in range(b, a+1):
            # print('the number is ', num)
            tots = tots + num

    if a<b:
        for num in range(a, b+1):
            # print('the number is ' , num)
            tots = tots + num


    return tots