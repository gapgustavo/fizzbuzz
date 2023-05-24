from fizzbuzz_functions import is_multiple_of_5, is_multiple_of_7, fizz_buzz

# Test function for is_multiple_of_5()
def test_is_multiple_of_5():
    # Test case 1: number is a multiple of 5
    assert is_multiple_of_5(10) is True
    # Test case 2: number is not a multiple of 5
    assert is_multiple_of_5(7) is False
# Test function for is_multiple_of_7()

def test_is_multiple_of_7():
    # Test case 1: number is a multiple of 7
    assert is_multiple_of_7(21) is True
    # Test case 2: number is not a multiple of 7
    assert is_multiple_of_7(10) is False
# Test function for fizz_buzz()

def test_fizz_buzz():
    # Test case 1: number is a multiple of 5 and 7
    assert fizz_buzz(35) == "fizzbuzz"
    # Test case 2: number is only a multiple of 5
    assert fizz_buzz(25) == "fizz"
    # Test case 3: number is only a multiple of 7
    assert fizz_buzz(77) == "buzz"
    # Test case 4: number is not a multiple of 5 or 7
    assert fizz_buzz(16) == "miss"

#TO RUN THE TEST YOU NEED TO USE THIS: python -m pytest test_fizzbuzz_functions.py
