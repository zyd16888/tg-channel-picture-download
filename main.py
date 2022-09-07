# telegram频道图片下载
import asyncio
import datetime
import time
from pyrogram import Client, filters
from config import settings

api_id  = settings.api_id
api_hash  = settings.api_hash
proxy = settings.proxy
# Create a new Client instance
if proxy.enable:
    app = Client("my_account", api_id=api_id, api_hash=api_hash, proxy=proxy)
else:
    app = Client("my_account", api_id=api_id, api_hash=api_hash)

date = '2022-08-23 06:15:25'
# change date to datetime
time6 = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
# get timestamp
def get_timestamp():
    return time.time()




async def main():
    start = time.time()
    async with app:
        # Send a message, Markdown is enabled by default
        await app.send_message("me", f"Hi there! I'm using **Pyrogram**{start}")
        # Get the message history of a chat
        tasks = []
        num = 0 # 计数器
        async for message in app.get_chat_history(-1001383316433):
            # download_image(message)
            await save_message(message)
            if message.photo:
                photo = message.photo
                num += 1
                tasks.append(app.download_media(photo, file_name=f'./images/{photo.file_unique_id}.jpg', progress=progress, progress_args=(photo.file_unique_id, num)))
                if num % 100 == 0: # 每100个任务开始执行一次下载
                    await asyncio.gather(*tasks)
                    tasks = []
                if num % 1000 == 0:
                    time.sleep(60) # 每1000个任务停一分钟
        await asyncio.gather(*tasks)

        # print(res)

    end = time.time()
    print(end - start)

async def save_message(message):
    # 保存消息到本地文件
    with open('message_不绝对领域.txt', 'a', encoding="utf-8") as f:
        f.write(str(message))

def progress(current, total, file_unique_id, num):
    print(f"{num}-{file_unique_id} {current * 100 / total:.1f}%")



@app.on_message(filters.command("start"))
async def download_image(message):
    photo = message.photo
    file_name = f'{photo.file_unique_id}.jpg'
    await app.download_media(photo, file_name=f'./image_test/{file_name}', progress=progress)

app.run(main())


