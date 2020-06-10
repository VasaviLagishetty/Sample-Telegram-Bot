import telebot
API_TOKEN = 'Your API TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
  bot.reply_to(message, "\nHi there, I am SampleDemoBot.\nI am here to repeat your words. Just send anything  and I'll send the same thing to you!\n")
  
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  bot.reply_to(message, message.text)
  
bot.polling()