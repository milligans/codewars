def similar_license_plates(plate1: str, plate2: str) -> bool:
    # put the similar characters into arrays so that they can be checked for the corresponding characters in the plates
    ohs=["0", "O", "Q"]
    ones=["1", "I", "T"]
    twos=["2", "Z"]
    eights=["8", "B"]
    esses = ["5", "S"]
    # first strip the strings of spaces by replacing space with ""
    plate1=plate1.replace(" ","")
    plate2=plate2.replace(" ","")
    # get the length of the plates for the range calc later
    plate1len = len(plate1)
    plate2len = len(plate2)

    # print(plate1, plate2) sanity check
    # find the shortest plate length - should be the same but just in case they're not
    # we want to compare the shortest one so that we don't get a range error
    if plate2len>=plate1len:
        rangelen=plate1len
    else:
        rangelen=plate2len

    for item in range(0, rangelen):
        print(item, " top of the loop ")
        print(plate1[item], " top of the loop")
        if plate1[item] == plate2[item]:
            print(plate1[item])

        if plate1[item]!= plate2[item]:
            if plate1[item] in ohs:
                if plate2[item] in ohs:
                    print("ohs")
                    continue
                else:
                    return False
            if plate1[item] in ones:
                if plate2[item] in ones:
                    print("ones")
                    continue
                else:
                    return False

            if plate1[item] in twos:
                if plate2[item] in twos:
                    print("twos")
                    continue
                else:
                    return False

            if plate1[item] in eights:
                if plate2[item] in eights:
                    print("eights")
                    continue
                else:
                    return False
            if plate1[item] in esses:
                if plate2[item] in esses:
                    print("esses")
                    continue
                else:
                    return False
            else:
                # plate1[item]!=plate2[item]:
                return False

    return True