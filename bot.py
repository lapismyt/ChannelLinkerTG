import telebot

with open('token.txt', 'r') as file:
    token = file.read().strip()

with open('link.txt', 'r') as file:
    link = file.read().strip()

bot = telebot.TeleBot(token)

@bot.channel_post_handler(content_types=['text'])
def add_link_to_post(message):
    channel_id = message.chat.id
    post_id = message.message_id
    text = message.text
    bot.edit_message_text(chat_id=channel_id, message_id=post_id, text=text + '\n\n' + link, parse_mode='markdown')

@bot.channel_post_handler(content_types=['photo'])
def add_link_to_caption(message):
    channel_id = message.chat.id
    post_id = message.message_id
    caption = message.caption
    bot.edit_message_caption(chat_id=channel_id, message_id=post_id, caption=caption + '\n\n' + link, parse_mode='markdown')

bot.infinity_polling()
