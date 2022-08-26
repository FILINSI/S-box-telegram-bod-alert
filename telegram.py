import telebot
from telebot import types 
import time
bot = telebot.TeleBot('5633233488:AAHeDekLTlhSql0qRFS2Y5tzxVVZ8ZMYPak')
 
@bot.message_handler(commands=['start'])
def button(message):
    
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("own" ) 
    item2 = types.KeyboardButton("two" )
    item3 = types.KeyboardButton("three" )

    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, "Привет, я бот, не пытайтесь со мной разговаривать.Все, что я могу сделать, это информировать об обновлениях сайта и раздаче ключей S&box", reply_markup=markup)
    bot.send_message(message.chat.id, "Hi, I'm a bot, don't try to talk to me. All I know how to do is notify about site updates and S&box key giveaways" , reply_markup=markup)
    

bot.polling(none_stop=True) 
