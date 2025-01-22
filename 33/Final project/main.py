import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 45.464203 # Your latitude
MY_LONG = 9.189982 # Your longitude

MY_POS = [MY_LAT, MY_LONG]

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_position = (iss_latitude, iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

sun_hours = (sunrise, sunset)
time_now = datetime.now()
current_hour = time_now.hour


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def check_iss_is_visible(iss_position, my_position, sun_hours, current_hour):
    is_visible = 0
    for idx in range(0, 2):
        if (my_position[idx] - 5 <= iss_position[idx] <= my_position[idx] + 5) \
                and ((current_hour < sun_hours[0]) or (current_hour > sun_hours[1])):
            is_visible = 1
    return is_visible

while True:
    if check_iss_is_visible(iss_position, MY_POS, sun_hours, current_hour):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            sender_email = "s.jalalabbasi37@gmail.com"
            password = "ckqwsmwawcqtafcr"
            message = "Hey man! go and look up the sky! The ISS is now on top of your head!"
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs="s.jalalabbasi37@gmail.com",
                                msg=f"ISS is visible!! \n\n {message}"
                                )
    time.sleep(60)




