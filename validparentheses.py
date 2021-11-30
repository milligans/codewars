def valid_parentheses(string):
    i=0
    # keep track of left brackets
    j=0
    # keep track of right brackets
    if len(string)== 1:
        return False

    else:
        for char in string:
            if char =="(":
                # print("it's a match")
                i=i+1
            if char ==")":
                # print("it's a right match")
                j=j+1
            if j>i:
                return False
    if i==j:
        # print("number of left is number of right")
        return True
    else:
        return False


