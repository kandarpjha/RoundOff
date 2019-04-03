calc_tax = int(input(">"))  # Gets user input as an integer only amount

if calc_tax % 10 == 0:      # If the input integer is a number rounded off to 10, then simply prints the number
    print(calc_tax)
elif calc_tax % 10 < 5:     # If the number at unit place of the input is less than 5, then keeps reducing the number
                            # till the input reaches to the nearest previous 10s rounded number zero.
    while calc_tax % 10 != 0:
        calc_tax = int(calc_tax) - 1
    print(calc_tax)
else:                       # If the unit figure of the number is equal to or more than 5, then keeps incrementing
                            # the number by 1 till it reaches the next 10s rounded number.
    while calc_tax % 10 != 0:
        calc_tax = int(calc_tax) + 1
    print(calc_tax)
