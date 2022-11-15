# telegram频道图片下载
import asyncio
import datetime
import time

from pyrogram import Client, filters

from tools.config import settings

api_id = settings.api_id
api_hash = settings.api_hash
proxy = settings.proxy

channel_id = settings.channel_id
message_file = settings.message_file
save_dir = settings.save_dir
offset_id = settings.offset_id


# Create a new Client instance
if proxy.enable:
    app = Client("my_account", api_id=api_id, api_hash=api_hash, proxy=proxy)
else:
    app = Client("my_account", api_id=api_id, api_hash=api_hash)


async def main():
    start = time.time()
    async with app:
        # Send a message, Markdown is enabled by default
        await app.send_message("me", f"Hi there! I'm using **Pyrogram**{start}")
        await download_image(channel_id, message_file, save_dir, offset_id)
    end = time.time()
    print(end - start)


async def save_message(message, file_name="message.txt"):
    # 保存消息到本地文件
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(str(message))


def progress(current, total, file_unique_id, num):
    print(f"{num}-{file_unique_id} {current * 100 / total:.1f}%")


async def download_image(
    chat_id,
    message_name,
    save_path="./images/",
    offset_id=0,
    limit=0,
):
    tasks = []
    num = 0  # 计数器
    async for message in app.get_chat_history(
        chat_id, offset_id=offset_id, limit=limit
    ):
        await save_message(message, message_name)
        if message.photo:
            photo = message.photo
            num += 1
            tasks.append(
                app.download_media(
                    photo,
                    file_name=f"{save_path}",
                    progress=progress,
                    progress_args=(photo.file_unique_id, num),
                )
            )
            if num % 100 == 0:  # 每100个任务开始执行一次下载
                await asyncio.gather(*tasks)
                tasks = []
            if num % 1000 == 0:
                time.sleep(20)  # 每1000个任务停20秒
    await asyncio.gather(*tasks)


app.run(main())
