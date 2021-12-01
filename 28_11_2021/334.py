my_file = open("read_my_contents.txt")
# print(list(my_file.readlines()))

for line in my_file.readlines():
    print(line, end='')
print()
my_other_file = open("moshe.txt", "w")
my_other_file.write("hey hey\n")


def save_name(name):
    names_file = open("names.txt", "a")
    names_file.write(name + "\n")
    names_file.close()

def welcome_name_file():
    names_file = open("names.txt", "r")
    for name in names_file:
        print(f"Welcome {name}", end="")
    names_file.close()

save_name("Ariel")
save_name("Arielos")
save_name("Arielush")
save_name("Arielyted")
welcome_name_file()
