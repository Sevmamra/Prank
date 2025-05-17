import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as KB, InlineKeyboardMarkup as KM
from pyrogram.errors import UserIsBlocked

# Bot credentials from environment variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Initialize client
app = Client("prank_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Image URLs
START_IMAGE = "https://i.ibb.co/XZKGjP03/x.jpg"
PRANK_IMAGES = [
    "https://i.ibb.co/MWcnjS4/x.jpg",
    "https://i.ibb.co/6cDSfLHv/x.jpg",
    "https://i.ibb.co/tTrJLfRW/x.jpg",
    "https://i.ibb.co/3m7J4tGJ/x.jpg",
    "https://i.ibb.co/jvD6s7KN/x.jpg"
]

# Owner ID (apna Telegram numeric ID daal do)
OWNER_ID = 6567162029  # << yaha apni ID daal dena

# Registered users list
USERS_FILE = "users.txt"

# Caption
START_CAPTION = """
<b>🎓 Premium Education Content Extractor Bot 🎓</b>

<b>✨ Features:</b>
• 100+ Educational Platforms Supported
• One-Click Content Extraction
• Premium Quality Content
• Regular Updates

<b>🚀 Get started by exploring the apps below:</b>
"""

# Home Keyboard
def home():
    return KM([
        [KB("🌟 VIP (Normal App) 🤖", "page_1"), KB("🚀 PRO (Special App) 🚀", "page_2")],
        [KB("⚡ Legend (No Login Required) ⚡", "page_3")],
        [KB("❌ Close ❌", "close")]
    ])

# Page 1
def page_1():
    return KM([
        [KB("🌐 All Appx API APP [Web Url or API] 🌐", "prank_1")],
        [KB("📱 All ClassPlus APK 📱", "prank_2")],
        [KB("🔑 ClassPlus Token Generator 🔑", "prank_3")],
        [KB("📘 Edukemy 📘", "prank_4"), KB("📗 Apni Kaksha 📗", "prank_5")],
        [KB("📕 Khan GS 📕", "prank_6")],
        [KB("📙 Neon Classes 📙", "prank_7")],
        [KB("🎓 Nidhi Academy 🎓", "prank_8"), KB("🎥 KD LIVE 🎥", "prank_9")],
        [KB("📚 Physics Wallah 📚", "prank_10")],
        [KB("👨‍🏫 Tarun Grover Sir 👨‍🏫", "prank_11")],
        [KB("🏫 My Pathsala 🏫", "prank_12"), KB("📝 CareerWill 📝", "prank_13")],
        [KB("🌟 My Rising India 🌟", "prank_14")],
        [KB("🩺 Nursing Next 🩺", "prank_15")],
        [KB("⏩ Next Page ➡️", "page_2")]
    ])

# Page 2
def page_2():
    return KM([
        [KB("🎯 Allen New V2 🎯", "prank_16")],
        [KB("🚀 Allen Institute 🚀", "prank_17")],
        [KB("🎓 IFAS Academy 🎓", "prank_18"), KB("🧑‍🏫 ICS Coaching 🧑‍🏫", "prank_19")],
        [KB("🌟 Sanskriti IAS 🌟", "prank_20")],
        [KB("🩺 Nursing Next 🩺", "prank_21")],
        [KB("💡 Study IQ 💡", "prank_22"), KB("🏆 Utkarsh 🏆", "prank_23")],
        [KB("📚 Forum IAS 📚", "prank_24")],
        [KB("🔍 Vision IAS 🔍", "prank_25")],
        [KB("💼 Insight IAS 💼", "prank_26"), KB("📝 Vajiram IAS 📝", "prank_27")],
        [KB("🔑 Sunya IAS 🔑", "prank_28")],
        [KB("📈 Level UP IAS 📈", "prank_29")],
        [KB("🏅 Next IAS 🏅", "prank_30"), KB("🔧 MadeEasy 🔧", "prank_31")],
        [KB("🌐 WebSankul 🌐", "prank_32")],
        [KB("💻 All Spayee Websites 💻", "prank_33")],
        [KB("💻 DSL KrantiKari 💻", "prank_34")],
        [KB("🔙 Back Page ⬅️", "page_1"), KB("➡️ Next Page ➡️", "page_3")]
    ])

# Page 3
def page_3():
    return KM([
        [KB("🌐 Appx All API (Nothing Required) 🌐", "prank_35")],
        [KB("🎲 Adda 247 (Any Random Login) 🎲", "prank_36")],
        [KB("📘 Abhinav Maths (Nothing Required) 📘", "prank_37")],
        [KB("🚀 CDS Journey (Any Random Login) 🚀", "prank_38")],
        [KB("📱 ClassPlus (Org Code Required) 📱", "prank_39")],
        [KB("🎓 Awadh Ojha App (Nothing Required) 🎓", "prank_40")],
        [KB("📕 Khan Sir (Nothing Required) 📕", "prank_41")],
        [KB("🧑‍🏫 ICS Coaching (Any Random Login) 🧑‍🏫", "prank_42")],
        [KB("🧑‍🏫 IFAS Academy (Any Random Login) 🧑‍🏫", "prank_43")],
        [KB("📚 Forum IAS (Any Random Token) 📚", "prank_44")],
        [KB("📚 JRF Adda (Nothing Required) 📚", "prank_45")],
        [KB("🏫 My Pathsala (Nothing Required) 🏫", "prank_46")],
        [KB("🔑 Physics Wallah (Any Random Token) 🔑", "prank_47")],
        [KB("🎓 Quality Education (Nothing Required) 🎓", "prank_48")],
        [KB("💡 Study IQ (Nothing Required) 💡", "prank_49")],
        [KB("📘 Sunya IAS (Nothing Required) 📘", "prank_50")],
        [KB("📝 Test Paper (Nothing Required) 📝", "prank_51")],
        [KB("🎯 TestBook (Any Random Login) 🎯", "prank_52")],
        [KB("🚀 Verbal Math (Nothing Required) 🚀", "prank_53")],
        [KB("🔙 Back Page ⬅️", "page_2"), KB("🏠 Home 🏠", "home")]
    ])

# /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    if not os.path.exists(USERS_FILE):
        open(USERS_FILE, "w").close()
    with open(USERS_FILE, "r") as f:
        users = f.read().splitlines()
    if str(user_id) not in users:
        with open(USERS_FILE, "a") as f:
            f.write(f"{user_id}\n")
        await client.send_message(OWNER_ID, f"👤 New user joined: [{message.from_user.first_name}](tg://user?id={user_id}) (`{user_id}`)", parse_mode="markdown")
    await message.reply_photo(photo=START_IMAGE, caption=START_CAPTION, reply_markup=home())

# Navigation handlers
@app.on_callback_query(filters.regex("^page_"))
async def handle_pages(client, cb):
    page = int(cb.data.split("_")[1])
    if page == 1:
        await cb.message.edit_reply_markup(page_1())
    elif page == 2:
        await cb.message.edit_reply_markup(page_2())
    elif page == 3:
        await cb.message.edit_reply_markup(page_3())
    await cb.answer()

@app.on_callback_query(filters.regex("^home$"))
async def go_home(client, cb):
    await cb.message.edit_reply_markup(home())
    await cb.answer()

@app.on_callback_query(filters.regex("^close$"))
async def close_menu(client, cb):
    await cb.message.delete()

# All prank buttons handler
@app.on_callback_query(filters.regex("^prank_"))
async def send_prank(client, cb):
    prank_image = random.choice(PRANK_IMAGES)
    await client.send_photo(chat_id=cb.from_user.id, photo=prank_image, reply_to_message_id=cb.message.id)
    await cb.answer("Prank delivered!")

# Broadcast command
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    if len(message.command) < 2:
        await message.reply("Usage: /broadcast your_message_here")
        return
    text_to_send = message.text.split(" ", 1)[1]
    if not os.path.exists(USERS_FILE):
        await message.reply("Koi user registered nahi hai.")
        return
    with open(USERS_FILE, "r") as f:
        users = f.read().splitlines()
    sent, failed = 0, 0
    for user in users:
        try:
            await client.send_message(int(user), text_to_send)
            sent += 1
        except UserIsBlocked:
            failed += 1
        except Exception:
            failed += 1
    await message.reply(f"✅ Broadcast done.\nSuccess: {sent}\nFailed: {failed}")

print("Bot is running with user notification, apps & broadcast system...")
app.run()
