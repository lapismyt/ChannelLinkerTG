import telebot

with open('token.txt', 'r') as file:
    token = file.read().strip()

with open('link.txt', 'r') as file:
    link = file.read().strip()

bot = telebot.TeleBot(token)

@bot.channel_post_handler()
def add_link_to_post(message):
    channel = message.chat.id
    post_id = message.message_id
    caption = message.caption if message.caption else ''
    bot.edit_message_caption(chat_id=channel, message_id=post_id, caption=caption + '\n\n' + link, parse_mode='markdown')

bot.infinity_polling()
