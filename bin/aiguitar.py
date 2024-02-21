import requests
import json

while(True):
    print("AIGuitar : ", end="")
    question = str(input())
    print("Downloading...")
    if question == "/q":
        break
    if question == "/help":
        print(" /q => exit ")
        print(" /help => all command ")
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
    print(data['candidates'][0]['content']['parts'][0]['text'])
    
print("bye.")