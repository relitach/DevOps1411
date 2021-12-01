isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if a >= 2 and strOne == "One" or strThree == "two":
    print("a is greater then 2")
elif b == 2.5:
    print("something")
else:
    print("a i lower than 2")

if a > 0 and a < 4:
    print("yeah its between 0-4")

if 0 < a < 4:
    print("yeah its between 0-4")

my_list = ["hen", "lior", "shay", "ariel"]
if my_list[0] == "hen":
    print("0hen is in the list")
elif my_list[1] == "hen":
    print("1hen is in the list")
elif my_list[2] == "hen":
    print("2hen is in the list")
elif my_list[3] == "hen":
    print("3hen is in the list")


if my_list[0] == "hen" or \
        my_list[0] == "hen" or \
        my_list[0] == "hen" or \
        my_list[0] == "hen":
    print("hen is in the list")


if "hen" in my_list:
    print("in hen is in the list")


my_other_list = ["ariel"]
if my_other_list:
    print("hello")

if len(my_list) > 0:
    print("hey")

c = "aaa"
d = "aaa"

if c is d:
    print("c is d")

cc = ["aaa", "1"]
dd = ["aaa", "1"]

if cc is dd:
    print("cc is dd")

e = 9
if type(e) is int:
    print("e is an integer")

