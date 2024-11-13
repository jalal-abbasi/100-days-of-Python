names = ["Jalal", "Hamid", "Ali", "Elahe"]
import random
student_scores = {student: random.randint(1,100) for student in names}

passed_students = {key:value for (key,value) in student_scores.items() if value>=60}

# print(passed_students)

import pandas
my_dictionary = {"Jalal": ["J", "A"], "Hamid": ["H", "A"], "Ali": ["A", "L"], "Elahe": ["E", "L"]}
my_dataframe = pandas.DataFrame(my_dictionary)
# print(my_dataframe)
# for (key,value) in my_dataframe.items():
#     print(value)

for (index, row) in my_dataframe.iterrows():
    if (row.Jalal == "J"):
        print(row)

