from logging import Logger
import random
import json
from unittest import result
import torch
from brain import NeuralNet
from NN import bag_of_words,tokenize
#from train import FILE

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json","r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-----------------------

Name = "Friday"
from listen import listen
from speak import speak
from task import NonInputExec, InputExec , wishMe

def Main():
    
    sentence = listen()
    result = str(sentence)

    if sentence == "bye": 
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExec(reply)

                elif "date" in reply:
                    NonInputExec(reply)

                elif "day" in reply:
                    NonInputExec(reply)

                elif "wikipedia" in reply:
                    InputExec(reply,result)

                elif "google" in reply:
                    InputExec(reply,result)

                elif "email" in reply:
                    InputExec(reply,result)

                elif 'discord' in reply:
                    NonInputExec(reply)

                elif 'word' in reply:
                    NonInputExec(reply)

                elif 'powerpoint' in reply:
                    NonInputExec(reply)

                elif 'excel' in reply:
                    NonInputExec(reply)

                elif 'chrome' in reply:
                    NonInputExec(reply)

                elif 'youtube' in reply:
                    NonInputExec(reply)

                elif 'weather' in reply:
                    NonInputExec(reply)

                elif 'menu' in reply:
                    NonInputExec(reply)

                elif 'screenshot' in reply:
                    NonInputExec(reply)

                elif 'music' in reply:
                    NonInputExec(reply)

                elif 'maps' in reply:
                    NonInputExec(reply)

                elif 'alarm' in reply:
                    NonInputExec(reply)

                elif 'reminder' in reply:
                    NonInputExec(reply)

                elif 'remember' in reply:
                    NonInputExec(reply)

                elif 'speed' in reply:
                    NonInputExec(reply)

                else:
                    speak(reply)

from face import facerec
speak("This application is password protected, in order to authenticate the user I will have to run facial recognition")
speak("opening facial recognition app")
speak("Please press the letter v to verify")
y = facerec()
y
if y == True:
    speak("User authenticated")
    wishMe()
    while True:
        Main()
else:
    speak('Sorry, unable to recognize the user. Access Denied!')
    exit()


