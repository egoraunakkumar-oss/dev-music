
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI")

# YouTube API
YTPROXY_URL = getenv(
    "YTPROXY_URL", ""
)
YT_API_KEY = getenv("YT_API_KEY")

# Duration
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))

# Logging & Owner
LOGGER_ID = int(getenv("LOGGER_ID", "0"))
OWNER_ID = int(getenv("OWNER_ID", "0"))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# GitHub
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/dipagsiXraunak/Developer-music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")

# Network & Updates
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/updatesxhub"
)
SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT", "https://t.me/aresxcores"
)

# Assistant
AUTO_LEAVING_ASSISTANT = (
    getenv("AUTO_LEAVING_ASSISTANT", "True").lower() == "true"
)
ASSISTANT_LEAVE_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", 5400)
)

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# Playlist
PLAYLIST_FETCH_LIMIT = int(
    getenv("PLAYLIST_FETCH_LIMIT", 25)
)

# Telegram File Limits
TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600)
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824)
)

PRIVATE_BOT_MODE_MEM = int(
    getenv("PRIVATE_BOT_MODE_MEM", 1)
)

# Cache
CACHE_DURATION = int(getenv("CACHE_DURATION", 86400))
CACHE_SLEEP = int(getenv("CACHE_SLEEP", 3600))

# Assistant String Sessions
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# Other Variables
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
file_cache: dict[str, float] = {}

# Images
START_IMG_URL = [
    "https://te.legra.ph/file/5fd13f2cc0d03bce9f7f2.jpg",
    "https://te.legra.ph/file/c15d01b3e6b40ea141dc9.jpg",
    "https://te.legra.ph/file/5fd13f2cc0d03bce9f7f2.jpg",
]

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/87f680aead03443f291b0.jpg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
STATS_IMG_URL = "https://telegra.ph/file/edd388a42dd2c499fd868.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
STREAM_IMG_URL = "https://graph.org/file/ff2af8d4d10afa1baf49e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(DURATION_LIMIT_MIN * 60)

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL must start with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHAT must start with https://"
        )
