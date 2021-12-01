X = 7
Y = 3

if X > Y:
    print("BIG")
elif X == Y:
    print("equals")
else:
    print("small")

for i in range(5):
    print(i)

var = 3
if var == 1:
    print("summer season")
elif var == 2:
    print("winter season")
elif var == 3:
    print("fall season")
elif var == 4:
    print("spring season")

count = 1
while count < 11:
    print(count)
    count = count + 1

age = 29
first_letter = "I"
current_shekel_dollar_currency = 3.18
is_flew = True
apartment_number = 13
print(age)
print(first_letter)
print(current_shekel_dollar_currency)
print(is_flew)
print(apartment_number)
print(current_shekel_dollar_currency + age)


# num = input("Please enter your phone number: ")
# print(f"phone number {num}")


def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


printHello()
calculate()


def name(name):
    print(name)


def divide_by_two(num):
    print(num / 2)


name("Ariel")
divide_by_two(10)


def sum(x, y):
    return x + y


def space(stra, strb):
    return stra + " " + strb


print(sum(5, 5))
print(space("ariel", "itach"))

for i in range(1, 6):
    print(i * "#")

for i in range(1, 6):
    for j in range(i):
        print("#", end="")
    print()

for i in range(7):
    for j in range(7):
        if j == i or j == 7 - i - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()


def get_num():
    num = input("Please enter number: ")
    return num


def get_digits_from_num(x):
    strx = str(x)
    sum = 0
    for i in range(len(str(strx))):
        sum = sum + int(strx[i])
    return sum


print(get_digits_from_num(get_num()))
