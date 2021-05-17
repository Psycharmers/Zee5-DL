import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from script import script

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["help"]))
def help_user(bot, update):

    bot.send_message(
        chat_id=update.chat.id,
        text=script.HELP_USER,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Nexon Projects ❤", url="https://t.me/NexonHex")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["start"]))
def send_start(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=script.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Projects", url="https://t.me/NexonHex")], [InlineKeyboardButton(text="SUPPORT", url="https://t.me/NexonHex_grp"),
                                                    InlineKeyboardButton(text="SHARE ♐️", url="tg://msg?text=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%20%0A__Today%20i%20just%20found%20out%20an%20intresting%20and%20Powerful__%20%2A%2AZee5%20Downloader%20Bot%2A%2A%20__for%20Free%F0%9F%A5%B0.__%20%20%0A%2A%2ABot%20Link%20%3A%20%40Zee5dl_robot%2A%2A%20%F0%9F%94%A5")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["upgrade"]))
def upgrade(bot, update):

    bot.send_message(
        chat_id=update.chat.id,
        text=script.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@Client.on_message(filters.command(["about"]))
def about(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=script.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    ) 
        
                
