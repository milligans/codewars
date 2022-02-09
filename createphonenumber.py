def create_phone_number(n):
    phone_num="("
    length_of_num =len(n)
    if length_of_num != 10:
        print("invalid")
        return ("invalid number")
    i =0
    while i< len(n) :

        if i ==3:
            phone_num = phone_num + ") " + str(n[i])
            i+=1
        elif i ==6:
            phone_num = phone_num+ "-"  + str(n[i])
            i +=1
        else:
            phone_num = phone_num + str(n[i])
            i+=1

    return phone_num


