import requests
from send_mail import send_email
#import streamlit as st

#Get url
api_key="948212c9027947c0a1b743c8c9b6cee7"

topic="tesla"
#url="https://newsapi.org/v2/everything?q=tesla&from=2024-12-07&sortBy=publishedAt&apiKey=948212c9027947c0a1b743c8c9b6cee7"
url ="https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2024-12-07&" \
    "sortBy=publishedAt&" \
    "apiKey=948212c9027947c0a1b743c8c9b6cee7&"\
    "language=en"
#url="https://news.yahoo.com/"


#Get data from API
response=requests.get(url)
content_text=response.text
print('Contnet type:',type(content_text))
#st.write(content)
content=response.json()


print('Content:',content)
print('Articles:',content['articles'])
print(content.keys())
print('No of articles:',len(content["articles"]))
#print all articles

# for article in content["articles"]:
#     print('Title:',article['title'])
#     print('Description:',article['description'])
    
#     print(article)
#     print('----------------------')
    
#Lets send the content to mail
body=" "
for article in content['articles'][:20]:
    #if article['title'] or article['description'] is not None:
        #body= "Subject: Today's news" + '\n' +body +'Title: ' + article['title']+ '\n' +article['description'] + 2*'\n'
       # body = body +'Title: ' + article['title']+ '\n' +article['description'] + 2*'\n'
        
       # print(body)
        print('------')
        title = article.get('title') or 'No Title'  # Set default 'No Title' if None
        description = article.get('description') or 'No Description'  # Set default 'No Description' if None
    
        body += "Subject: Today's news" + '\n' + 'Title: ' + title + '\n' + description + '\n'+ article['url'] + '\n\n'
    

body = body.encode('utf-8')
send_email(message=body)
print('News sent')