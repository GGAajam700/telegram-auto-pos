from telethon import TelegramClient, events
import asyncio

api_id = 36052645
api_hash = "d1144f120a817edab4e446591a56717c"

source_channels = [
    "apna_exams"
]

target_channel = "examupdate3"

REPLACE_TEXTS = [
    "@apna_exams",
    "Join",
    "for more such updates"
]

ADD_TEXT = "\n\n👉 Join @examupdate3 for more such updates"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    msg = event.message
    text = msg.text or ""

    for t in REPLACE_TEXTS:
        text = text.replace(t, "")

    text = text.strip() + ADD_TEXT
    await asyncio.sleep(2)

    await client.send_message(
        target_channel,
        text,
        file=msg.media
    )

client.start()
client.run_until_disconnected()
