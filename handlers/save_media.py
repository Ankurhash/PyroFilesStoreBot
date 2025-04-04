# (c) @AbirHasan2005

import asyncio
from configs import Config
from handlers import linkshort
from handlers.remove_word import rmw
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.copy(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)


async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        message_cap =""
        i = 1
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            cap01 = sent_message.caption
            if cap01:
                cap = await rmw(cap01)
                if cap != cap01:
                    await bot.edit_message_caption(Config.DB_CHANNEL,sent_message.id,f"{cap}")
            else:
                cap = "file don't have caption 🤥"
            message_cap += f"<b>{i}</b>: {cap}\n\n"
            i += 1
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Delete Batch", callback_data="closeMessage")
            ]])
        )
        if Config.SHORTNER_API_LINK and Config.SHORTNER_API:
            share_link = await linkshort.Short(f"https://t.me/{Config.BOT_USERNAME}?start=storebot_{str_to_b64(str(SaveMessage.id))}")
        else:
            share_link = f"https://t.me/{Config.BOT_USERNAME}?start=storebot_{str_to_b64(str(SaveMessage.id))}"
        #share_link = f"https://t.me/{Config.BOT_USERNAME}?start=storebot_{str_to_b64(str(SaveMessage.id))}"
        await editable.edit(
            #f"**Batch Files Stored in my Database!**\n\n
            f"Here is the Permanent Link of your files: {share_link} \n\n"
            f"<b><i>Just Click the link to get your files!</i></b>\n\n"
            f"<b>your files name are:👇</b> \n\n <i>{message_cap}</i>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Open Link", url=share_link)],
                 [InlineKeyboardButton("Bots Channel", url="https://t.me/"),
                  InlineKeyboardButton("Support Group", url="https://t.me/")]]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) Got Batch Link!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open Link", url=share_link)]])
        )
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.copy(Config.DB_CHANNEL)
        cap01 = forwarded_msg.caption
        if cap01:
            cap = await rmw(cap01)
            if cap != cap01:
                await bot.edit_message_caption(Config.DB_CHANNEL,forwarded_msg.id,f"{cap}")
        else:
            cap = "file don't have any caption 😟"
        file_er_id = str(forwarded_msg.id)           
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            disable_web_page_preview=True)
        if Config.SHORTNER_API_LINK and Config.SHORTNER_API:
            share_link = await linkshort.Short(f"https://t.me/{Config.BOT_USERNAME}?start=storebot_{str_to_b64(file_er_id)}")
        else:
            share_link = f"https://t.me/{Config.BOT_USERNAME}?start=storebot_{str_to_b64(file_er_id)}"
        #share_link = f"https://t.me/{Config.BOT_USERNAME}?start=storebot_{str_to_b64(file_er_id)}"
        await editable.edit(
            #"**Your File Stored in my Database!**\n\n"
            f"Here is the Permanent Link of your file: {share_link} \n\n"
            "<i><b>Just Click the link to get your file!</b></i> \n\n"
            f"<b>your file name is 👇</b>:\n\n<i>{cap}</i>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Open Link", url=share_link)],
                 [InlineKeyboardButton("Bots Channel", url="https://t.me/"),
                  InlineKeyboardButton("Support Group", url="https://t.me/")]]
            ),
            disable_web_page_preview=True
        )
    except FloodWait as sl:
        if sl.value > 45:
            print(f"Sleep of {sl.value}s caused by FloodWait ...")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
