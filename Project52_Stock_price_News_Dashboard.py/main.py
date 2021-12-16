## Retrieve stocks of your wish
# Get the news of those stocks
# Create dashboard of price change and news

# challenges faced in sending content : no format
from smtplib import SMTP
import html
my_mail ="osrarts@gmail.com"
pw = "$uch!tr@"

def send_mail(my_mail, pw,Company,up_down,CP_DIFF_percent, Title,Description,URL):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=pw)
        connection.sendmail(from_addr=my_mail, to_addrs="suchitraraniojha@gmail.com", msg=f"Subject: Stock Tesla\n\n {Company} stocks {up_down} by {abs(CP_DIFF_percent)}\n 'Heading:' is {Title}\n  'Brief:'{Description}    \n 'url:' {URL}")

# def send(my_mail, pw,formatted_articles):
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_mail, password=pw)
#         connection.sendmail(from_addr=my_mail, to_addrs="suchitraraniojha@gmail.com", msg=f"Subject: Stock Tesla\n\n {formatted_articles}")


import requests
import datetime as dt
from datetime import timedelta
import smtplib
today = dt.datetime.now()
Date = today.day
print(today)
print(Date)
Yesterday = (dt.datetime.now() - dt.timedelta(1)).date()
yesterday = str(Yesterday)
print(Yesterday)
print("YEST:", yesterday)
Day_before_Yesterday = str((dt.datetime.now() - dt.timedelta(2)).date())
print(Day_before_Yesterday)


Stock_Name="TSLA"
Company = "Tesla"

stock_price_endpoint="https://www.alphavantage.co/query"
sp_api_key = "OB9HXGILEN1MOQI7"
sp_parameters={"function": "TIME_SERIES_DAILY",
               "symbol": Stock_Name,
               "apikey": sp_api_key}

News_endpoint="https://newsapi.org/v2/everything"
News_api_key ="ff057b5d63904ed9a7d93b9fcd828389"
news_parameters={"q": Company,
                    "from":Date,
                    "sortBy":"popularity",
                    "apiKey":News_api_key}

SP_response = requests.get(url=stock_price_endpoint, params=sp_parameters)
SP_response.raise_for_status
print(SP_response.status_code)
SP_data = SP_response.json()
# Yesterday close price
yest_CP = float(SP_data['Time Series (Daily)'][yesterday]['4. close'])
# Day before yesterday closing price of stock
DBY_CP = float(SP_data['Time Series (Daily)'][Day_before_Yesterday]['4. close'])
# CLOSING PRICE DIFFERENCE
CP_DIFF_percent = round(((yest_CP - DBY_CP)/yest_CP)*100,2)
print("diference:", CP_DIFF_percent)
up_down= "None"
if CP_DIFF_percent <0:
    up_down= 'DECREASES'
else:
    up_down = 'INCREASES'
if abs(CP_DIFF_percent) > 1:
    News_response = requests.get(url=News_endpoint, params=news_parameters)
    News_response.raise_for_status
    #print(News_response.status_code)
    News_data = News_response.json()["articles"]
    print("News Data:", News_data)
    # Consider first  articles
    Articles = News_data[:3]
    print(Articles)
formatted_articles =[f"Headline:{article['title']}, \nBrief:{article['description']}\n" for article in Articles]
print("<<=======================>>")
print(formatted_articles)
print("<<=======================>>")
for i in range(0, len(Articles)):
    Title=Articles[i]['title']
    Description = html.unescape(Articles[i]['description']).encode('utf-8')
    Content = Articles[i]['content']
    URL =Articles[i]['url']
    print(Title)
    print(Description)
    print("UT:", Description)
    print(Content)
    print(URL)
    send_mail(my_mail, pw, Company, up_down, CP_DIFF_percent, Title, Description, URL)
    #send(my_mail, pw, formatted_articles)

##Get the stock price
#formatted_articles =[f"Headline:{Articles['title']}, \nBrief:{Articles['description']}" for article in Articles]
#print(formtted_articles)