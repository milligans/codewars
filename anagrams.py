def anagrams(word, words):
    # establish an empty array for any solutions to populate
    ana_array=[]
    # print(word)
    # print(words)
    # making sure it isn't case sensitive
    word=word.lower()

    for item in words:
        test_word=""
        for char in item:
            if char.lower() in word:
                test_word=test_word+char
                # print(test_word)
                # testing if the characters are exactly the same by calculating the sum of the ordinals
                if len(test_word)==len(item) and sum(ord(c)for c in word)==sum(ord(c) for c in test_word):
                    ana_array.append(item)






    return(ana_array)