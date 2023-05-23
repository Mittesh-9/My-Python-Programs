# Exercise 3 CWH (KBC) Create a program capable of displaying questions to the user like KBC.

#-> Use list data type to store questions and correct answers.
#-> Display the final amount the person is taking home after playing the game.

import sys

questions = ["Which famous painter created the Mona Lisa?",["a) Leonardo da Vinci", "b) Pablo Picasso", "c) Vincent van Gogh", "d) Michelangelo"],"Who is the author of the Harry Potter book series?",["a) J.R.R. Tolkien", "b) J.K. Rowling", "c) George R.R. Martin", "d) Stephen King"],"What is the chemical symbol for the element gold?",["a) Au", "b) Ag", "c) Fe", "d) Hg"],"Which musical instrument has 88 keys",["a) Violin", "b) Guitar", "c) Piano", "d) Flute"],"What is the largest planet in our solar system?",["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"]]

prize_money = [1000000, 1500000, 2000000, 2500000, 3000000]

print("Welcome to play KBC")

print(questions[0])
print(questions[1])
user_input = (input("Write the correct answer : "))
if user_input == questions[1][0]:
    print(f"Correct answer, You have won \u20B9 {prize_money[0]}")
else:
    print("Wrong answer, Better luck next time")
    sys.exit()

print(questions[2])
print(questions[3])
user_input = (input("Write the correct answer : "))
if user_input == questions[3][1]:
    print(f"Correct answer, You have won \u20B9 {prize_money[0] + prize_money[1]}")
else:
    print("Wrong answer, Better luck next time")
    print(f"You have won \u20b9 {prize_money[0]}")
    sys.exit()

print(questions[4])
print(questions[5])
user_input = (input("Write the correct answer : "))
if user_input == questions[5][0]:
    print(f"Correct answer, You have won \u20B9 {prize_money[0] + prize_money[1] + prize_money[2]}")
else:
    print("Wrong answer, Better luck next time")
    print(f"You have won \u20b9 {prize_money[0] + prize_money[1]}")
    sys.exit()

print(questions[6])
print(questions[7])
user_input = (input("Write the correct answer : "))
if user_input == questions[7][2]:
    print(f"Correct answer, You have won \u20B9 {prize_money[0] + prize_money[1] + prize_money[2] + prize_money[3]}")
else:
    print("Wrong answer, Better luck next time")
    print(f"You have won \u20b9 {prize_money[0] + prize_money[1] + prize_money[2]}")
    sys.exit()

print(questions[8])
print(questions[9])
user_input = (input("Write the correct answer : "))
if user_input == questions[9][2]:
    print(f"Correct answer, You have won \u20B9 {prize_money[0] + prize_money[1] + prize_money[2] + prize_money[3] + prize_money[4]}")
else:
    print("Wrong answer, Better luck next time")
    print(f"You have won \u20b9 {prize_money[0] + prize_money[1] + prize_money[2] + prize_money[3]}")
    sys.exit()

print("Thank you for playing KBC")