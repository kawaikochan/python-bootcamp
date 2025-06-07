student_names = ["Juan", "Maria", "Joseph"]
student_scores = [70, 90, 81]
for student_names,student_scores in zip(student_names,student_scores):
    print(student_names,student_scores)
    #print(f{""})

# Print the student scores and names in the following format:
# Student Records:
#   Record: Juan scored 70 in the exam.
#   Record: Maria scored 90 in the exam.
#   Record: Joseph scored 81 in the exam.
#
# Bonus Challenge: Print the highest scorer