def count_substring(string, sub_string):
    count = 0
    start = 0
    
    while True:
        index = string.find(sub_string, start)
        if index == -1:
            break
        count += 1
        start = index + 1  # Move to the next character after the current match
    
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
