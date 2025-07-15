def groupAnagrams(strs):
    anagram_dict = {}

    for word in strs:
        key = ''.join(sorted(word))
        if key not in anagram_dict:
            anagram_dict[key] = []
        anagram_dict[key].append(word)

    print (list(anagram_dict.values()))


# Input:
strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

groupAnagrams(strs)

def groupAnagrams(strs):
    # Initialize an empty dictionary to hold groups of anagrams
    anagram_dict = {}

    # Loop through each word in the input list
    for word in strs:
        # Sort the letters in the word and join them back to form a string
        # This sorted string will be the key since all anagrams will have the same sorted key
        key = ''.join(sorted(word))

        # If the key doesn't exist in the dictionary, create a new empty list for it
        if key not in anagram_dict:
            anagram_dict[key] = []

        # Append the current word to the correct anagram group based on the key
        anagram_dict[key].append(word)

    # Print the list of grouped anagrams (each group is a list of words)
    print(list(anagram_dict.values()))
