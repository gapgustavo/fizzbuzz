# Importing functions from fizzbuzz_functions.py
from fizzbuzz_functions import fizz_buzz

# Main function
def main():
    # Asking the user to enter a natural number
    number = int(input("Digite um número natural: "))
    
    # Calling the fizz_buzz function to check if the number is a multiple of 5, 7 or both
    result = fizz_buzz(number)
    
    #Printing the result
    print(result)
    
# Calling the main function
if __name__ == "__main__":
    main()