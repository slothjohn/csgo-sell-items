import os
import requests
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client


#twillio tokens and id
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

#AK REDLINE FIELD TESTED-----------------------------------------------------------------------------------------------------------------------------------------------------------
RedlineUrl = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=AK-47%20|%20Redline%20(Field-Tested)"

response = requests.get(RedlineUrl)
RedlineData = response.json()

#json returns ex. {"success":true,"lowest_price":"$14.57","volume":"452","median_price":"$14.33"}
#slice lowest_price to remove $ and convert to float
curPrice = float(RedlineData["lowest_price"][1:])

if curPrice >= 19.50:
  #send the message
  message = client.messages.create(
    body="AK is above $19.50",
    from_="+12513223091",
    to="+16463937873"
  )


# M4A4 | Evil Daimyo (Field-Tested)-----------------------------------------------------------------------------------------------------------------------------------------------------------
M4Url = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=M4A4%20|%20Evil%20Daimyo%20(Field-Tested)"

response = requests.get(M4Url)
M4Data = response.json()

#json returns ex. {"success":true,"lowest_price":"$14.57","volume":"452","median_price":"$14.33"}
#slice lowest_price to remove $ and convert to float
curPrice = float(M4Data["lowest_price"][1:])

if curPrice >= 3.00:
  #send the message
  message = client.messages.create(
    body="M4 is above $3.00",
    from_="+12513223091",
    to="+16463937873"
  )
