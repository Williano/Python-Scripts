"""
  Script: Fibonacci.py
  Description: A scritp to generate fibonacci numbers
  Author: William Kwabla
  Date: 18/02/20

"""

def generate_fibonacci_numbers(first_number, second_number, size_of_fibonacci):
    """
        Generates a list of fibonacci
    """
    list_of_nums = list()

    list_of_nums.append(first_number)
    list_of_nums.append(second_number)

    while len(list_of_nums) < size_of_fibonacci:
        first_previous_number_in_list = list_of_nums[len(list_of_nums) - 1]
        second_previous_number_in_list = list_of_nums[len(list_of_nums) - 2]

        list_of_nums.append(first_previous_number_in_list + second_previous_number_in_list)

    for number in list_of_nums:
        print(number)

def main():
    """
        Main entry point of program.
    """

    first_number = int(input("Enter first number of fibonacci: "))
    second_number = int(input("Enter second of fibonacci: "))
    size_of_fibonacci = int(input("Enter size of fibonacci: "))

    print()

    generate_fibonacci_numbers(first_number, second_number, size_of_fibonacci)

if __name__ == "__main__":
    main()
