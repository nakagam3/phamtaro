from plugins.lampReplace import LampReplace


class TestLampReplace():

    def test_make_send_message(self):
        to = 'a@gmial.com'
        cc = 'b@gmail.com'

        lamp = LampReplace(to, cc)
        response = lamp.make_send_message()

        assert to in response
        assert cc in response

    def test_make_api_param(self):
        to = 'a@gmial.com'
        cc = 'b@gmail.com'

        lamp = LampReplace(to, cc)
        json = lamp.make_api_param()

        assert json[0]['title'] == 'メールを作成'
        assert '21階' in json[0]['text']
        assert to in json[0]['title_link']
        assert cc in json[0]['title_link']
        assert '&subject=' in json[0]['title_link']
