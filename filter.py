# filter function returns all elements of a collection that pass a condition

grades = [93,98,74,35,45,63,26,90]

passing_grades = list(filter(lambda grade: grade >= 50, grades))

print(passing_grades)