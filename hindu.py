
from bs4 import BeautifulSoup
import time
import pyttsx3

import requests
import speech_recognition as sr
import webbrowser as wb

all_tweets_ids = []
all_tweets_texts = []
url = 'https://twitter.com/awscloud?lang=en'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
timeline = html.select('#timeline li.stream-item')
r = sr.Recognizer()
r.energy_threshold = 4000
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.get(url, headers=headers)
for tweet in timeline:
    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    all_tweets_ids.append(tweet_id)
    all_tweets_texts.append( tweet_text)
print(all_tweets_ids[19])
a=0
for i in all_tweets_texts:
    print(a,")",i)
    a=a+1
    print()

newVoiceRate = 50
while newVoiceRate <= 300:

    newVoiceRate = newVoiceRate + 50

engine.setProperty('rate', 175)

engine.say("Hello! This is JATOSH    !!!! Here we go! I am presenting latest aws news for you from twitter !!!!!!!Check out the list given below")
engine.runAndWait()

time.sleep(6)
engine.say("This includes the tweet")
engine.runAndWait()
time.sleep(5)


with sr.Microphone() as source:
    engine.say("Hope you have choosen  !so! please mention the serial number")
    engine.runAndWait()

    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print('You have chosen:\n' + text)
    if(text=='0' ):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/"+all_tweets_ids[0])
    elif (text=='1'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[1])
    elif (text=='2'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[2])
    elif (text=='3'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[3])
    elif (text=='4'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[4])
    elif (text=='5'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[5])
    elif (text=='6'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[6])
    elif (text=='7'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[7])
    elif (text=='8'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[8])
    elif (text=='9'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[9])
    elif (text=='10'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[10])
    elif (text=='11'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[11])
    elif (text=='12'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[12])
    elif (text=='13'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[13])
    elif (text=='14'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[14])
    elif (text=='15'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[15])
    elif (text=='16'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[16])
    elif (text=='17'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[17])
    elif (text=='18'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[18])
    elif (text=='19'):
        wb.get(chrome_path).open("https://twitter.com/awscloud/status/" + all_tweets_ids[19])

    engine.say('Here is your news! Happy Reading!')
    engine.runAndWait()
except Exception as e:
            print(e)
