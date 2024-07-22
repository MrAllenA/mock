import requests

url = "https://api.onesignal.com/apps/c54300e9-f710-473f-aa5b-952228a8b147/users"

payload = {
    "identity": { "my_custom_alias_label": "my_custom_alias_id" },
    "subscriptions": [
        {
            "type": "iOSPush",
            "token": "abcd1234",
            "enabled": True
        }
    ],
    "properties": { "tags": { "firstname": "joe" } }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)