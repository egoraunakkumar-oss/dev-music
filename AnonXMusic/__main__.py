import asyncio
import importlib

from pyrogram import idle
import config
from AnonXMusic import LOGGER, app, userbot
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    # Register every handler before starting the Pyrogram client. Starting the
    # client first can leave the dispatcher without command handlers, making
    # /start and /play appear to be ignored.
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("AnonXMusic.plugins").info("Successfully Imported Modules...")
    await app.start()
    LOGGER("AnonXMusic").info("Telegram bot client started; initializing assistants...")
    try:
        await userbot.start()
    except Exception:
        LOGGER(__name__).exception(
            "Assistant startup failed. Keeping the Telegram bot online so /start and diagnostics still work."
        )
    try:
        await Anony.start()
    except Exception:
        LOGGER(__name__).exception(
            "PyTgCalls startup failed. Keeping the Telegram bot online without voice-chat playback."
        )
    # Do not probe the logger chat with a voice-call stream here. A logger
    # group normally has no active voice chat, and treating that expected
    # condition as fatal causes Railway to restart the bot in a loop before
    # it reaches idle() and starts handling commands.
    try:
        await Anony.decorators()
    except Exception:
        LOGGER(__name__).exception("Could not register PyTgCalls update handlers.")
    LOGGER("AnonXMusic").info("Startup complete; waiting for Telegram updates.")
    try:
        await idle()
    finally:
        for component, name in (
            (Anony, "PyTgCalls"),
            (userbot, "assistants"),
            (app, "bot"),
        ):
            try:
                await component.stop()
            except Exception:
                LOGGER(__name__).exception("Error while stopping %s.", name)
        LOGGER("AnonXMusic").info("Stopping AnonX Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
