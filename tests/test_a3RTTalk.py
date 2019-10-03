from unittest import mock

from plugins.aiTalk import A3RTTalk

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
        
    def raise_for_status(self):
        pass

def mocked_requests_post(*args, **kwargs):
    return MockResponse({
        'status': 0,
        'message': 'ok',
        'results': [
            {
                'perplexity': 1.3358218026477,
                'reply': 'はいなんでしょう'
            }
        ]
    }, 200)

def mocked_requests_post_fail(*args, **kwargs):
    return MockResponse({
        'status': 2000,
       'message': 'empty reply'
    }, 200)


class TestA3RTTalk:

    def setup_method(self, method):
        self.talk_api = A3RTTalk('http://test.co.jp/', 'XXXXXXXXXXXXXXXXXXXX')

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_talk(self, mock_post):
        response = self.talk_api.talk('ねえ')
        assert response == 'はいなんでしょう'

    @mock.patch('requests.post', side_effect=mocked_requests_post_fail)
    def test_talk_fail(self, mock_post):
        response = self.talk_api.talk('ねえ')
        assert response == 'くしくし、何を言ってるかわからないのだ'

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_fetch(self, mock_post):
        response = self.talk_api.fetch('ねえ')

        assert len(response) == 3
        assert response['status'] == 0
        assert response['message'] == 'ok'
        assert len(response['results']) == 1
        assert response['results'][0]['reply'] == 'はいなんでしょう'

