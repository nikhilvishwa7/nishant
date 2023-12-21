import time
import random
from pyrogram import Client, filters

PHOTO = [
    "https://telegra.ph/file/d2a23fbe48129a7957887.jpg",
    "https://telegra.ph/file/ddf30888de58d77911ee1.jpg",
    "https://telegra.ph/file/268d66cad42dc92ec65ca.jpg",
    "https://telegra.ph/file/13a0cbbff8f429e2c59ee.jpg",
    "https://telegra.ph/file/bdfd86195221e979e6b20.jpg",
]

lucy = [
    [
        InlineKeyboardButton(text="ɴᴏᴏʙ", url=f"https://t.me/sewxiy"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="➕ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕",
            url=f"http://t.me/Lucy_Filter_bot?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.2)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        PICS,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[𝐋ᴜᴄʏ](f"t.me/Lucy_Filter_bot")』**
    ABOUT_TXT = """
<b>‣ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/{}">ʙᴏᴛ</a>
‣ ᴄʀᴇᴀᴛᴏʀ : <a href="https://t.me/xenxv">мɪкєʏ</a>
‣ ʟɪʙʀᴀʀʏ : <a href="https://pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ</a>
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
‣ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
‣ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/teamanteiku">ᴠᴘs</a>
‣ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ : ᴠ3.7.1 [ꜱᴛᴀʙʟᴇ]</b>

‣ ᴀʟʟ ᴄʀᴇᴅɪᴛs​: <a href='https://t.me/team_netflix'>ᴍɪᴋᴇʏ</a></b>"""
   ━━━━━━━━━━━━━━━━━━━
        reply_markup=InlineKeyboardMarkup(lucy),
    )
