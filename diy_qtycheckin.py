#
#cron "5 0 0 * * *" autoShareCode.py, tag:qty自动签到
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
# 在 https://my.telegram.org 申请到的 id 和 hash 值
client = TelegramClient("bot", 18642001, "44ed97b7e6d493cac73a57daf292fbe4", connection_retries=None).start()
async def main():
    # qty签到
    await client.send_message("@qtyuncloud_bot", "/checkin")
    await client.send_read_acknowledge("@qtyuncloud_bot")
with client:
    client.loop.run_until_complete(main())
