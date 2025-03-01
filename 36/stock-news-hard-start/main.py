import urllib
from urllib.parse import urlencode
import requests
import os
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API = os.environ.get("NEWS_API_KEY")
STOCK_API = os.environ.get("ALFA_VANTAGE_API")

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
    "symbol" : "TSLA",
    "apikey" : STOCK_API,
}
# response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
# response.raise_for_status()
# data = response.json()
#
# today = datetime.date.today()
# delta = datetime.timedelta(days=1)
# yesterday = today - delta
# day_before_yesterday = yesterday - delta
#
# yesterday = str(yesterday)
# day_before_yesterday = str(day_before_yesterday)
#
# yesterday_cv = float(data["Time Series (Daily)"][yesterday]['4. close'])
# day_before_yesterday_cv = float(data["Time Series (Daily)"][day_before_yesterday]['4. close'])
#
# is_high_change, change_percentile = calculate_change_percentage(yesterday_cv, day_before_yesterday_cv)




## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if True:
    news_parameters = {
        "q" : "Tesla",
        "pageSize" : 3,
        "apikey" : NEWS_API
    }
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()

    news_list = []
    for index in range(0, 2):
        data = response.json()
        title = data["articles"][index]["title"]
        url = data["articles"][index]["url"]

        description = (data["articles"][index]["description"])

        news = {
            "Title" : title,
            "url" : url,
            "Description" : description,
        }
        news_list.append(news)

print(news_list)




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

