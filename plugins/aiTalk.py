import configparser
import requests
import logging
from slackbot.bot import default_reply
from slackbot.settings import DEFAULT_REPLY

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
        if response['status'] == 0:
            return response['results'][0]['reply']
        else:
            return DEFAULT_REPLY

    def fetch(self, text):
        param = {'apikey': self.token, 'query': text}
        response = requests.post(self.endpoint, param)
        response.raise_for_status()
        return response.json()
