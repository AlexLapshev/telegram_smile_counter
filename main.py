import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

dict_of_sadness = {}
search = ':('


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if search in message.text:
		num = message.text.count(search)
		user_id = message.from_user.id
		username = message.from_user.username
		bot.reply_to(message, 'Опять грустим?')
		dict_of_sadness.setdefault(user_id, 0)
		dict_of_sadness[user_id] += num
		bot.send_message(message.chat.id, '@{} вы уже грустили {} раза.'.format(username, dict_of_sadness[user_id]))


if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)