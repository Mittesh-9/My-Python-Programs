# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

user_choice = input("Please input 'Encode' to encode a message or 'Decode' to decode a message OR Enter 'Q' to quit : ")

if user_choice.lower() == 'encode':
    user_input = input("Please enter the message: ")
    splitted_string = user_input.split(' ')
    new_encoded_string = []
    def myencode(user_input):
        for i in splitted_string:
            if len(i) >= 3:
                random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
                random_chars_2 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
                new_word = random_chars + i[1:] + i[0] + random_chars_2
                new_encoded_string.append(new_word)

            else:
                new_word_1 = i[::-1]
                new_encoded_string.append(new_word_1)

        final_encoded_string = " ".join(new_encoded_string)
        return(final_encoded_string)
    encoded_result = myencode(user_input)
    print(f"Encoded Result: {encoded_result}")

elif user_choice.lower() == 'decode':
    user_input = input("Please enter the message: ")
    new_decoded_string = []
    splitted_string_2 = user_input.split(' ')
    def mydecode(user_input):
        for j in splitted_string_2:
            if len(j) < 3:
                new_word_2 = j[::-1]
                new_decoded_string.append(new_word_2)                
            else:

                new_word_3 = j[3:-3]
                new_word_4 = new_word_3[-1] + new_word_3[0:-1]
                new_decoded_string.append(new_word_4)


        final_decoded_string = " ".join(new_decoded_string)
        return(final_decoded_string)
    decoded_result = mydecode(user_input)
    print(f"Decoded Result: {decoded_result}")

elif user_choice.lower() == 'q':
    print("Quitting the program.")

else:
    print("Invalid choice. Please enter 'Encode', 'Decode', or 'Q' to Quit.")