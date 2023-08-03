""" Calculadora com while """
calculator = True

while calculator:
    numbers_is_digit = False
    # numbers_is_float = numbers_is_digit and

    # So aceita se o numero for um digito.
    while not (numbers_is_digit):
        print("Numbers invalid!! Enter that an number integer.")
        number_1 = input("Enter again the first number (Only integer): ")
        number_2 = input("Enter again the second number (Only integer): ")
        numbers = number_1 + number_2
        numbers_is_digit = numbers.isdigit()

    # Transforma a entrada em um float.
    number_1 = float(number_1)
    number_2 = float(number_2)

    operator = True

    while operator:
        print("Operations:")
        print(" * => multiplication,\n + => sum,\n - => subtraction,\n / => division")
        operation = input("Enter the operation that you want execute: ")

        if operation == "*":
            print("Result", number_1 * number_2)
            operator = False
        elif operation == "+":
            print("Result", number_1 + number_2)
            operator = False
        elif operation == "-":
            print("Result", number_1 - number_2)
            operator = False
        elif operation == "/":
            print(f"Result {number_1 / number_2:.2f}")
            operator = False
        else:
            print("\nOperator invalid! Select only one operator")

    condition = input("Do you want to calculate any more numbers:(y/n) ")
    while condition != "y" and condition != "n":
        print("Enter an value valid (y/n)!!!")
        condition = input("Do you want to calculate any more numbers:(y/n) ")

    if (condition == "n"):
        calculator = False

print("You left the calculater")
