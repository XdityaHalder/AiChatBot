import os, random

from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
from typing import Union, List, Pattern


API_ID = os.environ.get("API_ID", 0)
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
MONGO_DB_URL = os.environ.get("MONGO_DB_URL", None)


client = Client(
    name="AiChatBot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=STRING_SESSION,
)

# custom command filters
def cdx(commands: Union[str, List[str]]):
    return filters.command(commands, ["/", "!", "."])


@client.on_message(cdx(["alive"]) & ~filters.private)
async def start_in_chat(client, message):
    return await message.reply_text(f"**🥀 𝑰 𝒂𝒎 𝑨𝒍𝒊𝒗𝒆 𝑫𝒆𝒂𝒓 ✨...**")


@client.on_message(
    (filters.text | filters.sticker)
    & ~filters.private & ~filters.me & ~filters.bot
)
async def text_and_sticker(client: Client, message: Message):

    chatdb = MongoClient(MONGO_DB_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        adityadb = MongoClient(MONGO_DB_URL)
        aditya = adityadb["AdityaDb"]["Aditya"]
        is_aditya = aditya.find_one({"chat_id": message.chat.id})
        if not is_aditya:
            await client.send_chat_action(message.chat.id, "typing")
            K = []
            is_chat = chatai.find({"word": message.text})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if not Yo == "sticker":
                    await message.reply_text(f"{hey}")

    if message.reply_to_message:
        adityadb = MongoClient(MONGO_DB_URL)
        aditya = adityadb["AdityaDb"]["Aditya"]
        is_aditya = aditya.find_one({"chat_id": message.chat.id})
        getme = await client.get_me()
        user_id = getme.id
        if message.reply_to_message.from_user.id == user_id:
            if not is_aditya:
                await client.send_chat_action(message.chat.id, "typing")
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "sticker":
                        await message.reply_sticker(f"{hey}")
                    if not Yo == "sticker":
                        await message.reply_text(f"{hey}")
        if not message.reply_to_message.from_user.id == user_id:
            if message.sticker:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.text,
                        "id": message.sticker.file_unique_id,
                    }
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.text,
                            "text": message.sticker.file_id,
                            "check": "sticker",
                            "id": message.sticker.file_unique_id,
                        }
                    )
            if message.text:
                is_chat = chatai.find_one(
                    {"word": message.reply_to_message.text, "text": message.text}
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.text,
                            "text": message.text,
                            "check": "none",
                        }
                    )


@client.on_message(
    (filters.sticker | filters.text)
    & ~filters.private & ~filters.me & ~filters.bot
)
async def adityastickerai(client: Client, message: Message):

    chatdb = MongoClient(MONGO_DB_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        adityadb = MongoClient(MONGO_DB_URL)
        aditya = adityadb["AdityaDb"]["Aditya"]
        is_aditya = aditya.find_one({"chat_id": message.chat.id})
        if not is_aditya:
            await client.send_chat_action(message.chat.id, "typing")
            K = []
            is_chat = chatai.find({"word": message.sticker.file_unique_id})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "text":
                    await message.reply_text(f"{hey}")
                if not Yo == "text":
                    await message.reply_sticker(f"{hey}")

    if message.reply_to_message:
        adityadb = MongoClient(MONGO_DB_URL)
        aditya = adityadb["AdityaDb"]["Aditya"]
        is_aditya = aditya.find_one({"chat_id": message.chat.id})
        getme = await client.get_me()
        user_id = getme.id
        if message.reply_to_message.from_user.id == user_id:
            if not is_aditya:
                await client.send_chat_action(message.chat.id, "typing")
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "text":
                        await message.reply_text(f"{hey}")
                    if not Yo == "text":
                        await message.reply_sticker(f"{hey}")
        if not message.reply_to_message.from_user.id == user_id:
            if message.text:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.text,
                    }
                )
                if not is_chat:
                    toggle.insert_one(
                        {
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.text,
                            "check": "text",
                        }
                    )
            if message.sticker:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.sticker.file_id,
                    }
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.sticker.file_id,
                            "check": "none",
                        }
                    )


@client.on_message(
    (filters.text | filters.sticker)
    & filters.private & ~filters.me & ~filters.bot
)
async def adityaprivate(client: Client, message: Message):

    chatdb = MongoClient(MONGO_DB_URL)
    chatai = chatdb["Word"]["WordDb"]
    if not message.reply_to_message:
        await client.send_chat_action(message.chat.id, "typing")
        K = []
        is_chat = chatai.find({"word": message.text})
        for x in is_chat:
            K.append(x["text"])
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        Yo = is_text["check"]
        if Yo == "sticker":
            await message.reply_sticker(f"{hey}")
        if not Yo == "sticker":
            await message.reply_text(f"{hey}")
    if message.reply_to_message:
        getme = await client.get_me()
        user_id = getme.id
        if message.reply_to_message.from_user.id == user_id:
            await client.send_chat_action(message.chat.id, "typing")
            K = []
            is_chat = chatai.find({"word": message.text})
            for x in is_chat:
                K.append(x["text"])
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text["check"]
            if Yo == "sticker":
                await message.reply_sticker(f"{hey}")
            if not Yo == "sticker":
                await message.reply_text(f"{hey}")


@client.on_message(
    (filters.sticker | filters.text)
    & filters.private & ~filters.me & ~filters.bot
)
async def adityaprivatesticker(client: Client, message: Message):

    chatdb = MongoClient(MONGO_DB_URL)
    chatai = chatdb["Word"]["WordDb"]
    if not message.reply_to_message:
        await client.send_chat_action(message.chat.id, "typing")
        K = []
        is_chat = chatai.find({"word": message.sticker.file_unique_id})
        for x in is_chat:
            K.append(x["text"])
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        Yo = is_text["check"]
        if Yo == "text":
            await message.reply_text(f"{hey}")
        if not Yo == "text":
            await message.reply_sticker(f"{hey}")
    if message.reply_to_message:
        getme = await client.get_me()
        user_id = getme.id
        if message.reply_to_message.from_user.id == user_id:
            await client.send_chat_action(message.chat.id, "typing")
            K = []
            is_chat = chatai.find({"word": message.sticker.file_unique_id})
            for x in is_chat:
                K.append(x["text"])
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text["check"]
            if Yo == "text":
                await message.reply_text(f"{hey}")
            if not Yo == "text":
                await message.reply_sticker(f"{hey}")


client.run()
