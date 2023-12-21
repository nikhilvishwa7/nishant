import asyncio
import os
from pyrogram import filters, enums, Client 
from Script import script

@Client.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def report_user(bot, message):
    if message.reply_to_message:
        await message.reply_chat_action("typing")
        k = await message.reply_text("**Processing...⏳**", quote=True)
        await bot.send_message(PM, A.format(message.from_user.first_name, message.from_user.username, message.from_user.id, message.from_user.mention, message.from_user.id))
        await message.reply_to_message.forward(chat_id=PM)
        await k.edit_text("**Thanks for Reporting.** ❤️\n..\n**I have forwarded your message to my Owner. He will reply you When ever he will be free. ✌️**")
    else:
        await message.reply_text("**Please Send me a message** and **Then Reply that message with __/report__ , so that I can report that to my Owner**")
