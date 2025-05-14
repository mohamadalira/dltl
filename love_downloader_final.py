from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

BOT_TOKEN = "7890752478:AAG2lEqrjSJtUsChNfna3C4XCueIaqpzQiA"

CHANNEL_USERNAME = "eshghabadi_twt"
FILE_CHANNEL_ID = -1002516050852

bot = Client("eshgheabadi_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    user_id = message.from_user.id
    args = message.text.split()

    try:
        member = await client.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception()
    except:
        await message.reply(
            "برای دریافت لینک دانلود، اول عضو کانال شو:",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/eshghabadi_twt")
            ]])
        )
        return

    if len(args) > 1:
        if args[1] == "ep1":
            sent = await client.forward_messages(
                chat_id=message.chat.id,
                from_chat_id=FILE_CHANNEL_ID,
                message_ids=[2]
            )
            await asyncio.sleep(30)
            await sent[0].delete()
        else:
            await message.reply("قسمت مورد نظر پیدا نشد.")
    else:
        await message.reply("سلام! برای دریافت قسمت‌ها روی لینک هر قسمت در کانال کلیک کن.")

bot.run()
