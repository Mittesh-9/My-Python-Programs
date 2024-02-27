num = 786

# By using list comprehension
num_lst = [int(x) for x in str(num)]

print(sum(num_lst))


# Another way to do it >>
num_lst2 = []

for x in str(num):
    num_lst2.append(int(x))

print(sum(num_lst2))

# Reversing the num >>

num_lst = [str(x) for x in str(num)]

reverse_num = ''.join(num_lst[::-1])
print(reverse_num)

# Mathematical way to do it >> to be completed

new_num = num % 10

print(new_num)
