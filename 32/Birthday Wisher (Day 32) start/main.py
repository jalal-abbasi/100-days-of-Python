import smtplib

sender_email = "s.jalalabbasi37@gmail.com"
password = "ckqwsmwawcqtafcr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(from_addr=sender_email,
                        to_addrs="s.jalal9s@yahoo.com",
                        msg="Subject:Hi \n\n This is my message for you bro."
                        )
