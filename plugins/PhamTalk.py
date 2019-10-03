import random
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('大?好きなのは')
def reply(message, *param):
    phrase = [
        '一番目はひまわりの種なのだ。二番目はロコちゃんの毛布、三番目はかじりかけのえんぴつ…大好きなのだ！',
        'ひまわりの種なのだ！',
        'ひまわりの種なのだ！',
        'ひまわりの種なのだ！',
        'ひ〜まわりの種〜♪',
        'ひ〜まわりの種〜♪'
    ]
    message.send(random.choice(phrase))

