student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# not use the sum() or len() functions


count_iter = 0
count = 0
for stud in student_heights:
    count_iter += 1
    count += stud
print(round(count / count_iter))
