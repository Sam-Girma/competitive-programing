def gradingStudents(grades):
    for i in range (len(grades)):
        if grades[i]>=38 and (5-(grades[i]%5))<3:
            grades[i]=(grades[i]//5 +1)*5
    return grades
    
