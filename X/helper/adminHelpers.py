import asyncio
from time import time

from pyrogram.types import Message

from pyrogram import Client 
from X.helper.interval import IntervalHelper


async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await Client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ!__!")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__ɴᴏ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴛᴏ ʀᴇꜱᴛʀɪᴄᴛ ᴍᴇᴍʙᴇʀꜱ__")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit("ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ɴᴇᴇᴅꜱ ᴛᴏ ʙᴇ ᴀ ʀᴇᴘʟʏ")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"ɪ ᴄᴀɴ'ᴛ {message.command[0]} ᴍʏꜱᴇʟꜰ.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"ɪ ᴄᴀɴ'ᴛ {message.command} ᴛʜɪꜱ ᴜꜱᴇʀ.")
    await asyncio.sleep(2)
    await message.delete()
