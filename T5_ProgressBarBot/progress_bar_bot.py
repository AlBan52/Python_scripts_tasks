import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse
import time

load_dotenv()
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def bot_reply(user_time_message):
    seconds = parse(user_time_message)
    bot_message_to_chat = 'Таймер запущен на {} секунд'.format(seconds)
    bot.create_timer(seconds, end_of_time)
    bot.send_message(CHAT_ID, bot_message_to_chat)
    bot.create_countdown(seconds, notify_progress, message_id=bot.send_message(CHAT_ID, bot_message_to_chat),
                         seconds=seconds)


def end_of_time():
    bot_end_to_chat = 'Время вышло'
    time.sleep(0.5)
    bot.send_message(CHAT_ID, bot_end_to_chat)


def notify_progress(secs_left, message_id, seconds):
    secs_left_to_chat = "Осталось секунд: {0} \n {1}".format(secs_left, render_progressbar(seconds, secs_left))
    bot.update_message(CHAT_ID, message_id, secs_left_to_chat)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    progbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, progbar, percent, suffix)


if __name__ == '__main__':
    bot = ptbot.Bot(TOKEN)
    bot.send_message(CHAT_ID, "Бот запущен")
    bot.send_message(CHAT_ID, 'На сколько запустить таймер?')
    bot.reply_on_message(bot_reply)
    bot.run_bot()
