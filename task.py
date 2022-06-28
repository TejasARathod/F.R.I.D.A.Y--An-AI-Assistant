# Two types of functions - Input and Non-Input
from time import time
from speak import speak
import datetime
import wikipedia
import pywhatkit as kt
from listen import listen
import os
import webbrowser
import smtplib
import requests
import pyautogui
import datetime
from email.policy import default
from http import server
from json.tool import main
from urllib import response
from xmlrpc.client import DateTime
from PyDictionary import PyDictionary
import spotipy
import json
import sys
import spotipy.util as util
from json.decoder import JSONDecodeError
import openrouteservice
from openrouteservice import convert
import folium
from geopy.geocoders import Nominatim
import geopy.geocoders
from playsound import playsound
import speedtest

def Time():
    strtime = datetime.datetime.now().strftime("%H:%M:%S") # getting the current time
    speak(f"Sir, the time is {strtime}")

def Date():
    date = datetime.datetime.now().today()
    speak(f"Sir, today's date is {date}")

def Day():
    day = datetime.datetime.now().strftime("%A") 
    speak(f"Sir, today's day is {day}")

def NonInputExec(query):

    query = str(query)

    if "time" in query:
        try:
            Time()
        except:
            speak("sorry , unable to get the time right now")

    elif "date" in query:
        try:
            Date()
        except:
            speak("sorry , unable to get the date right now")

    elif "day" in query:
        try:
            Day()
        except:
            speak("sorry , unable to get the day right now")

    elif 'discord' in query:
        try:
            path = "C:\\Users\\Tejas Rathod\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk" # location of Discord App for it to open
            os.startfile(path)
        except:
            speak("sorry, cannot open discord right now")

    elif 'word' in query:
        try:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk" 
            os.startfile(path)
        except:
            speak("sorry, cannot open word right now")

    elif 'powerpoint' in query:
        try:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk" 
            os.startfile(path)
        except:
            speak("sorry, cannot open powerpoint right now")

    elif 'excel' in query:
        try:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk" 
            os.startfile(path)
        except:
            speak("sorry, cannot open excel right now")


    elif 'chrome' in query:
        try:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(path)
        except:
            speak("sorry, cannot open chrome right now")

    elif 'youtube' in query:
        try:
            webbrowser.open('youtube.com') # opens Youtube from webbrowser
        except:
            speak("sorry, cannot open youtube right now")

    elif 'weather' in query:
        speak("getting the weather details")
        try:
            Weather()
        except Exception as e:
            speak("Sorry , cannot get the details for current weather right now.")

    elif 'menu' in query:
        try:
            speak('opening windows start menu')
            pyautogui.hotkey('ctrl', 'esc')
        except:
            speak("sorry, cannot open menu right now")

    elif 'screenshot' in query:
        try:
            speak('opening windows snipping tool')
            pyautogui.hotkey('win', 'shift', 's')
        except:
            speak("sorry, cannot open windows snipping tool right now")

    elif 'music' in query:
        try:
            speak('playing music from spotify')
            Spotify()
        except:
            speak('sorry , unable to retrieve any song at the moment')


    elif 'maps' in query:
        try:
            maps()
        except:
            speak('cannot access maps right now')

    elif 'alarm' in query:
        try:
            speak("Enter the Time please")
            time = input("Enter the time: ")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time is up Sir!")
                    playsound('bully_maguire.mp3')
                    speak("Alarm is now closed")

                elif now>time:
                    break
        except:
            speak("sorry, unable to setup an alarm right now")

    elif 'reminder' in query:
        try:
            speak("What would you like me to remind you?")
            Rmsg = listen()
            Rfile = open('data.txt','w')
            Rfile.write(Rmsg)
            Rfile.close()
            speak('Your reminder has been saved successfully')
        except:
            speak("sorry, unable to setup a reminder right now")

    elif 'remember' in query:
        try:
            Rfile = open('data.txt','r')
            speak("Here's what you had set as your reminder" + Rfile.read())
        except:
            speak("sorry , cannot remember what you had said to me at the moment")

    elif 'speed' in query:
        try:
            SpeedTest()
        except:
            speak("sorry, unable conduct the internet speed test at this moment")


def InputExec(tag,query):

    if "wikipedia" in tag:
        try:
            speak('Searching Wikipedia...')
            query = str(query).replace("wikipedia","").replace("who is","").replace("about","").replace("what is","").replace("tell me about","") # replacing wikipedia in speech with blank so that it helps in obtaining info. about that specific thing asked
            results = wikipedia.summary(query, sentences=1) # speak info upto 1 line
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except:
            speak("Sorry , unable to retrieve any information from wikipedia")

    elif "google" in tag:
        try:
            speak("what do you want me to search for?")
            word = listen()
            print('Searching...')
            #query = str(query).replace("search","").replace("google","").replace("google search","").replace("perform google search","")
            kt.search(word)
        except:
            speak("sorry , unable to perform google search")
            
    elif 'email' in tag:
            try:
                speak("What should I say?")
                content = listen() # content of the mail
                to = "tejasrathod007@rediffmail.com" # email id of person to send to
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir , I am not able to send this email")

