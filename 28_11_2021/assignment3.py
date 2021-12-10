try:
    a = 1 / 0
except ZeroDivisionError:
    print("Error: division by zero")

try:
    x = 1
finally:
    print("finally")

words_file = open("words.txt", "w")
words_file.write("Ariel\n")
words_file.close()

words_file = open("words.txt")
for word in words_file:
    print(word, end="")
words_file.close()

words_file = open("words.txt", "w", encoding='utf-8')
words_file.write("בוקר טוב")
words_file.close()

words_file = open("words.txt", encoding='utf-8')
for word in words_file:
    print(word, end="")
words_file.close()

