import os, asyncio
from xgorn_api import NoidAPI
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Environments / Configs
API_HASH = os.environ.get('API_HASH', '')
APP_ID = int(os.environ.get('APP_ID', ''))
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'abc;123')
API_KEY = os.environ.get('API_KEY', 'AIzaSyAjlZfV8QfFmXRIyAdBfrqf2TdHHJgJ3o0')
OWNER_ID = os.environ.get('OWNER_ID', "6497757690")

# See Documentation for more details (api.xgorn.pp.ua/docs)
SAMPLER = os.environ.get('SAMPLER', 'k_euler_a')
MODEL = os.environ.get('MODEL', 'anime')
GENDER = os.environ.get('GENDER', 'female')
NSFW = os.environ.get('NSFW', 'false')


api = NoidAPI()

api.api_key = API_KEY

# Helpers
def get_text(update) -> [None, str]:
    text_to_return = update.text
    if update.text is None:
        return None
    if " " in text_to_return:
        try:
            return update.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


# Running bot
xbot = Client('Anime-Ai', api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Generating
@xbot.on_message(filters.command('animeai') & filters.private)
async def _animeai(bot, update):
    prompt = get_text(update)
    if prompt:
        x = await update.reply('Wait for 10~20 seconds..')
        await bot.send_chat_action(update.from_user.id, enums.ChatAction.UPLOAD_PHOTO)
        result = api.make_request('post', '/ai/silmin_generate', prompt=prompt, sampler=SAMPLER, gender=GENDER, model=MODEL, nsfw=NSFW)
        if not result['error']:
            count = 1
            while True:
                await asyncio.sleep(10)
                task = api.make_request('post', '/ai/silmin_task', task_id=result['task_id'])
                if not task['error']:
                    break
                else:
                    if count > 5:
                        break
                    count+=1
            await x.delete()
            await update.reply_photo(task['image'])
        else:
            await x.edit(result['message'])


xbot.run()
