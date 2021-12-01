what_to_print = "hello world! \n"
print(what_to_print * 4)
amount_of_prints = 4

whatt_to_print = "hello world!"
for i in range(4):
    print(whatt_to_print)

for i in range(amount_of_prints):
    print(str(i) + ") " + whatt_to_print)

list_of_names = ["michael", "hen", "noam", "lior", "amichai"]
for i in range(len(list_of_names)):
    print(list_of_names[i])

for name in list_of_names:
    print(name)
    if name == "hen":
        break

for name in list_of_names:
    if name == "hen":
        continue
    print(name)

a = 0
while a < 10:
    print(a)
    a = a + 1

for i in range(100):
    if i % 7 == 0 or int(i / 10) == 7 or int(i % 10) == 7 or "7" in str(i):
        print("Boom!")
    else:
        print(i)

for i in range(1, 101):
    if i % 7 == 0 or int(i / 10) == 7 or int(i % 10) == 7 or "7" in str(i):
        pass  # don't do nothing
    else:
        print(i)

a = 0
while a < 10:
    print(a)
    a = a + 1
else:
    print("finished successfully")


a = "a"
while a != "q":
    a = input("enter q or not:")
else:
    print("finished successfully")


