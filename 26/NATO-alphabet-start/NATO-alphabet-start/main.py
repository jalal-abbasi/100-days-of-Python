student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
df_phono_bet = pandas.read_csv("nato_phonetic_alphabet.csv")
dic_df = {row.letter:row.code for (index, row) in df_phono_bet.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please input the word: ")
letter_list = [letter.capitalize() for letter in user_input]

phonetic_code_list = [dic_df[key] for key in letter_list]

print(phonetic_code_list)






