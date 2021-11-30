def duplicate_count(text):
    build_word=""
    i=0
    j=0

    while j<len(text):
        if text[j].lower() in text[j+1:].lower():
            if text[j].lower() in build_word:
                print('a duplicate of a duplicate ' + text[j])
                pass
            else:
                build_word=text[j].lower()+build_word.lower()

                print("Look lads!" + text[j])
                i=i+1
        j=j+1
    print("number duplicates ", i)
    return i