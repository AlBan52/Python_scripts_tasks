# ProgressBarBot

This code helps you to visual countdown timer in Telegram chat.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
You need to copy ptbot.py in current directory

### How to use

To start use this code, you need to create your own environment file .env in current directory.
This file must have the next data:
```
TOKEN=1108388680:AAHVOSKmpcyQxUcPdkEo44u_94Gu8HZOs6A
CHAT_ID=741843936
```
Then you run this code, you'l see in Telegram chat and in the terminal the next message: "Бот запущен".
It means: "Bot started". The next message is the timer countdown request: "На сколько запустить таймер?"
It means: "How much seconds to start timer?" The answer on this request must have the next attributes: "10s"
Where 10 - seconds amount; s - seconds indicator

### Output results

As results you get visual progress bar in percent.
Also you'll see the message with last seconds: "Осталось секунд: 3".
It means: "Seconds left: 3"
When the time is up, the bot send the message: "Время вышло". It means: "Time is up"

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).