#This is a mirror bot. Anything that user sends, returning to him

from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('token')

bot = TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start_handle(message):
    """Robot introduce himself"""
    bot.send_message(chat_id=message.chat.id, text="Hello👋! I'm a mirror robot🤖. Anything you send, I will return it to you.")

@bot.message_handler(func=lambda m: True)
def echo_message(message):
    """Robot returning message text"""
    bot.send_message(chat_id=message.chat.id, text=message.text)

@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    """Robot returning photo"""
    photo = message.photo[-1].file_id
    bot.send_photo(chat_id=message.chat.id, photo=photo)

@bot.message_handler(content_types=['animation'])
def echo_animation(message):
    """Robot returning animation"""
    animation = message.animation.file_id
    bot.send_animation(chat_id=message.chat.id, animation=animation)

@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    """Robot returning sticker"""
    sticker = message.sticker.file_id
    bot.send_sticker(chat_id=message.chat.id, sticker=sticker)

@bot.message_handler(content_types=['video'])
def echo_video(message):
    """Robot returning video"""
    video = message.video.file_id
    bot.send_video(chat_id=message.chat.id, video=video)

@bot.message_handler(content_types=['voice'])
def echo_voice(message):
    """Robot returning voice"""
    voice = message.voice.file_id
    bot.send_voice(chat_id=message.chat.id, voice=voice)

@bot.message_handler(content_types=['document'])
def echo_document(message):
    """Robot returning document"""
    document = message.document.file_id
    bot.send_document(chat_id=message.chat.id, document=document)

print("bot is running...")
bot.infinity_polling()