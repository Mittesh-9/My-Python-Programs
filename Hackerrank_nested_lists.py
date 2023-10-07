# There are 5 students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

# Solution ----->

if __name__ == '__main__':
    result = []
    names_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name, score])

grades = sorted(set(score for name, score in result))

second_lowest = (grades[1])

for name, score in result:
    if score == second_lowest:
        names_list.append(name)
        names_list.sort()
        
print(' \n'.join(names_list))