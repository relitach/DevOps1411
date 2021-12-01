my_number = "4"
result = float(my_number) - 2
print(result)
print("your result is " + str(result))
print(f"your result is {result}")
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list)
print(my_list[2])
print(my_list[0:2])
print(my_list[4:0])
print(my_list[4:0:-1])
print(my_list[0::2])
my_str = 'hello and welcome to "devops experts"'
my_str2 = "hello and welcome to \"devops experts\""
my_str3 = "hello and welcome to \\\"devops experts\\\""
print(my_str)
print(my_str2)
print(my_str3)
print(my_str[::2])
my_dict = {"fname": "Ariel",
           "lname": "Itach",
           "age": 29,
           "id": 203171095}
print(my_dict)
key_to_print = input(f"enter key {list(my_dict.keys())}: ")
print("you choose to print: " + str(my_dict[key_to_print]))

