# import smtplib
#
# sender_email = "s.jalalabbasi37@gmail.com"
# password = "ckqwsmwawcqtafcr"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=sender_email, password=password)
#     connection.sendmail(from_addr=sender_email,
#                         to_addrs="s.jalal9s@yahoo.com",
#                         msg="Subject:Hi \n\n This is my message for you bro."
#                         )

import datetime as dt
current_time = dt.datetime.now()
print(current_time)
current_year = current_time.year
current_day = current_time.day
current_weekday = current_time.weekday()
print(current_weekday)

my_datetime = dt.datetime(2024, 12, 1)
print(my_datetime)