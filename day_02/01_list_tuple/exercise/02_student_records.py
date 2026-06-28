student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""
highest_score = 0
for student_name, student_score in zip(student_names,student_scores):
    print(f"Student: {student_name} scored {student_score} in the exam")

    if student_score > highest_score:
        highest_score = student_score
print(highest_score)