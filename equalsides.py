def find_even_index(arr):
    num=len(arr)
    # print(num)

    for ind in range(num):
        ups=sum(arr[0:ind+1])
        # print(ups)
        downs= sum(arr[ind:num])
        # print(downs)
        if ups==downs:
            # print("yeehaw!")
            return ind
    return -1