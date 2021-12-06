def final_grade(homework, assessment, exam):
    i= (homework + assessment + exam) / 175 * 100
    grade = ""
    if i<=25: grade=" D"
    elif i>25 and i<=50: grade=" C"
    elif i>50 and i<=70: grade=" B"
    elif i>70 and i<=90: grade=" A"
    elif i>90: grade="A*"
    return grade, i
   
    
    

final_marks=final_grade(23, 48, 92)
print(final_marks)






