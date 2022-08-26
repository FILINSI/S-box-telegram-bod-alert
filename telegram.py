import telebot
from telebot import types
import logging

from sqldb import sqldb



TOKEN = '5633233488:AAHeDekLTlhSql0qRFS2Y5tzxVVZ8ZMYPak'

bot = telebot.TeleBot(TOKEN)


#логгирование в файл
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)  # DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename='bot.log', level=logging.INFO)
logger.setLevel(logging.DEBUG)

#база данных SQLite

db = sqldb("subscriptions.db")

#команда подписки
@bot.message_handler(commands=['subscribe'])
async def subscribe(message):
    if not db.subscriber_exists(message.chat.id):
        db.add_subscriber(message.chat.id, message.chat.first_name)
    else:
        db.update_subscriber(message.chat.id, message.chat.first_name)
    await bot.send_message(message.chat.id, "Вы успешно подписались на рассылку!/You have successfully subscribed to the newsletter!")  # подписка прошла успешно

#команда отписки
@bot.message_handler(commands=['unsubscribe'])
async def unsubscribe(message):
    if not db.subscriber_exists(message.chat.id):
        await bot.send_message(message.chat.id, "Вы и так не подписаны/You are already unsigned.")
        return
    else:
        db.remove_subscriber(message.chat.id)
        await bot.send_message(message.chat.id, "Вы успешно отписались от рассылки/you have successfully unsubscribed")



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
        markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
        btn1 = types.KeyboardButton('обновление')
        btn2 = types.KeyboardButton('раздача')
        btn3 = types.KeyboardButton('автор')
        btn4 = types.KeyboardButton('подписаться')
        btn5 = types.KeyboardButton('отписаться')
        btn4 = types.KeyboardButton('назад/Escape')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(
            message.chat.id, 'Привет, я бот, не пытайтесь со мной разговаривать. Все, что я могу сделать, это информировать об обновлениях сайта и раздаче ключей S&box', reply_markup=markup)
    elif message.text == 'автор':
        bot.send_message(message.chat.id, 'Автор бота  - @FilinSi')
        bot.send_message(message.chat.id, 'Версия бота - 0.3')
        bot.send_message(
            message.chat.id, 'ETH/BTC/BNB/BUSD - 0xbfe5A7fe19B93f538400BC60741B46d13D50CbC6')
        bot.send_message(message.chat.id, 'Приятного использования!')
    elif message.text == 'назад/Escape':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton('🇺🇸 English')
        btn2 = types.KeyboardButton('🇷🇺 Русский')
        btn3 = types.KeyboardButton('Назад/Escape')
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            message.chat.id, 'Выберете язык\Select a language ', reply_markup=markup)
    elif message.text == 'обновление':
        bot.send_message(message.chat.id, 'Обновление было 64 минуты назад')
    elif message.text == 'раздача':
        bot.send_message(message.chat.id, 'Раздача была 23 минуты назад')
# Script after language selection
# Russian
    elif message.text == '🇺🇸 English':
        markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
        btn1 = types.KeyboardButton('upd')
        btn2 = types.KeyboardButton('give')
        btn3 = types.KeyboardButton('author')
        btn4 = types.KeyboardButton('subscribe')
        btn5 = types.KeyboardButton('unsubscribe')
        btn4 = types.KeyboardButton('назад/Escape')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(
            message.chat.id, 'Hi, Im a bot, dont try to talk to me. All I can do is inform you about site updates and S&box key giveaways', reply_markup=markup)

    elif message.text == 'author':
        bot.send_message(message.chat.id, 'Bot author  - @FilinSi')
        bot.send_message(message.chat.id, 'Bot version - 0.3')
        bot.send_message(
            message.chat.id, 'ETH/BTC/BNB/BUSD - 0xbfe5A7fe19B93f538400BC60741B46d13D50CbC6')
        bot.send_message(message.chat.id, 'Enjoy your use!')
    elif message.text == 'назад/Escape':
        bot.send_message(message.chat.id, '/start')
    elif message.text == 'upd':
        bot.send_message(
            message.chat.id, 'The site was updated 64 minutes ago')
    elif message.text == 'give':
        bot.send_message(message.chat.id, 'It was distributed 23 minutes ago')
    else:
        bot.send_message(message.chat.id, 'i dont understand you')


bot.polling(none_stop=True)
