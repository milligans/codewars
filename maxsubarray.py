def max_sequence(arr):
    cont_arr=[]
    print(arr)
    if not arr:
        return 0
    length_of_array = len(arr)
    for num in range(length_of_array-1):
        if arr[num]<arr[num+1]:
            print(arr[num])
            cont_arr.append(arr[num])

    print(sum(cont_arr))
    return sum(cont_arr)