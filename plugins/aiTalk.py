from slackbot.bot import default_reply


class A3RTTalk(object):
    def __init__(self, endpoint=None, token=None):
        self.endpoint = endpoint
        self.token = token

    def talk(self, text):
        response = self.fetch(text)
        return response["results"][0]["reply"]

    def fetch(self, text):
        return {
            'results': [
                {'reply': "はいなんでしょう"}
            ]
        }


@default_reply()
def reply(message):
    text = message.body['text']

    talk_api = A3RTTalk("https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk", "DZZD5nGrQ5PDZDeqHmw6BQOunH5yiRMs")
    response = talk_api.talk(text)
    message.send(response)
