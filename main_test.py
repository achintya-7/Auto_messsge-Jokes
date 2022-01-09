output = {
    "success": {
        "total": 1
    },
    "contents": {
        "jokes": [{
            "category": "jod",
            "title": "Joke of the day ",
            "description": "Joke of the day ",
            "background": "",
            "date": "2019-01-23",
            "joke": {
                "title":
                "Courtship Signals",
                "length":
                "83",
                "clean":
                "1",
                "racial":
                "0",
                "date":
                "2019-01-23",
                "id":
                "He3_WpaNfBV1Hs7zMLsR4QeF",
                "text":
                "Q. Why shouldn't you marry a tennis player?\r\nA. Because Love means nothing to them."
            }
        }],
        "copyright":
        "2018-20 https://jokes.one"
    }
}

jokes = output['contents']['jokes'][0]
final = jokes['joke']['text']

## Main code

from twilio.rest import Client as Client2
import os

from appwrite.client import Client
from appwrite.services.database import Database

# account_sid = os.environ['ACCOUNT_SID']
# auth_token = os.environ["AUTH_TOKEN"]

account_sid = 'ACed6990b7175b248dc25f724c76ca40cf'
auth_token = 'c8ef2235878fe57f1a659e74721de340'
client = Client2(account_sid, auth_token)

client_aw = Client()
client_aw.set_endpoint("https://35.202.222.146/v1")
client_aw.set_project("61d5806909248")  # this is available by default.
client_aw.set_key( "4869aa1dfa376452b50b6024f7619927c1999a47a2d2c232449d94f80aea7f5525079f3dc3cf28eb8f9a94067fc0eb7475c1c607fed10790ead5bf26da658795c666c379c2f2fbc0f5f9e5bd489c0a2623927df620f3ca5b9763eae0a158ab31d4e17b8ef4d51a68f1998429b27a70ed8f08ffbe5ddd423b7602a6e320b24668")
client_aw.set_self_signed()

database = Database(client_aw)

result = database.list_documents('61d7183bd4dc3', limit=100)  # give the document id amd limit here
collection_list = result['documents']

numbers = []
for i in range(result["sum"]):
    numbers.append(collection_list[i]["db_num"])

try:
    for x in range(result["sum"]):
        print(str(numbers[x]))
        message = client.messages.create(from_='whatsapp:+12564743321',
                                         body=final,
                                         to='whatsapp:+91' + str(numbers[x]))
        print("message sent!")
except Exception as e:
    print(e)
