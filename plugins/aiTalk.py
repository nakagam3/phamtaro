import configparser
import requests
from slackbot.bot import default_reply

ini = configparser.ConfigParser()
ini.read('./config.ini', 'UTF-8')


@default_reply()
def reply(message):
    talk_api = A3RTTalk(ini['talk']['endpoint'], ini['talk']['token'])

    text = message.body['text']
    message.send(talk_api.talk(text))


class A3RTTalk(object):
    def __init__(self, endpoint=None, token=None):
        self.endpoint = endpoint
        self.token = token

    def talk(self, text):
        response = self.fetch(text)
        return response['results'][0]['reply']

    def fetch(self, text):
        param = {'apikey': self.token, 'query': text}
        response = requests.post(self.endpoint, param)
        return response.json()
