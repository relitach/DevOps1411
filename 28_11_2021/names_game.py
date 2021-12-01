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

with open("names.txt") as f: # after this scope "with" close the file
    for line in f.readlines():
        print(line)

try:
    names_file = open("asdasdasd.txt", "r")
except BaseException as e:
    print(e.args)

names_file = open("dasd.txt", "dsadasdas")

