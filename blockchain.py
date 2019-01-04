
import time

import pyttsx3

from lxml import html

import requests
import speech_recognition as sr
import webbrowser as wb


r = sr.Recognizer()
r.energy_threshold = 4000
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
r1 = requests.get('https://www.blockchaintechnology-news.com/')
url='https://www.blockchaintechnology-news.com/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
page = requests.get(url, headers=headers)

newVoiceRate = 50
while newVoiceRate <= 300:

    newVoiceRate = newVoiceRate + 50

engine.setProperty('rate', 175)

engine.say("Hello! This is JATOSH    !!!! Here we go! I am presenting latest block chain news for you !!!!!!!Check out the list given below")
engine.runAndWait()

try:
    doc = html.fromstring(page.content)
    XPATH_DOMAIN = '//div[@class="blog-widget-text left relative"]/span//text()'
    RAW_DOMAIN = doc.xpath(XPATH_DOMAIN)
    XPATH_ADDRESS = '//li[@class="infinite-post"]/a//@href'
    RAW_ADDRESS = doc.xpath(XPATH_ADDRESS)
    XPATH_NAME = '//div[@class="blog-widget-text left relative"]/h2//text()'
    RAW_NAME = doc.xpath(XPATH_NAME)
    new_list=[['0)',RAW_DOMAIN[0],RAW_NAME[0],RAW_ADDRESS[0]]]
    new_list.append(['1)',RAW_DOMAIN[1],RAW_NAME[1],RAW_ADDRESS[1]])
    new_list.append(['2)', RAW_DOMAIN[2], RAW_NAME[2], RAW_ADDRESS[2]])
    new_list.append(['3)', RAW_DOMAIN[3], RAW_NAME[3], RAW_ADDRESS[3]])
    new_list.append(['4)', RAW_DOMAIN[4], RAW_NAME[4], RAW_ADDRESS[4]])
    new_list.append(['5)', RAW_DOMAIN[5], RAW_NAME[5], RAW_ADDRESS[5]])
    new_list.append(['6)', RAW_DOMAIN[6], RAW_NAME[6], RAW_ADDRESS[6]])
    new_list.append(['7)', RAW_DOMAIN[7], RAW_NAME[7], RAW_ADDRESS[7]])
    new_list.append(['8)', RAW_DOMAIN[8], RAW_NAME[8], RAW_ADDRESS[8]])
    new_list.append(['9)', RAW_DOMAIN[9], RAW_NAME[9], RAW_ADDRESS[9]])

    for xs in new_list:
            print(" : ".join(map(str, xs)))


except Exception as e:
    print(e)
time.sleep(6)
engine.say("The below given list includes the domain name, headline and the url")
engine.runAndWait()
time.sleep(5)


with sr.Microphone() as source:
    engine.say("Hope you have choosen  !so! please mention the serial number")
    engine.runAndWait()

    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print('You have chosen:\n' + text)
    if('0' in text ):
        wb.get(chrome_path).open(RAW_ADDRESS[0])
    elif ('1' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[1])
    elif ('2' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[2])
    elif ('3' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[3])
    elif ('4' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[4])
    elif ('5' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[5])
    elif ('6' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[6])
    elif ('7' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[7])
    elif ('8' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[8])
    elif ('9' in text):
        wb.get(chrome_path).open(RAW_ADDRESS[9])

    engine.say('Here is your news! Happy Reading!')
    engine.runAndWait()
except Exception as e:
            print(e)
