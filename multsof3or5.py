def solution(number):
    if number <= 0:
        return 0
    i=1
    numset =[]
    while i < number:
        if i%3 ==0 and i%5 ==0:
            numset.append(i)
            i+=1
            continue
        elif i%5 ==0:
            numset.append(i)
            i+=1
        elif i%3 ==0:
            numset.append(i)
            i+=1
        else:
            i+=1
    total =0
    for value in numset:
        total = total + value
    return total