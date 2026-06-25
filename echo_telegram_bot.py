from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('token')

bot = TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start_handle(message):
    bot.send_message(chat_id=message.chat.id, text="سلام. من ربات آیینه هستم. هرچی شما بگید، منم همونو می گم.")

@bot.message_handler(func=lambda m: True)
def echo_message(message):
    bot.send_message(chat_id=message.chat.id, text=message.text)

@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    photo = message.photo[-1].file_id
    bot.send_photo(chat_id=message.chat.id, photo=photo)

@bot.message_handler(content_types=['animation'])
def echo_animation(message):
    animation = message.animation.file_id
    bot.send_animation(chat_id=message.chat.id, animation=animation)

@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    sticker = message.sticker.file_id
    bot.send_sticker(chat_id=message.chat.id, sticker=sticker)

@bot.message_handler(content_types=['video'])
def echo_video(message):
    video = message.video.file_id
    bot.send_video(chat_id=message.chat.id, video=video)

@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    voice = message.voice.file_id
    bot.send_voice(chat_id=message.chat.id, voice=voice)

@bot.message_handler(content_types=['document'])
def echo_document(message):
    document = message.document.file_id
    bot.send_document(chat_id=message.chat.id, document=document)

print("bot is running...")
bot.infinity_polling()