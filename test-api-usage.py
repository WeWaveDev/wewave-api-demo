import requests

url = "https://api.wewave.ai/api/v1/api-usage-count?apiKey=h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2"

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
