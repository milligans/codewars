def toWeirdCase(words):
    # print(words)
    string_length = len(words)
    # print(f"{words} the length of the string is {string_length}")
    i=0
    variable_flag_is_even = False
    converted_words=""
    while i < string_length:
        if ord(words[i]) ==32:
            # print("theres a space here at ", i)
            converted_words = converted_words + words[i]
            if i%2 ==0:

                # print(f"{i} is the index")
                converted_words = converted_words + words[i+1].upper()
                variable_flag_is_even = True
                i+=2
                continue

            else:
                # print(f"{i} is an uneven index")
                variable_flag_is_even = False
                converted_words = converted_words + words[i+1].upper()
                i+=2
                continue



        elif i%2==0 and variable_flag_is_even == False :
            converted_words = converted_words + words[i].upper()
            i+=1
        elif i%2 !=0 and variable_flag_is_even == True:
            converted_words = converted_words + words[i].upper()
            i += 1
        elif i%2 ==0 and variable_flag_is_even == True:
            converted_words = converted_words + words[i].lower()
            i+=1
        elif i%2 !=0 and variable_flag_is_even == False:
            converted_words = converted_words + words[i].lower()
            i+=1
    return converted_words