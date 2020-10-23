import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse

load_dotenv()
token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')

bot = ptbot.Bot(token)
bot.send_message(chat_id, "Бот запущен")
print('Бот запущен')
bot.send_message(chat_id, 'На сколько запустить таймер?')


def bot_reply(user_time_message):
    seconds = parse(user_time_message)
    bot_message_to_chat = 'Таймер запущен на {} секунд'.format(seconds)
    bot.create_timer(seconds, end_of_time)
    print(bot_message_to_chat)
    bot.send_message(chat_id, bot_message_to_chat)
    bot.create_countdown(seconds, notify_progress, message_id=bot.send_message(chat_id, bot_message_to_chat),
                         seconds=seconds)


def end_of_time():
    bot_end_to_chat = 'Время вышло'
    bot.send_message(chat_id, bot_end_to_chat)


def notify_progress(secs_left, message_id, seconds):
    secs_left_to_chat = "Осталось секунд: {0} \n {1}".format(secs_left, render_progressbar(seconds, secs_left))
    bot.update_message(chat_id, message_id, secs_left_to_chat)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    progbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, progbar, percent, suffix)


bot.reply_on_message(bot_reply)


bot.run_bot()

