"""
$File: god_of_request_bot.py
$Comment: Bot methods
"""
from utilities.config_reader import get_attribute_str
from common.methods import build_url, hit_link
from common.api_signs import *


class GodBot:

    def __init__(self, bot_name):
        self.botname = bot_name
        self.token = get_attribute_str(bot_name, 'access_token')
        self.base_link = get_attribute_str(bot_name, 'root_api')
        self.timeout = get_attribute_str(bot_name, 'timeout')

    def get_update_base_link(self):
        return self.base_link + self.token + BOT_UPDATE

    def get_send_message_base_link(self):
        return self.base_link + self.token + BOT_SEND_MESSAGE

    def get_updates(self, offset=None):
        url = self.get_update_base_link()
        if offset is not None:
            url = build_url(url, offset=str(offset), timeout=get_attribute_str(self.botname, 'timeout'))
        return hit_link(url)

    def send_message(self, message, chat_id):
        url = self.get_send_message_base_link()
        if message is not None:
            url = build_url(url, text=message, chat_id=chat_id)
            hit_link(url)

    def send_message_list(self, message_list, chat_id):
        for message in message_list:
            if message:
                self.send_message(message, chat_id)

