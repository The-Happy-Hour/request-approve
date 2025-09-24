from pyrogram import Client, filters
import asyncio
from pyrogram.errors import FloodWait

API_ID = 
API_HASH = 

app = Client(
    "my_userbot",
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("approve"))
async def approve_cmd(client, message):
    chat_id = message.chat.id
    approved = 0
    failed = 0
    await message.reply_text("Starting...")
    async for req in client.get_chat_join_requests(chat_id):
        try:
            await client.approve_chat_join_request(chat_id, req.user.id)
            approved += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            continue
        except Exception as e:
            failed += 1
            print(f"❌ Could not approve {req.user.id}: {e}")
            continue
    await message.reply_text(f"🎉 Done!\n✅ Approved: {approved}\n❌ Failed: {failed}")
app.run()
