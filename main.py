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
		if str(dict_of_sadness[user_id])[len(str(dict_of_sadness[user_id])) - 2:] in \
				['1', '5', '6', '7', '8', '9', '11', '12', '13', '14', '15', '16', '17', '18', '19']\
				or str(dict_of_sadness[user_id])[-1] == '0':
			word = 'раз'
		else:
			word = 'раза'
		bot.send_message(message.chat.id, '@{} Вы уже грустили {} {}.'.format(username, dict_of_sadness[user_id], word))


if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)