''' Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line. '''

if __name__ == '__main__':
    st_arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st_arr.append([name,score])
    
    sorted_arr = sorted(list(set([x[1] for x in st_arr])))
    second_high = sorted_arr[1]
    
    #print(second_high)
    
    student_name = []
    
    for student in st_arr:
        if second_high == student[1]:
            student_name.append(student[0])
            
    for i in sorted(student_name):
        print(i)
