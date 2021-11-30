def find_outlier(integers):
    test_set=[]
    # setting counters ready
    i=0
    j=0
    # we do a test on the minimum set of numbers, and set the flag accordingly allowing
    # for the special case that the rogue number may lie in the first 3 numbers
    for item in range(0,3):
        if integers[item]%2==0:
            test_set.append(integers[item])
            # print(test_set)
    if len(test_set)==3:
        flag="even"
    else:
        if len(test_set)==0:
            flag="odd"
        else:
            # we know the rogue number must lie in the first 3 so we do a test to see which is greater
            # the number of odd or even - if odd is greater then the rogue must be even and vice versa
            # the flag is set accordingly
            for num in integers[0:3]:
                if num%2==0:
                    i+=1

                else:
                    j+=1

            if i<j:
                flag="odd"
            else:
                flag="even"
    # now that the nature of the outlier has been established we can conduct a test to find it
    # as there is only one outlier the loop can finish when it has been located
    if flag=="even":
        for num in integers:
            if num%2 == 0:
                continue
            else:
                return num
    if flag =="odd":
        for num in integers:
            if num%2!=0:
                continue
            else:
                return num

