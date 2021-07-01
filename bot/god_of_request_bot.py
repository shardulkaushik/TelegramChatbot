"""
$File: god_of_request_bot.py
$Comment: Bot methods
"""
from .god_bot import GodBot


class GodOfRequestsBot(GodBot):

    def __init__(self):
        super(GodOfRequestsBot, self).__init__(type(self).__name__)
