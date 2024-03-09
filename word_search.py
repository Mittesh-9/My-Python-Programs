def word_search(doc_list, keyword):

    output_list = []

    lowercase_list = [item.lower() for item in doc_list]

    key_to_be_found = f" {keyword.lower()}"

    for i in lowercase_list:
        if key_to_be_found in i:
            output_list.append(lowercase_list.index(i))

    if output_list:
        return output_list

    return ["none"]


doc_list = ["They Learn Python Challenge Casino.", "They bought a car", "Casinoville"]

# result = word_search(doc_list, "Casino")
# result = word_search(doc_list, "bought")
# result = word_search(doc_list, "car")
result = word_search(doc_list, "They")
# result = word_search(doc_list, "not found")

print(result)
