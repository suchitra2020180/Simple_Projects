##Project 22: Converting student scores to grades

student_score={
"Harry":81,
"Sita":50,
"Ron":78,
"Hermoine":99,
"Draco":74,
"Neville":62}

student_grades={}
for student in student_score:
    if student_score[student]>=91 and student_score[student]<100:
        student_grades[student]="Excellent"
    elif student_score[student]>=81 and student_score[student]<=90:
        student_grades[student]="Exceeds Expectation"
    elif student_score[student]>=71 and student_score[student]<=80:
        student_grades[student]="Acceptable" 
    elif student_score[student] <=70:
        student_grades[student]="Fail"

print("===== Student Scores ====")
print(student_score)
print("===== Student Grades ====")
print(student_grades)