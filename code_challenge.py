def withdraw(amount: int) -> list:
    # setting up variables
    money_array=[0, 0, 0]
    hundreds=0
    fifties=0
    twenties=0

    # invalid amounts
    if amount <20 or amount%10!=0:
        return("invalid amount")


    # first work out the twenties
    if amount%20!=0:
        # the amount must require a 50 to make it
        # there will only ever be one 50 maximum or it will become a hundred
        fifties =1
        amount=amount - 50
        hundreds = amount//100
        twenties = int((amount - (100*hundreds))/20)

    if amount%20 ==0:
        hundreds=amount//100
        twenties = int((amount - (100*hundreds))/20)

    money_array = [hundreds, fifties, twenties]

    return money_array