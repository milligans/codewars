def maskify(masking: str):
    masked_str = ""
    strLength = len(masking)

    if strLength <= 4:
        # print(masking)
        return masking
    else:
        for num in range(0,strLength-4):
            masked_str = masked_str + "#"
        masked_str = masked_str + masking[-4:]
    # print(masked_str)
    return masked_str