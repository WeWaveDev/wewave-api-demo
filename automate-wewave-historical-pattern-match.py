import datetime
import json

import requests

url = "https://api.wewave.ai/api/v1/historical-pattern-match-events?apiKey=h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2"

ticker_to_analyze = "NVDA"

# start timestamp is millisecond epoch time of now -32 days
# end timestamp is millisecond epoch time of now - 2 days
# using datetime lib
startTimestamp = datetime.datetime.now() - datetime.timedelta(days=32)
endTimestamp = datetime.datetime.now() - datetime.timedelta(days=2)

# convert to milliseconds
startTimestamp = int(startTimestamp.timestamp() * 1000)
endTimestamp = int(endTimestamp.timestamp() * 1000)

print(startTimestamp, endTimestamp)


payload = json.dumps({
  "ticker": ticker_to_analyze,
  "timeInterval": "1D",
  "startTime": startTimestamp,
  "endTime": endTimestamp
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# save the response.text to a json, file name including the ticker and the current timestamp
filename = f"{ticker_to_analyze}-historical-pattern-match-events-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"

# make the response.text pretty
response_text = json.dumps(json.loads(response.text), indent=2)

with open(filename
          , 'w') as f:
    f.write(response_text)
    print(f"File {filename} saved")