def duplicate_encode(word):
    word = word.lower()
    encoded=""

    for char in word:
        count = word.count(char)
        if count>1:
            print("Yeah! there is a duplicate of " + char)
            encoded = encoded + ")"
        else:
            encoded = encoded + "("
    return encoded

