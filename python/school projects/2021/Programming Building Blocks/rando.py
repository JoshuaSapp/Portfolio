first_number = float(input("What is the first number?"))
second_number = float(input("What is the Second number?"))

if first_number > second_number:
    print("the first number is greater then the second number")
else:
    print("the first number is not greater then the second number")

if first_number == second_number:
    print("the numbers are equal")
else:
    print("the numbers are not equal")

if first_number < second_number:
    print("the first number is less then the second number")
else:
    print("The first number is not less then the second number")

print()

my_favorite_animal = 'Penguin'

input_animal = input("what is your favorite animal?")
input_animal = input_animal.capitalize()

if my_favorite_animal == input_animal:
    print("Thats my favorite animal too!")
else:
    print("that is not my favorite animal")