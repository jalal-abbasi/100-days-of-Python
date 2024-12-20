##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
today = now.day
current_month = now.month

birthdays = pd.read_csv("birthdays.csv")
# dataframe containing the data of people whose birthday day is the same as today
same_day_of_today = birthdays[birthdays.day == today]
# dataframe containing the data of people whose birthday day is the same as today's day and month
have_birthday = same_day_of_today[same_day_of_today.month == current_month]
# List of celebrants' names
birthday_celebrants = have_birthday.name.to_list()

sender_email = "s.jalalabbasi37@gmail.com"
password = "ckqwsmwawcqtafcr"

for celebrant in birthday_celebrants:
    rand_int = random.choice([1, 2, 3])
    letters_directory = f"letter_templates/letter_{rand_int}.txt"
    with open(letters_directory, mode='r') as letter:
        letter_list = letter.readlines()
        if rand_int == 2:
            letter_list[0] = f'Hey {celebrant},\n'
        else:
            letter_list[0] = f'Dear {celebrant},\n'
        message = ''.join(letter_list)

    celebrant_email = have_birthday[have_birthday.name == celebrant].email.to_list()[0]
