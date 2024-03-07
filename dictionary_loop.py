# A for loop over a dictionary will loop over its keys

numbers = {'one': 'Pluto', 'two': 2, 'three': 3, 'eleven': 11}

# print(numbers["two"]) >> checking  if we can access the value of key two
for i in numbers:
    print("{} = {}".format(i, numbers[i]))



# The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. (In Python jargon, an item refers to a key, value pair)
    
planet_to_initial = {'Mercury': 'M',
                    'Venus': 'V',
                    'Earth': 'E',
                    'Mars': 'M',
                    'Jupiter': 'J',
                    'Saturn': 'S',
                    'Uranus': 'U',
                    'Neptune': 'N'}

# print(planet_to_initial)

for planet , initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet, initial))
