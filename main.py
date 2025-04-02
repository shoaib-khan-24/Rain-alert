import requests
from twilio.rest import Client

RECEIVER_MOBILE_NO = "1234567890"

api_key = "b99fd8ce96859cdaef5562dfa1e16e3a"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 42.331429
MY_LON = -83.045753

account_sid = "AC39001723e555612bd6724d5e93707806"
auth_token = "d37b5691a11b2d8bbefd99e2264e73b3"

weather_parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LON,
    "appid" : api_key,
    "cnt" : 4
}

response = requests.get(url=OWM_endpoint , params=weather_parameters)
response.raise_for_status()
weather_data_list = response.json()["list"]

is_raining = False

for weather_data in weather_data_list:
    weather_id = weather_data["weather"][0]["id"]
    if weather_id < 700:
        is_raining = True

if is_raining:
    client = Client(account_sid , auth_token)
    message = client.messages.create(
        body="Is it going to rain today.\nBring an umbrella.",
        from_="+13802604957",
        to=RECEIVER_MOBILE_NO,
    )
    print(message.status)




