def square_digits(num):
    numstring = str(num)
    squared_string=""

    for char in numstring:
        squared = str(pow(int(char), 2))
        squared_string = squared_string + squared

    return int(squared_string)