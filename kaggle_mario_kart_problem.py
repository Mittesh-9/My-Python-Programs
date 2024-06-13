# Import luigi's full dataset of race data
# from learntools.python.luigi_analysis import full_dataset

sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]


# Fix me!     # Hint >>
# What is the type of variable i?
# What happens if you inspect the full_dataset list you imported? (Don't worry, it's not actually that big.) Can you find the racer that's causing the error?
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            racer['name'] = ('Unknown racer')
            # print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(i+1, len(racers), racer['name']))
    print(winner_item_counts)



best_items(sample)
# Try analyzing the imported full dataset
# best_items(full_dataset)

# TypeError                                 Traceback (most recent call last)
# Cell In[6], line 26
#      23     return winner_item_counts
#      25 # Try analyzing the imported full dataset
# ---> 26 best_items(full_dataset)

# Cell In[6], line 21, in best_items(racers)
#      18     # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
#      19     if racer['name'] is None:
#      20         print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
# ---> 21             i+1, len(racers), racer['name'])
#      22              )
#      23 return winner_item_counts

# TypeError: can only concatenate str (not "int") to str




# Solution: Luigi used the variable name i to represent each item in racer['items']. However, he also used i as the loop variable for the outer loop (for i in range(len(racers))). These i's are clobbering each other. This becomes a problem only if we encounter a racer with a finish of 1 and a name of None. If that happens, when we try to print the "WARNING" message, i refers to a string like "green shell", which python can't add to an integer, hence a TypeError.

# This is similar to the issue we saw when we imported * from math and numpy. They both contained variables called log, and the one we got when we tried to call it was the wrong one.

# We can fix this by using different loop variables for the inner and outer loops. i wasn't a very good variable name for the inner loop anyways. for item in racer['items'] fixes the bug and is easier to read.

# Variable shadowing bugs like this don't come up super often, but when they do they can take an infuriating amount of time to diagnose!