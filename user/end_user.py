class User:

    def __init__(self, chat_id, user_name, is_bot, bot_type):
        self.chat_id = chat_id
        self.user_name = user_name
        self.is_bot = is_bot
        self.bot_type = bot_type
        self.state = None

    def make_reply(self, message_received):
        if message_received:
            return ['This bot is serious', 'This Bot is dangerous', 'This bot is dumb',
                    'user with name: {},chat id: {} has communicated with bot: {}'.format(self.user_name,
                                                                                          self.chat_id,
                                                                                          self.bot_type),
                    'Message Received from you: {}'.format(message_received)
                    ]
        else:
            return ["Hi Stranger! Welcome to Shardul's Bot"]
