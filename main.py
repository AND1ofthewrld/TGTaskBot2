import telebot
import configDE
from telebot import types
import requests
from io import BytesIO

bot = telebot.TeleBot(configDE.token)
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <b>{message.from_user.first_name} </b>, выберите что именно вам нужно, либо напишите текстом.'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Получить случайный медиафайл")
    item2 = types.KeyboardButton("Получить случайный аудиофайл")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text.lower() == 'репозиторий')
def ask_for_password(message):
    bot.send_message(message.chat.id, "Для доступа к репозиторию введите пароль:")
    bot.register_next_step_handler(message, check_password)

def check_password(message):
    user_input = message.text

    if user_input == "1234":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти в репозиторий", url="https://github.com/AND1ofthewrld/DeminTGBot"))
        bot.send_message(message.chat.id, "Пароль верный. Вот кнопка для перехода в репозиторий:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Пароль неверный. Попробуйте еще раз.")
@bot.message_handler(content_types='text')
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Получить случайный медиафайл':
            photo = configDE.get_random_photo()
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'Получить случайный аудиофайл':
            audio_url = configDE.get_random_audio()
            response = requests.get(audio_url)
            bot.send_chat_action(message.chat.id, 'upload_audio')
            bot.send_audio(message.chat.id, response.content, title='Аудио')

# @bot.message_handler(commands=['stop'])
# def stop(message):
#     bot.send_message(message.chat.id, 'Бот остановлен.')
#     exit()
#
bot.polling(none_stop=True)