def maps():
    geopy.geocoders.options.default_user_agent = 'loc.py'

    # calling the Nominatim tool
    loc = Nominatim()

    # entering the location name
    speak('Please mention a destination you would like to start off with')
    add1 = listen()
    speak('Please mention a destination you would like to reach')
    add2 = listen()
    Loc1 = loc.geocode(add1)

    # printing address
    print(Loc1.address)

    # printing latitude and longitude
    Lat1 = Loc1.latitude
    Long1 = Loc1.longitude
    print("Latitude = ",Lat1 , "\n")
    print("Longitude = ",Long1,"\n" )

    Loc2 = loc.geocode(add2)

    # printing address
    print(Loc2.address)
    Lat2 = Loc2.latitude
    Long2 = Loc2.longitude
    # printing latitude and longitude
    print("Latitude = ",Lat2, "\n")
    print("Longitude = ", Long2)

    client = openrouteservice.Client(key='5b3ce3597851110001cf62485ade6831604f4dab89207834cfc0399b')

    #set location coordinates in longitude,latitude order
    coords = ((Long1,Lat1),(Long2,Lat2))
    #call API
    res = client.directions(coords)
    geometry = client.directions(coords)['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)

    distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
    duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

    m = folium.Map(location=[6.074834613830474, 80.25749815575348],zoom_start=10, control_scale=True,tiles="cartodbpositron")
    folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)

    folium.Marker(
        location=list(coords[0][::-1]),
        popup="Galle fort",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    folium.Marker(
        location=list(coords[1][::-1]),
        popup="Jungle beach",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    speak('opening map')
    m.save('map.html')
    webbrowser.open_new_tab('map.html')

    


def wishMe(): # function to greet the user according to the time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Friday, Sir. Please tell me how may I help you? ")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # This class manages a connection to an SMTP or ESMTP server
    server.ehlo() #  Hostname to send for this command defaults to the FQDN of the local host.
    server.starttls() # Puts the connection to the SMTP server into TLS mode. If you provide the keyfile and certfile parameters, the identity of the SMTP server and client can be checked.
    server.login('tejasrathod709@gmail.com', '@Rmafcbcfc123')
    server.sendmail('tejasrathod709@gmail.com',to,content)
    server.close()

def Weather():
    complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q=Pune&appid=0b3b598b540995e9755cdf8ab184dcaa'
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()


    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']

    temp = "Current temperature is {:.2f} degree Celsius ".format(temp_city)
    desc = "Current weather description is "+ str(weather_desc)
    hum =  "Current Humidity is " + str(hmdt) + '%'
    wind = "Current wind speed is " + str(wind_spd) + 'kmph'

    print(temp)
    print(desc)
    print(hum)
    print(wind)

    speak(temp)
    speak(desc)
    speak(hum)
    speak(wind)

scope = 'user-read-private user-read-playback-state user-modify-playback-state'


username = '31dwnnxv5x5bspqqlq4itb4whxn4'

client_id = 'c0fbbe8353b04bb0b5b9e4bf805bec21'
client_secret = 'e2125648febd477a8277fb7cebb857c6'
redirect_uri = 'http://google.com/'


token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# Get current device
devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

def Spotify():
    # Main Menu
    speak("Welcome to Spotipy " + displayName + "!")
    speak("Please specify an artist name")
    searchQuery = listen()
    # Get search results
    searchResults = spotifyObject.search(searchQuery,1,0,"artist")

    # Artist details
    artist = searchResults['artists']['items'][0]
    print(artist['name'])
    print(str(artist['followers']['total']) + " followers")
    print(artist['genres'][0])
    print()
    webbrowser.open(artist['images'][0]['url'])
    artistID = artist['id']


    # Album and track details
    trackURIs = []
    trackArt = []
    z = 0

    # Extract album data
    albumResults = spotifyObject.artist_albums(artistID)
    albumResults = albumResults['items']

    for item in albumResults:
        print("ALBUM: " + item['name'])
        albumID = item['id']
        albumArt = item['images'][0]['url']

        # Extract track data
        trackResults = spotifyObject.album_tracks(albumID)
        trackResults = trackResults['items']

        for item in trackResults:
            print(str(z) + ": " + item['name'])
            trackURIs.append(item['uri'])
            trackArt.append(albumArt)
            z+=1
        print()

    # See album art
    while True:
        speak("Please specify a song number to see album artist and play the song" )
        songSelection = int(listen()) # and play the song
        if songSelection == "x":
            break
        trackSelectionList = []
        trackSelectionList.append(trackURIs[int(songSelection)])
        spotifyObject.start_playback(deviceID, None, trackSelectionList) # added
        webbrowser.open(trackArt[int(songSelection)])


def SpeedTest():
    speak("Checking Speed")
    print("Checking Speed...") 
    speed = speedtest.Speedtest()
    download = speed.download()
    corr_down = int(download/800000)
    upload = speed.upload()
    corr_upload = int(upload/800000)
    print(" ")
    speak("Here is the result of your speed test")
    speak("Your uploading speed is " + str(corr_upload) + " mbps")
    print(str(corr_upload) + " mbps")
    speak("Your downloaing speed is " + str(corr_down) + " mbps")
    print(str(corr_down) + " mbps")

