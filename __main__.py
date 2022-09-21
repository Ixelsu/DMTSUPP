# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Dmt-PyroBot

from pyrogram import idle
from uvloop import install

from config import BOT_VER
from Dersu import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from Dersu.helpers.misc import create_botlog, git, heroku

MSG_ON = """
✅ **Dmt-supp Activated.**
**🏷️ Userbot Version -** `{}`
**Ketik** `.dersu` **untuk Mengecheck Bot**
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("Lunatic0de")
            await bot.join_chat("SharingUserbot")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER)
                )
            except BaseException:
                pass
            LOGGER("Dersu").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Dersu").info(f"Dmt-supp v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Dersu").info("Starting Cilik-Ubot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
