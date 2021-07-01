from bot import *
from user.end_user import User
update_id = None

while True:

    for bot in bot_list:
        updates = bot.get_updates(offset=update_id)
        results = updates.get('result', [])

        if results:

            if update_id is None and len(results) != 0:
                update_id = max([int(float(item.get('update_id', 0.0))) for item in results])

            for result in results:
                chat_id = result['message']['chat']["id"]
                message_received = result['message']['text']
                received_from = result['message']['chat']["first_name"]
                is_bot = result['message']['from']["is_bot"]
                language = result['message']['from']["language_code"]
                user = User(chat_id=chat_id, user_name=received_from, is_bot=is_bot, bot_type=type(bot).__name__)
                if update_id == int(result['update_id']):
                    bot.send_message_list(user.make_reply(message_received), chat_id)
                update_id += 1




