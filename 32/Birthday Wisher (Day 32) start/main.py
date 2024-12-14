import smtplib
import datetime as dt
import random


with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()

motivational_sentence = random.choice(quotes)

sundays_index = 6
current_time = dt.datetime.now()
current_weekday = current_time.weekday()

sender_email = "s.jalalabbasi37@gmail.com"
password = "ckqwsmwawcqtafcr"

if current_weekday == sundays_index:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs="s.jalal9s@yahoo.com",
                            msg=f"Subject:Sundays Motivational Quote \n\n {motivational_sentence}"
                            )

# print(current_time)
# current_year = current_time.year
# current_day = current_time.day


#
# my_datetime = dt.datetime(2024, 12, 1)
# print(my_datetime)