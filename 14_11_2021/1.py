print("hello")
my_var = 10
print(my_var)  # another print
my_name = "Ariel"
print(my_name)
is_true = False
# my comment about this variable - short cut = ctrl + ?
my_list = ["ariel", "itach", 29, True, my_name]
print(my_list[1])
my_dict = {"name": "Ariel",
           "lname": "Itach",
           "age": 29,
           "is_married": True,
           123: False}
print(my_dict["name"])
print(my_dict[123])
print(my_dict.keys())

my_number = 5 * 2
my_other = 5 * "Ariel"
print(my_other)

if my_number == 10:
    print("my number is 10")

fname = "Ariel"
lname = "Itach"
print("hello " + fname + " " + lname)  # השיטה הכי בזבזנית בזיכרון
print(f"hello {fname} {lname}")
print("hello %s %s" % (fname, lname))


