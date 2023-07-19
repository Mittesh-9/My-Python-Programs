from textblob import TextBlob

t = 1
while t:
    a = input("Enter the word to be checked:- ") # Incorrect spelling
    print("Original text:- " + str(a)) # Printing original text

    b = TextBlob(a) # Correcting the text

    # Prints the correct spelling
    print("Corrected text:- " + str(b.correct()))
    t = int(input("Try Again? 1 : 0 "))