def sqre(x):
    print(x * x)


def mul(x, y):
    result = x * y
    return result


sqre(100)
a = mul(100, 9)
print(a)


# input_from_user = int(input("enter your age: "))
#
# if input_from_user > 0:
#     print("age is ok")
#
# input_from_user = int(input("enter your amount of pets: "))
#
# if input_from_user > 0:
#     print("amount of pets is ok")


# def check_input(gt, input_string, print_string):
#     input_from_user = int(input(f"enter your {input_string}: "))
#     if input_from_user > gt:
#         print(f"{print_string} is ok")
#
#
# check_input(0, "age", "age")
# check_input(0, "amount of pets", "amount of pets")

def check_input(gt, input_string):
    input_from_user = int(input(f"enter your {input_string}: "))
    if input_from_user > gt:
        return True
    else:
        return False


result = check_input(0, "age")
if result == True:
    print("age is ok")

result = check_input(2, "amount of pets")
if result == True:
    print("amount of pets is ok")