from unittest import TestCase

from plugins.aiTalk import A3RTTalk


class TestA3RTTalk(TestCase):
    def test_talk(self):
        talk_api = A3RTTalk("", "")

        response = talk_api.talk("ねえ")

        assert response == "はいなんでしょう"
