# cron：0 0 * * 0 python3 example.py
#依赖：
#pip3 install requests
#pip3 install telethon
[task_local]
#cron "5 0 0 * * 1" autoShareCode.py, tag:自动提交助力码

from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
# 在 https://my.telegram.org 申请到的 id 和 hash 值
client = TelegramClient("bot", 18642001, "44ed97b7e6d493cac73a57daf292fbe4", connection_retries=None).start()
async def main():
    # 将您的互助码替换掉下面的 “<码1>&<码2>&<码3>&<码4>&<码5>”，可直接从导出互助码日志中提取
    await client.send_message("@JDShareCodebot", "/farm 08fd097cfa7f4424b6cbcf4269711c41&bacb4b5024ce4a99b706e53bc86990e8&d84c2308e111438a89a35f7bc955b7c0&5b45f6c6621f4b73a23ac3a65ab49de7&b8f807093f144becae16e1ab7a2c81eb")
    await client.send_message("@JDShareCodebot", "/pet MTE5MzEwNTEzODAwMDAwMDA1NTcxNjU2MQ==&MTEyNjE4NjQ2MDAwMDAwMDU1NzY5MDk5&MTEzMzI1MTE4NTAwMDAwMDA2OTI5NjE3NQ==&MTE1NDY3NTMwMDAwMDAwNjkwNzg4MjM=&MTEzMzI1MTE4NDAwMDAwMDA3NjA3NjQyMw==")
    await client.send_message("@JDShareCodebot", "/bean e7lhibzb3zek24owajrpfcdzp35ksvfymcf32yq&olmijoxgmjutzeh2ba64kognnsgjk2l3c2ohmca&t7obxmpebrxkcostfx2v4gfqgzarxu3hbn56dny&olmijoxgmjuty52u4k3kyh7323ybmoj6legnuvy&4npkonnsy7xi2ijzrfwp7morjbssh5cprglthyy")
    await client.send_message("@JDShareCodebot", "/jxfactory 2ytWjFp_M5bIpzHK6ziZdg==&LJsqJ2zOnvBs1oWBO3M0Hw==")
    await client.send_message("@JDShareCodebot", "/ddfactory T0225KkcRBof9FKEIE-gnfIKcgCjVWnYaS5kRrbA&T0225KkcRh8a8lzXIhmgxvQLIACjVWnYaS5kRrbA&T0205KkcFGxlli-oeW-M7JRNCjVWnYaS5kRrbA&T0225KkcRh0d_VDWch6hwaJbdgCjVWnYaS5kRrbA&T0225KkcRxcRpFOGIh30kPYJfQCjVWnYaS5kRrbA")
    await client.send_message("@JDShareCodebot", "/sgmh T0225KkcRBof9FKEIE-gnfIKcgCjVQmoaT5kRrbA&T0225KkcRh8a8lzXIhmgxvQLIACjVQmoaT5kRrbA&T0205KkcFGxlli-oeW-M7JRNCjVQmoaT5kRrbA&T0225KkcRh0d_VDWch6hwaJbdgCjVQmoaT5kRrbA&T0225KkcRxcRpFOGIh30kPYJfQCjVQmoaT5kRrbA")
    await client.send_message("@JDShareCodebot", "/health T0225KkcRBof9FKEIE-gnfIKcgCjVfnoaW5kRrbA&T0225KkcRh8a8lzXIhmgxvQLIACjVfnoaW5kRrbA&T0205KkcFGxlli-oeW-M7JRNCjVfnoaW5kRrbA&T0225KkcRh0d_VDWch6hwaJbdgCjVfnoaW5kRrbA&T0225KkcRxcRpFOGIh30kPYJfQCjVfnoaW5kRrbA")
    await client.send_read_acknowledge("@JDShareCodebot")
with client:
    client.loop.run_until_complete(main())
