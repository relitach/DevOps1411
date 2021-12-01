import requests

try:
    response = requests.get("https://dsfsdf .com")
except requests.exceptions.ConnectionError:
    print("unable to connect to host")


# try:
#     a = int(input("enter first number: "))
#     b = int(input("enter second number: "))
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("could not divide by zero")
# except BaseException as e:
#     print("something went wrong" + str(e.args))


def get_user_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age can not be negative")
    return age


age = -1
while age < 0:
    try:
        age = get_user_age()
    except ValueError as e:
        print(e.args[0])

print(f"your age is: {age}")
