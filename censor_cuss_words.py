from better_profanity import profanity

text = input("Enter the text you want to censor: ")

censored = profanity.censor(text)

print(censored)