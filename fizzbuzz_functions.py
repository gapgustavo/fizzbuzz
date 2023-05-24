def is_multiple_of_5(number):
    """Function that checks if a number is a multiple of 5."""
    return number % 5 == 0

def is_multiple_of_7(number):
    """Function that checks if a number is a multiple of 7."""
    return number % 7 == 0

def fizz_buzz(number):
    """Main function that checks if a number is a multiple of 5, 7 or both."""
    if is_multiple_of_5(number) and is_multiple_of_7(number):
        return "fizzbuzz"
    elif is_multiple_of_5(number):
        return "fizz"
    elif is_multiple_of_7(number):
        return "buzz"
    else:
        return "miss"