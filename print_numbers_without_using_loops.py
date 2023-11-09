def print_number(upper):
  if (upper > 0):
    print_number(upper - 1)
    print(upper)

upper = int(input("Enter upper limit : "))
print_number(upper)
