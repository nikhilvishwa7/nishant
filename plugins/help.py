import os
from pyrogram.errors import ChatAdminRequired, FloodWait
import random
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import enums, filters, Client
from info import API_ID, API_HASH, BOT_TOKEN, PORT, ADMINS, LOG_CHANNEL, DATABASE_NAME, DATABASE_URI, S_GROUP, S_CHANNEL
from Script import script
import time
from utils import temp
from pyrogram.errors import FloodWait
from database.users_chats_db import db
import re
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command("support"))
async def support_command(client, message):
    buttons = [
        [
            InlineKeyboardButton("📢 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ", url=S_GROUP),
            InlineKeyboardButton("📢 sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url=S_CHANNEL)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=script.SUPPORT_TXT, reply_markup=reply_markup)

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    buttons = [[
            InlineKeyboardButton('📕 ᴍᴀɴᴀɢᴇᴍᴇɴᴛ', callback_data='management'),
            InlineKeyboardButton('ᴀʟʟ ᴄᴍɴᴅs ❍', callback_data='help')
         ], [
            InlineKeyboardButton('💁 ʙᴀsɪᴄ', callback_data='basic_help'),
            InlineKeyboardButton('ᴇxᴘᴇʀᴛ 👮', callback_data='expert_help')
         ], [
            InlineKeyboardButton('🍹 sᴜᴘᴘᴏʀᴛ', callback_data='group_info'),
            InlineKeyboardButton('ᴅᴏɴᴀᴛɪᴏɴ  🎉', callback_data='donate')
         ], [
            InlineKeyboardButton('• ᴄʟᴏsᴇ •', callback_data='close')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id,
            query.message.id,
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        await query.message.edit_text(
            text=script.MAIN_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ', callback_data='stats')
        ], [
            InlineKeyboardButton('ꜰɪʟᴛᴇʀꜱ', callback_data='filters'),
            InlineKeyboardButton('ꜰɪʟᴇ ꜱᴛᴏʀᴇ', callback_data='store_file'),
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜ', callback_data='tele')     
        ], [
            InlineKeyboardButton('ꜱᴇᴛᴛɪɴɢꜱ', callback_data='settings'),
            InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛɪᴏɴ', callback_data='coct'),
            InlineKeyboardButton('ᴇxᴛʀᴀ ᴍᴏᴅꜱ', callback_data='extra')
        ], [
            InlineKeyboardButton('ꜰᴏɴᴛ', callback_data='font'),
            InlineKeyboardButton('ꜱᴛɪᴄᴋᴇʀ', callback_data='sticker'),
            InlineKeyboardButton('ʀᴜʟᴇꜱ', callback_data='rule')
         ], [
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
            InlineKeyboardButton('ɴᴇxᴛ', callback_data='help1')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id,
            query.message.id,
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "help1":
        buttons = [[
            InlineKeyboardButton('ʏᴛ-ᴛʜᴜᴍʙ', callback_data='ytthumb'),
            InlineKeyboardButton('ʏᴛ-ᴠɪᴅ', callback_data='video'),
            InlineKeyboardButton('ʏᴛ-ᴛᴀɢꜱ', callback_data='yttags')
         ], [
            InlineKeyboardButton('ᴏᴡɴᴇʀ', callback_data='mikey'),
            InlineKeyboardButton('ᴅᴏɴᴀᴛɪᴏɴ', callback_data='donate'),
            InlineKeyboardButton('ɢɪᴛʜᴜʙ', callback_data='github')
         ], [
            InlineKeyboardButton('ᴋᴀɴɢ', callback_data='kang'),
            InlineKeyboardButton('ʀᴇᴘᴏʀᴛ', callback_data='report'),
            InlineKeyboardButton('ɢᴇɴ-ᴘᴀss', callback_data='gen_pass')
        ], [
            InlineKeyboardButton('ᴏᴘᴇɴᴀɪ', callback_data='opnai'),
            InlineKeyboardButton('sᴀᴀᴠɴ', callback_data='song'),
            InlineKeyboardButton('ᴘᴜʀɢᴇ', callback_data='purge')
        ], [
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
            InlineKeyboardButton('ɴᴇxᴛ', callback_data='help2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id,
            query.message.id,
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "help2":
        buttons = [[
            InlineKeyboardButton('ᴘɪɴɢ', callback_data='alive'),
            InlineKeyboardButton('ᴄᴀʀʙᴏɴ', callback_data='carbon'),
            InlineKeyboardButton('ʀᴇᴘᴏ', callback_data='repo')
         ], [
            InlineKeyboardButton('ᴊsᴏɴ', callback_data='json'),
            InlineKeyboardButton('ʟʏʀɪᴄs', callback_data='lyrics'),
            InlineKeyboardButton('sʜᴏʀᴛɴᴇʀ', callback_data='shortner')
         ], [
            InlineKeyboardButton('ᴛᴏʀʀᴇɴᴛ', callback_data='torrent'),
            InlineKeyboardButton('ᴍᴜᴛᴇ', callback_data='restrict'),
            InlineKeyboardButton('ᴋɪᴄᴋ', callback_data='kick')
        ], [
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help1'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
            InlineKeyboardButton('ꜱᴘᴇᴄɪᴀʟ', callback_data='special')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        await query.message.edit_text(
            text=script.SPECIAL_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "special":
        buttons = [[
            InlineKeyboardButton('ꜱᴘᴇᴄɪᴀʟ ᴍᴏᴅ1', callback_data='special_mod1'),
            InlineKeyboardButton('ꜱᴘᴇᴄɪᴀʟ ᴍᴏᴅ2', callback_data='special_mod2'),
            InlineKeyboardButton('ᴇxᴛʀᴀ ᴍᴏᴅ', callback_data='extra_mod')
        ], [
            InlineKeyboardButton('⇍ ʙᴀᴄᴋ ⇏', callback_data='help2')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.SPECIAL_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "special_mod1":
        buttons = [[
            InlineKeyboardButton('⇍ ʙᴀᴄᴋ ⇏', callback_data='special')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.SPECIAL_MOD1,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "special_mod2":
        buttons = [[
            InlineKeyboardButton('⇍ ʙᴀᴄᴋ ⇏', callback_data='special')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.SPECIAL_MOD2,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "extra_mod":
        buttons = [[
            InlineKeyboardButton('⇍ ʙᴀᴄᴋ ⇏', callback_data='special')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.EXTRA_MOD,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )


        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('❗❗ ᴅɪꜱᴄʟᴀɪᴍᴇʀ ❗❗', callback_data='disclaimer')
        ], [
            InlineKeyboardButton('ᴇᴀʀɴ ᴍᴏɴᴇʏ', callback_data='source'),
            InlineKeyboardButton('ᴅᴏɴᴀᴛᴇ', callback_data='donate')
        ],[
            InlineKeyboardButton('• ᴄʟᴏsᴇ •', callback_data='close')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "disclaimer":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ ⇋', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.DISCLAIMER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "sticker":
            buttons = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help"),
                    InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(script.STICKER_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )  
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('⇇ ʙᴀᴄᴋ', callback_data='filters'),
            InlineKeyboardButton('ʙᴜᴛᴛᴏɴꜱ', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ ⇋', callback_data='manuelfilter')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('⇋ ʙᴀᴄᴋ ⇋', callback_data='filters')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('⇇ ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('ᴀᴅᴍɪɴ', callback_data='admin')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "store_file":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.FILE_STORE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='extra'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "tele":
            buttons = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help"),
                    InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(script.TELEGRAPH_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
    elif query.data == "settings":
            buttons = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help"),
                    InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(script.SETTINGS_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
    elif query.data == "rule":
            buttons = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help"),
                    InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(script.RULE_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
    elif query.data == "ytthumb":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.YTTHUMB,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "video":
            buttons = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help")
                    InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(script.VIDEO_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
    elif query.data == "yttags":
            buttons = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help"),
                    InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(script.YTTAGS),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
    elif query.data == "mikey":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.MIKEY,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "donate":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.DONATE,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "github":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.GITHUB,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "kang":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.KANG,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "report":
            buttons = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help"),
                    InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
                  ]]
            await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(script.REPORT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
    elif query.data == "gen_pass":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.GEN_PASS,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "opnai":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help1'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.OPNAI_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "song":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help1'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.SONG_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "purge":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help1'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.PURGE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "alive":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.ALIVE,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "carbon":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.CARB_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "repo":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.REPO,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "json":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.JSON_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "lyrics":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.LYRICS,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "shortner":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.SHORTNER,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "torrent":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.TORRENT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "restrict":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.RESTRIC_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "kick":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='help2'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.ZOMBIES_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "management":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='main'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.MANAGEMENT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "basic_help":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='main'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.BASIC_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "expert_help":
        buttons = [[
            InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='main'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', callback_data='group_info')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text="● ◌ ◌"
        )
        await query.message.edit_text(
            text="● ● ◌"
        )
        await query.message.edit_text(
            text="● ● ●"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.EXPERT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "group_info":
        buttons = [[
            InlineKeyboardButton('× ᴀʟʟ ᴏᴜʀ ʟɪɴᴋꜱ ×', url="https://t.me/Team_Netflix/33")
       ],[
            InlineKeyboardButton('• ɢʀᴏᴜᴘ •', url="t.me/movie7xchat"),
            InlineKeyboardButton('• ᴜᴘᴅᴀᴛᴇs •', url="t.me/team_netflix")
       ],[
            InlineKeyboardButton('• sᴇʀɪᴇsғʟɪx •', url="https://t.me/+fAjYIpR5Ju02M2Q1"),
            InlineKeyboardButton('• ᴍᴏᴠɪᴇғʟɪx •', url="https://t.me/+KeFIjHXhzLMyMWZl")
       ],[
            InlineKeyboardButton('• ᴋᴏʀᴇᴀɴ ᴅʀᴀᴍᴀs •', url="https://t.me/+EjBZ70D4ha8wNWY9")
       ],[ 
            InlineKeyboardButton('• ᴄʟᴏsᴇ •', callback_data='close')
        ]]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GROUP_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == 'close':
        await query.message.delete()
        edited_keyboard = InlineKeyboardMarkup([])
        await query.answer()
        await query.message.edit_reply_markup(edited_keyboard)
