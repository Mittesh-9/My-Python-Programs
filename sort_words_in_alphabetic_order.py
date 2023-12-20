my_string = input("Enter a string : ")

words = my_string.split()
words.sort()

for word in words:
    print(word)
