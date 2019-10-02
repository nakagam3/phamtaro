import configparser
import json

from slackbot.bot import respond_to
from slackbot.bot import listen_to

ini = configparser.ConfigParser()
ini.read('./config.ini', 'UTF-8')


@listen_to('(電球|蛍光灯).?(交換|取り|取替|取換|ちらつ|チラツ).?')
@respond_to('(電球|蛍光灯).?')
def reply(message, *param):
    to = ini['light']['desk_email']
    cc = ini['light']['adc_maillist']

    lamp_replace = LampReplace(to, cc)
    message.send_webapi('へけっ\n下記の◯を書き換えてメールを送るのだ。', json.dumps(lamp_replace.make_api_param()))


class LampReplace:

    def __init__(self, to=None, cc=None):
        self.to = to
        self.cc = cc

    def make_send_message(self):
        subject = '【蛍光灯交換依頼】シーフォート21階'
        body = ('ご担当者 様\n'
                '\n'
                'お疲れ様です。ADCの〇〇です\n'
                '\n'
                'オフィスの蛍光灯がちらついており、交換をお願いできますでしょうか。\n'
                '\n'
                '場所：シーフォート21階\n'
                '本数：〇本\n'
                '\n'
                '以上です。よろしくお願いいたします。\n'
                )
        link = '<mailto:' + self.to + '?cc=' + self.cc + '&amp;subject=' + subject + '|ココ>'

        message = '\n' \
                  'へけっ\n' + link + 'に下記の◯を書き換えてメールを送るのだ。\n\n' \
                                   '```' + body + '```'
        return message

    def make_api_param(self):
        subject = '【蛍光灯交換依頼】シーフォート21階'
        body = ('ご担当者 様\n'
                '\n'
                'お疲れ様です。ADCの〇〇です\n'
                '\n'
                'オフィスの蛍光灯がちらついており、交換をお願いできますでしょうか。\n'
                '\n'
                '場所：シーフォート21階\n'
                '本数：〇本\n'
                '\n'
                '以上です。よろしくお願いいたします。\n'
                )

        attachments = [{
            'color': 'good',
            'title': 'メールを作成',
            'title_link': 'mailto:' + self.to + '?cc=' + self.cc + '&subject=' + subject,
            'text': body
        }]
        return attachments
