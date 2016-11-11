import config
import telebot
from slacker import Slacker

slack = Slacker(config.slacktoken)
bot = telebot.TeleBot(config.teletoken)
slack_channel_name = '#' + input('Set Slack channel name (without #): ')
print('Bot still working...')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Yes, I'm here")


@bot.message_handler(content_types=['text'])
def to_console(message):
    try:
        N = message.from_user.username
        Q = message.text
        answer = (N+': '+Q)
        print(answer)
        slack.chat.post_message(slack_channel_name, answer)
    except Exception:
        print('emodzi!!!')
        slack.chat.post_message(slack_channel_name, 'incorrect symbols')


@bot.message_handler(content_types=['image', 'photo','text'])
def handle_docs_audio(message):
    try:
        N = message.from_user.username
        C = message.caption
        answer = (N+': ***.jpeg '+C)
        slack.chat.post_message(slack_channel_name, answer)
        print(answer)
    except Exception:
        slack.chat.post_message(slack_channel_name, 'little pretty error')

if __name__ == '__main__':
    bot.polling(none_stop=True)
