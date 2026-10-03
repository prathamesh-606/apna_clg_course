#WAP to count the number of students with the "A" grade in the tuple : (C, D, A, A, B, B, A)
#Store the above values in a list & sort them 
grade = ("C", "D", "A", "A", "B", "B", "A")
count_A = grade.count("A")
print(count_A)

grade_list = list(grade)
grade_list.sort()
print(grade_list)