def word_search(doc_list, keyword):

    output_list = []

    lowercase_list = [item.lower() for item in doc_list]

    key_to_be_found = f" {keyword.lower()}"

    for i in lowercase_list:
        if key_to_be_found in i:
            output_list.append(lowercase_list.index(i))

    if output_list:
        return output_list

    return []


def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    print( keyword_to_indices)

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
multi_word_search(doc_list, keywords)
