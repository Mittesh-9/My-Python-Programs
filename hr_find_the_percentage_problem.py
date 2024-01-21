if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# Solution >>
    
    if query_name in student_marks:
        marks_to_percentage = student_marks[query_name] 
        percentage_marks = []
        for i in marks_to_percentage:
            percentage_marks.append(i)
        
        average = sum(percentage_marks) / len(percentage_marks)
         
        formatted_average = f'{float(average):.2f}'
        print(formatted_average)
