from random import choice

import telebot

bot = telebot.TeleBot('insert_your_token_here')

FILE_ANSWERS = 'razumbot_answers.txt'


def get_answers():
    all_answers = []
    for line in open(FILE_ANSWERS, 'r', encoding='utf-8'):
        all_answers.append(line)
    return all_answers


@bot.message_handler(commands=["start"])
def start(message, res=False):
    start_text = ('Просто добавь бота как обычного пользователя в любой '
                  'групповой чат, где присутствует бот Зайчатки Разума'
                  '(@olobot).')
    username = str(message.from_user.username)
    bot.send_message(message.chat.id,
                     f'Приветствую, @{username}! {start_text}')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.chat.type == "private":
        request_text = ('Этот бот не умеет отвечать в личных сообщениях. '
                        'Для дальнейшего взаимодействия добавьте его в '
                        'групповой чат.')
        bot.send_message(message.chat.id, request_text)
    else:
        username = str(message.from_user.username)
        if username == 'olobot':
            request_text = choice(get_answers())
            bot.reply_to(message, request_text)


bot.polling(none_stop=True, interval=0)
