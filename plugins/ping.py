import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('ping', re.IGNORECASE)
def reply(message, *param):
    message.send('pong')

