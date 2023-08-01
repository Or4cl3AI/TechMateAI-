
# Generated by CodiumAI
from pickle import APPENDS

from pickle import APPEND


import pytest

class TestChat:
    # Tests that the chat function can handle messages with emojis
    def test_emojis(self):
        with app.test_client() as client:
            response = client.post('/chat', data={'message': 'Hello 👋🏼'});
            assert response.status_code == 200


    # Tests that the 'chat' function can handle non-ASCII characters in the message input
    def test_non_ascii_message(self):
        with app.test_client() as client:
            response = client.post('/chat', data={'message': 'こんにちは'})
            assert response.status_code == 200
            assert response.data.decode('utf-8') == 'Hello!'


    # Tests that the 'chat' function can handle a long message without errors
    def test_long_message(self):
        long_message = 'a' * 1000
        response = self.client.post('/chat', data={'message': long_message})
        assert response.status_code == 200

