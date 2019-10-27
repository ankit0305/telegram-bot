# Services supported Cricket Score, Youtube download, Temp of cities, Random pic, CPUVitals, Date, Time

from datetime import datetime,date
from snap import Snap
from PCVitals import PCVitals
from TempCity import TempCity
from pic import Pic
from cricket import Cricket
import importlib
import json 
import requests
import time
import urllib
#from token import *

TOKEN=""
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
now=datetime.now()  #Time Object
webcam=Snap()       #Cam Object
pcvital=PCVitals()  #Check PC Vitals
temp=TempCity()
pic=Pic()
cri=Cricket()         #Temperature object

def get_url(url):   #second call
    response = requests.get(url)
    content = response.content.decode("utf8")
    js=json.loads(content)
    #print(js)
    return js


def get_updates(offset=None):   #first call
    url = URL + "getUpdates?timeout=100"
    if offset:
        url+="&offset={}".format(offset)
    js = get_url(url)
    #print(js)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates):   #third call
    num_updates = len(updates["result"])
#    print(num_updates)

    last_update = num_updates - 1
#    print(last_update)

    text = updates["result"][last_update]["message"]["text"]
    #print(text)
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    #print(chat_id)

    return (text, chat_id)


def send_message(text, chat_id):  #fourth call
    #text=urllib.parse.quote(text)
    if text.lower()=="/start":
       text="Hi, I am a bot who can do a bunch of services including \n 1. Date(IST) \n 2. Time(IST) \n 3. Cricket-Score \n 4. CPUVitals \n 5. ENVitals \n 6. YouTube-Download \n 7. Pic \n 8. Cam \nOr you know what, You canhit me up with the serial number or the first three letters of the service"        
    elif text.lower()=="date" or text.lower()=='1' or text.lower()=="dat":
       text=date.today()

    elif text.lower()=="time" or text.lower()=='2' or text.lower()=="tim":
       text = now.strftime("%H:%M:%S")

    elif text.lower()=="cricket-score" or text.lower()=="3" or text.lower()=="cri":
       text=cri.match()
       print(text)

    elif text.lower()=="cpuvitals" or text.lower()=="4" or text.lower()=="cpu":

        text=pcvital.sensors()
        #print(se)
        
        
        # text="Hmmm.. I see you are interested in me but I do have some subcategories. \n 41. Sensors \n 42. Process \n 43. Network \n 44. CPU \n 45. Usage"
        # url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)

        
        # if text.lower()=="sensors" or text.lower()=="41":
        #     se=pcvital.sensors()
        #     text=se

        # elif text.lower()=="process" or text.lower()=="42":
        #     pr=pcvital.process()
        #     text=pr


        # elif text.lower()=="network" or text.lower()=="43":
        #     ne=pcvital.network()
        #     text=ne


        # elif text.lower()=="cpu" or text.lower()=="44":
        #     cp=pcvital.cpu()
        #     text=cp


        # elif text.lower()=="usage" or text.lower()=="45":
        #     us=pcvital.usage()
        #     text=us


    elif text.lower()=="envitals" or text.lower()=="5" or text.lower()=="env":
        text=temp.temp()
        
        

    elif text.lower()=="youtube-download" or text.lower()=="6" or text.lower()=="you":
        text="I am yet to be implemented"
        # logic to be implemented

    elif text.lower()=="pic" or text.lower()=="7":
        text=pic.dogpic()
        

    elif text.lower()=="cam" or text.lower()=="8":
        webcam.clickImg()

    else:
       text="I am not sure what it is!"

    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)


# def build_keyboard(items):
#     keyboard = [[item] for item in items]
#     reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
#     return json.dumps(reply_markup)



def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5) #Saves a lot of CPU and Network resource


if __name__ == '__main__':
    main()