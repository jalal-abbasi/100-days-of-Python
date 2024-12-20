import pandas as pd
import smtplib
import datetime as dt
import random

# Constants for email configuration
SENDER_EMAIL = "s.jalalabbasi37@gmail.com"
PASSWORD = "ckqwsmwawcqtafcr"
SMTP_SERVER = "smtp.gmail.com"

# ----------------- Section 1: Email Sending Function -----------------
def send_email(to_email, subject, body):
    """
    Sends an email to the specified recipient.
    - to_email: Recipient's email address.
    - subject: Subject of the email.
    - body: The content of the email.
    """
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject:{subject}\n\n{body}")

# ----------------- Section 2: Birthday Message Generator -----------------
def get_birthday_message(name):
    """
    Reads a random letter template, replaces [NAME] with the actual name.
    - name: The name of the birthday person.
    """
    letter_path = f"letter_templates/letter_{random.choice([1, 2, 3])}.txt"
    with open(letter_path, mode='r') as file:
        letter_content = file.read()  # Me: so here instead of readline, we get the file as a text
    return letter_content.replace("[NAME]", name)  # Me: we can substitute a word in a string by .replace

# ----------------- Section 3: Fetching Today's Birthdays -----------------
def get_todays_birthdays(birthdays_df):
    """
    Filters the DataFrame to return only the rows for today's birthdays.
    - birthdays_df: DataFrame containing birthday information.
    """
    today = dt.datetime.now()

    # Me: so if you want to get the rows that need to have specific features in more that one column
    # you use & operator
    return birthdays_df[(birthdays_df["day"] == today.day) & (birthdays_df["month"] == today.month)]

# ----------------- Section 4: Main Logic -----------------
# Load birthday data
birthdays = pd.read_csv("birthdays.csv")

# Get today's birthdays
today_birthdays = get_todays_birthdays(birthdays)

# Send emails
# Me: iterrows function iterates over all rows of a dataframe. itself is an iterator, and iterators are designed
# to provide one element at a time during each iteration. it returns each time the index and the contents of the row.
# When you call iterrows() on a DataFrame, it does not directly give you all rows at once.
# Instead, it provides a generator-like object that yields rows one by one when you iterate over it.
for _, row in today_birthdays.iterrows():
    name = row["name"]
    email = row["email"]
    message = get_birthday_message(name)
    send_email(to_email=email, subject="Happy Birthday!", body=message)