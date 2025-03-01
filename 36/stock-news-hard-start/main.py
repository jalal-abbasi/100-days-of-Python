import urllib
from urllib.parse import urlencode
import requests
import os
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API = os.environ.get("NEWS_API_KEY")
STOCK_API = os.environ.get("ALFA_VANTAGE_API")

twilio_phone_number = "+14155238886"
account_sid = "ACe34c895e1146f0a1b54f5e16d8c4512e"
auth_token = os.environ.get("AUTH_TOKEN")

def calculate_change_percentage(yesterday_value, day_before_yesterday_value):
    difference = yesterday_value - day_before_yesterday_value
    change_percentage = difference/day_before_yesterday_value * 100
    return abs(change_percentage) > 5, round(change_percentage, 2)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()

today = datetime.date.today()
delta = datetime.timedelta(days=1)
yesterday = today - delta
day_before_yesterday = yesterday - delta

yesterday = str(yesterday)
day_before_yesterday = str(day_before_yesterday)

yesterday_cv = float(data["Time Series (Daily)"][yesterday]['4. close'])
day_before_yesterday_cv = float(data["Time Series (Daily)"][day_before_yesterday]['4. close'])

is_high_change, change_percentile = calculate_change_percentage(yesterday_cv, day_before_yesterday_cv)




## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if is_high_change:
    news_parameters = {
        "q" : COMPANY_NAME,
        "pageSize" : 3,
        "apiKey" : NEWS_API
    }
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    data = response.json()

    for i in range(0,2):
        title = data["articles"][i]["title"]
        url = data["articles"][i]["url"]

        description = (data["articles"][i]["description"])
        index = description.index(".")
        description = description[0:index +1]

        news = {
            "Headline" : title,
            "url" : url,
            "Brief" : description,
        }

        client = Client(account_sid, auth_token)
        if change_percentile > 0:
            arrow = "🔺"
        else:
            arrow = "🔻"
        message = client.messages.create(
            body=f"{STOCK}: {arrow}{abs(change_percentile)}%\n"
                 f"Headline: {news["Headline"]}\nBrief: {news["Brief"]}\nURL: {news["url"]}",
            from_=twilio_phone_number,
            to="+393515024648",
        )
        print(message.status)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

