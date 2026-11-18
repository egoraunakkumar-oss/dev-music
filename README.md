<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,35:302b63,70:7c3aed,100:ec4899&height=220&section=header&text=DEV-MUSIC&fontSize=62&fontColor=ffffff&animation=twinkling&fontAlignY=42&desc=Telegram%20Voice%20Chat%20Music%20Bot&descAlignY=67&descSize=18&descColor=e2d9ff" alt="DEV-MUSIC — Telegram Voice Chat Music Bot" width="100%" />

<a href="https://t.me/Musicxdev_bot"><img src="https://img.shields.io/badge/TRY%20THE%20BOT-@Musicxdev__bot-A855F7?style=for-the-badge&logo=telegram&logoColor=white" alt="Open DEV-MUSIC bot" /></a>
<a href="https://t.me/aresxcores"><img src="https://img.shields.io/badge/SUPPORT-@aresxcores-0ea5e9?style=for-the-badge&logo=telegram&logoColor=white" alt="DEV-MUSIC support chat" /></a>
<a href="https://t.me/updatesxhub"><img src="https://img.shields.io/badge/UPDATES-@updatesxhub-16a34a?style=for-the-badge&logo=telegram&logoColor=white" alt="DEV-MUSIC updates channel" /></a>

[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Platform-Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://telegram.org/)
[![Kurigram](https://img.shields.io/badge/Client-Kurigram-7C3AED?style=flat-square)](https://github.com/delivrance/kurigram)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)](https://www.mongodb.com/)

</div>

---

**DEV-MUSIC** is a Python Telegram bot for playing music in group voice chats. It includes playback controls, queue management, playlist support, and assistant-account support. The public bot and community links below reflect this repository's current configuration; deployments can override the community links with environment variables.

> Runtime modules retain the `AnonXMusic` package name for compatibility. The public project branding is **DEV-MUSIC**.

## Features

- Play audio and video in Telegram group voice chats.
- Queue tracks and manage playback with pause, resume, skip, stop, loop, shuffle, seek, and speed controls.
- Play supported YouTube searches/links and playlists; other supported link sources include Spotify, SoundCloud, Apple Music, Resso, and Telegram media. Availability depends on the source and its current access restrictions.
- Use assistant user sessions for voice-chat playback. At least one assistant session is required at startup.
- Configure a support chat and an updates channel for the bot's in-chat buttons and support notices.

## Commands

Commands are primarily used in groups. Some controls also have channel-play variants; open `/help` in Telegram for the commands available to your deployment.

| Command | Purpose |
|---|---|
| `/play <song or link>` | Play a track or add it to the queue |
| `/vplay <song or link>` | Play video in the voice chat |
| `/pause` / `/resume` | Pause or resume playback |
| `/skip` | Skip the current track |
| `/stop` | Stop playback and clear the session |
| `/queue` | Show queued tracks |
| `/loop` | Toggle repeat playback |
| `/shuffle` | Shuffle the queue |
| `/seek <time>` | Seek within the current track |
| `/speed <value>` | Change playback speed |
| `/channelplay` | Configure channel playback |
| `/playmode` | Change playback mode |
| `/help` / `/settings` | Open help and bot settings |

## Requirements

- Python **3.13 or newer** (declared in `pyproject.toml`).
- FFmpeg available on the host for media processing.
- A Telegram bot token, Telegram API credentials, and a MongoDB database URI.
- One assistant account string session (`STRING_SESSION`; optional additional sessions are `STRING_SESSION2` through `STRING_SESSION5`).
- A Telegram chat/group ID for `LOGGER_ID` is recommended for startup/activity logs.

## Configuration

The application reads environment variables from a `.env` file in the working directory. Start by copying the included sample and filling in your own values:

```bash
cp sample.env .env
```

| Variable | Required | Description |
|---|---:|---|
| `API_ID` | Yes | Telegram API ID from [my.telegram.org](https://my.telegram.org/) |
| `API_HASH` | Yes | Telegram API hash from [my.telegram.org](https://my.telegram.org/) |
| `BOT_TOKEN` | Yes | Token created with [@BotFather](https://t.me/BotFather) |
| `MONGO_DB_URI` | Yes | MongoDB connection URI |
| `OWNER_ID` | Yes | Numeric Telegram user ID of the bot owner |
| `STRING_SESSION` | Yes | Session string for the first assistant user account |
| `LOGGER_ID` | Recommended | Numeric ID of a log group/channel where the bot can send messages |
| `SUPPORT_CHAT` | No | Support/community URL; defaults to `https://t.me/aresxcores` |
| `SUPPORT_CHANNEL` | No | Updates channel URL; defaults to `https://t.me/updatesxhub` |
| `STRING_SESSION2`–`STRING_SESSION5` | No | Additional assistant sessions |
| `SPOTIFY_CLIENT_ID` / `SPOTIFY_CLIENT_SECRET` | No | Optional Spotify API credentials for Spotify link metadata |

Keep `.env`, bot tokens, API credentials, database credentials, and user session strings private. Never commit them or paste them into a public issue or support chat. Use a dedicated assistant account where possible and protect its session string like a password.

## Run locally

Install [uv](https://docs.astral.sh/uv/) and Python 3.13+, then:

```bash
git clone https://github.com/egoraunakkumar-oss/dev-music.git
cd dev-music
cp sample.env .env
# Edit .env and fill in the required values.
uv sync
uv run python -m AnonXMusic
```

The repository also includes a `start` script. With `uv` installed, it runs the bot through the locked project environment:

```bash
./start
```

If FFmpeg is not already installed, install it with your operating system's package manager before starting the bot. The repository includes a `Dockerfile` and `Procfile` for deployment workflows; provide the same environment variables through your hosting platform's secret/environment-variable settings.

## Support and project links

| Purpose | Link |
|---|---|
| Bot | [@Musicxdev_bot](https://t.me/Musicxdev_bot) |
| Support chat | [@aresxcores](https://t.me/aresxcores) |
| Updates channel | [@updatesxhub](https://t.me/updatesxhub) |
| Maintainer contact | [@ik_zoro](https://t.me/ik_zoro) |
| Source code | [egoraunakkumar-oss/dev-music](https://github.com/egoraunakkumar-oss/dev-music) |

For a support request, include the command that failed and a short description of what happened. Remove private data first; never share tokens, API hashes, MongoDB URIs, or session strings.

## Contributing

Bug reports and focused pull requests are welcome. Before opening an issue, check whether the problem can be reproduced with the latest code and include relevant, redacted logs. Please do not publish secrets, private chat content, or copyrighted media.

## Disclaimer

This project is provided for personal/educational use. You are responsible for complying with Telegram's terms, the rules of each content provider, copyright law, and the laws applicable to your use. Source integrations may change or become unavailable without notice.

## License

See [`LICENSE`](LICENSE) for the license terms.

<div align="center">

Made with care for Telegram music communities.

</div>
