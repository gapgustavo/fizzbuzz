*FizzBuzz in Python

This is a simple Python script that implements FizzBuzz, a popular programming challenge.

The script uses functions imported from another file called fizzbuzz_functions.py to check if a natural number entered by the user is a multiple of 5, 7 or both, and prints the corresponding output according to the following rules:

If the number is a multiple of 5, print "fizz".
If the number is a multiple of 7, print "buzz".
If the number is a multiple of both 5 and 7, print "fizzbuzz".
Otherwise, it prints "miss".

*Prerequisites

Python 3.x installed on your system. If you don't have Python installed, you can download the latest version from https://www.python.org/downloads/

Virtual environment contained within the "flow" folder, with the folder open you can activate it with the following command:
Scripts/Activate.ps1

*How to run the script

Clone or download this repository in your development environment.

Open a terminal and navigate to the directory where the main.py file is located.

Run the following command to run the script:

python main.py

The script will ask you to enter a natural number.

After entering the number, the script will print the corresponding output according to the FizzBuzz rules.

*Project files

The project consists of the following files:

main.py: The main file that contains the main() function responsible for running the application and calling the functions in the fizzbuzz_functions.py file.

fizzbuzz_functions.py: The file that contains the is_multiple_of_5(), is_multiple_of_7() and fizz_buzz() functions, responsible for checking whether a number is a multiple of 5, 7 or both, and returning the corresponding output according to the FizzBuzz characteristics.

*Contribution

If you want to contribute to this project, feel free to open an issue or submit a pull request. It will be a pleasure to receive contributions to improve the code and make the project more robust.

*License

This project is licensed under the MIT License, which means that you can freely use, modify, distribute and/or market it, as long as you maintain the attribution of credits to the original authors.
