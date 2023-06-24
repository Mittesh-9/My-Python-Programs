'''(Intro to Lists)

Question ---

In the Python course, you'll learn all about list comprehensions, which allow you to create a list based on the values in another list. In this question, you'll get a brief preview of how they work.

{    Say we're working with the list below.
test_ratings = [1, 2, 3, 4, 5]

test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked)    }

---In this question, you'll use this list comprehension to define a function percentage_liked() that takes one argument as input:

ratings: list of ratings that people gave to a movie, where each rating is a number between 1-5, inclusive
We say someone liked the movie, if they gave a rating of either 4 or 5. Your function should return the percentage of people who liked the movie.

For instance, if we supply a value of [1, 2, 3, 4, 5, 4, 5, 1], then 50% (4/8) of the people liked the movie, and the function should return 0.5.

Part of the function has already been completed for you. You need only use list_liked to calculate percentage_liked.'''

# Solution --->

def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked) / len(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])