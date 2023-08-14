import json
import requests

SLACK_CHANNEL_ID = 'xxxxx'
SLACK_URL = "https://slack.com/api/conversations.history"
TOKEN = "xxxx"

def main():
    payload = {
        "channel": SLACK_CHANNEL_ID,
        "oldest": "1622761200"
    }
    headersAuth = {
    'Authorization': 'Bearer '+ str(TOKEN),
    }  
    response = requests.get(SLACK_URL, headers=headersAuth, params=payload)
    json_data = response.json()
    msgs = json_data['messages']

    with open('messages.json', 'w') as json_file:
      json.dump(msgs, json_file, indent=4)  # JSONファイルに書き出す

    return print(msgs)

if __name__ == "__main__":
    main()