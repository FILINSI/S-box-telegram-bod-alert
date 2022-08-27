import telebot
from telebot import types
import logging
from server import Server
from parcer import Parcer

TOKEN = 'Token'

bot = telebot.TeleBot(TOKEN)
# логгирование в файл
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)  # DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename='bot.log', level=logging.INFO)
logger.setLevel(logging.DEBUG)

# подключаемся к БД
server = Server('bot.db')

# Команда активации подписки
@bot.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if(not server.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его
		server.add_subscriber(message.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		server.update_subscription(message.from_user.id, True)
	
	await message.answer("Вы успешно подписались на рассылку! ")

# Команда отписки
@bot.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if(not server.subscriber_exists(message.from_user.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
		server.add_subscriber(message.from_user.id, False)
		await message.answer("Вы итак не подписаны.")
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		server.update_subscription(message.from_user.id, False)
		await message.answer("Вы успешно отписаны от рассылки.")


#  Выбор языка при START
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('🇺🇸 English')
    btn2 = types.KeyboardButton('🇷🇺 Русский')
    markup.add(btn1, btn2,)
    bot.send_message(
        message.chat.id, 'Выберете язык\Select a language ', reply_markup=markup)
# Сценарий после выбора языка
# Русский


@bot.message_handler(content_types=['text'])
def start_categorial(message):
    if message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn1 = types.KeyboardButton('Последнее обновление сайта🔧')
        btn2 = types.KeyboardButton('Последняя раздача ключей 🔑')
        btn3 = types.KeyboardButton('Автор 📕')
        btn4 = types.KeyboardButton('Назад/Escape ➡️')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(
            message.chat.id, 'Привет, я бот, не пытайтесь со мной разговаривать. Все, что я могу сделать, это информировать об обновлениях сайта и раздаче ключей S&box', reply_markup=markup)
    elif message.text == 'Автор 📕':
        bot.send_message(message.chat.id, 'Автор бота  - @FilinSi')
        bot.send_message(message.chat.id, 'Версия бота - 0.3')
        bot.send_message(
            message.chat.id, 'ETH/BTC/BNB/BUSD - 0xbfe5A7fe19B93f538400BC60741B46d13D50CbC6')
        bot.send_message(message.chat.id, 'Приятного использования!')
    elif message.text == 'Назад/Escape ➡️':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton('🇺🇸 English')
        btn2 = types.KeyboardButton('🇷🇺 Русский')
        btn3 = types.KeyboardButton('Назад/Escape ➡️')
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            message.chat.id, 'Выберете язык\Select a language ', reply_markup=markup)
    elif message.text == 'Последнее обновление сайта🔧':
        bot.send_message(message.chat.id, 'В разработке😋')
    elif message.text == 'Последняя раздача ключей 🔑':
        bot.send_message(message.chat.id, 'В разработке😋')
# Script after language selection
# Russian
    elif message.text == '🇺🇸 English':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn1 = types.KeyboardButton('Last web update 🔧')
        btn2 = types.KeyboardButton('Last giveaway 🔑')
        btn3 = types.KeyboardButton('Author 📕')
        btn4 = types.KeyboardButton('Назад/Escape ➡️')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(
            message.chat.id, 'Hi, Im a bot, dont try to talk to me. All I can do is inform you about site updates and S&box key giveaways', reply_markup=markup)

    elif message.text == 'Author 📕':
        bot.send_message(message.chat.id, 'Bot author  - @FilinSi')
        bot.send_message(message.chat.id, 'Bot version - 0.3')
        bot.send_message(
            message.chat.id, 'ETH/BTC/BNB/BUSD - 0xbfe5A7fe19B93f538400BC60741B46d13D50CbC6')
        bot.send_message(message.chat.id, 'Enjoy your use!')
    elif message.text == 'Назад/Escape ➡️':
        bot.send_message(message.chat.id, '/start')
    elif message.text == 'Last web update 🔧':
        bot.send_message(
            message.chat.id, 'in the works😋')
    elif message.text == 'Last giveaway 🔑':
        bot.send_message(message.chat.id, 'in the works😋')
    else:
        bot.send_message(message.chat.id, 'i dont understand you')
    


bot.polling(none_stop=True)
