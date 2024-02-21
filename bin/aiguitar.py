#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10
# -*- coding: utf-8 -*-
import requests
import json

# Black: 30
# Red: 31
# Green: 32
# Yellow: 33
# Blue: 34
# Magenta: 35
# Cyan: 36
# White: 37

while(True):
    print("\033[31mAIGuitar : \033[0m", end="")
    question = str(input())
    print("\033[32mDownloading...\033[0m")
    if question == "/q":
        break
    if question == "/help":
        print("\033[35m /q => exit \033[0m")
        print("\033[35m /help => all command \033[0m")
        continue
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyDOfLJFYbEX_6XLhAR5fN462X2FYPiU-oo"
    payload = json.dumps({
    "contents": [
        {
        "parts": [
            {
            "text": question
            }
        ]
        }
    ]
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    responseText = response.text
    data = json.loads(responseText)
    res = data['candidates'][0]['content']['parts'][0]['text'].replace("```", "\n===========================\n")
    print("\033[36m" + res + "\033[0m")
    
print("bye.")