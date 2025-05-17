import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as KB, InlineKeyboardMarkup as KM

# Bot credentials from environment variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Initialize client with API ID, API HASH, and Bot Token
app = Client("prank_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Image URLs
START_IMAGE = "https://i.ibb.co/XZKGjP03/x.jpg"
PRANK_IMAGE = "https://i.ibb.co/sdtR2VS2/x.jpg"

# Professional caption
START_CAPTION = """
<b>🎓 Premium Education Content Extractor Bot 🎓</b>

<b>✨ Features:</b>
• 100+ Educational Platforms Supported
• One-Click Content Extraction
• Premium Quality Content
• Regular Updates

<b>🚀 Get started by exploring the apps below:</b>
"""

# Keyboards
def home():
    return KM([
        [KB("🌟 VIP (Normal App) 🤖", "page_1"), KB("🚀 PRO (Special App) 🚀", "page_2")],
        [KB("⚡ Legend (No Login Required) ⚡", "page_3")],
        [KB("❌ Close ❌", "close")]
    ])

def page_1():
    return KM([
        [KB("🌐 All Appx API APP [Web Url or API] 🌐", "/prank")],
        [KB("📱 All ClassPlus APK 📱", "/prank")],
        [KB("🔑 ClassPlus Token Generator 🔑", "/prank")],
        [KB("📘 Edukemy 📘", "/prank"), KB("📗 Apni Kaksha 📗", "/prank")],
        [KB("📕 Khan GS 📕", "/prank")],
        [KB("📙 Neon Classes 📙", "/prank")],
        [KB("🎓 Nidhi Academy 🎓", "/prank"), KB("🎥 KD LIVE 🎥", "/prank")],
        [KB("📚 Physics Wallah 📚", "/prank")],
        [KB("👨‍🏫 Tarun Grover Sir 👨‍🏫", "/prank")],
        [KB("🏫 My Pathsala 🏫", "/prank"), KB("📝 CareerWill 📝", "/prank")],
        [KB("🌟 My Rising India 🌟", "/prank")],
        [KB("🩺 Nursing Next 🩺", "/prank")],
        [KB("⏩ Next Page ➡️", "page_2")]
    ])

def page_2():
    return KM([
        [KB("🎯 Allen New V2 🎯", "/prank")],
        [KB("🚀 Allen Institute 🚀", "/prank")],
        [KB("🎓 IFAS Academy 🎓", "/prank"), KB("🧑‍🏫 ICS Coaching 🧑‍🏫", "/prank")],
        [KB("🌟 Sanskriti IAS 🌟", "/prank")],
        [KB("🩺 Nursing Next 🩺", "/prank")],
        [KB("💡 Study IQ 💡", "/prank"), KB("🏆 Utkarsh 🏆", "/prank")],
        [KB("📚 Forum IAS 📚", "/prank")],
        [KB("🔍 Vision IAS 🔍", "/prank")],
        [KB("💼 Insight IAS 💼", "/prank"), KB("📝 Vajiram IAS 📝", "/prank")],
        [KB("🔑 Sunya IAS 🔑", "/prank")],
        [KB("📈 Level UP IAS 📈", "/prank")],
        [KB("🏅 Next IAS 🏅", "/prank"), KB("🔧 MadeEasy 🔧", "/prank")],
        [KB("🌐 WebSankul 🌐", "/prank")],
        [KB("💻 All Spayee Websites 💻", "/prank")],
        [KB("💻 DSL KrantiKari 💻", "/prank")],
        [KB("🔙 Back Page ⬅️", "page_1"), KB("➡️ Next Page ➡️", "page_3")]
    ])

def page_3():
    return KM([
        [KB("🌐 Appx All API (Nothing Required) 🌐", "/prank")],
        [KB("🎲 Adda 247 (Any Random Login) 🎲", "/prank")],
        [KB("📘 Abhinav Maths (Nothing Required) 📘", "/prank")],
        [KB("🚀 CDS Journey (Any Random Login) 🚀", "/prank")],
        [KB("📱 ClassPlus (Org Code Required) 📱", "/prank")],
        [KB("🎓 Awadh Ojha App (Nothing Required) 🎓", "/prank")],
        [KB("📕 Khan Sir (Nothing Required) 📕", "/prank")],
        [KB("🧑‍🏫 ICS Coaching (Any Random Login) 🧑‍🏫", "/prank")],
        [KB("🧑‍🏫 IFAS Academy (Any Random Login) 🧑‍🏫", "/prank")],
        [KB("📚 Forum IAS (Any Random Token) 📚", "/prank")],
        [KB("📚 JRF Adda (Nothing Required) 📚", "/prank")],
        [KB("🏫 My Pathsala (Nothing Required) 🏫", "/prank")],
        [KB("🔑 Physics Wallah (Any Random Token) 🔑", "/prank")],
        [KB("🎓 Quality Education (Nothing Required) 🎓", "/prank")],
        [KB("💡 Study IQ (Nothing Required) 💡", "/prank")],
        [KB("📘 Sunya IAS (Nothing Required) 📘", "/prank")],
        [KB("📝 Test Paper (Nothing Required) 📝", "/prank")],
        [KB("🎯 TestBook (Any Random Login) 🎯", "/prank")],
        [KB("🚀 Verbal Math (Nothing Required)🚀 ", "/prank")],
        [KB("🔙 Back Page ⬅️", "page_2"), KB("🏠 Home 🏠", "home")]
    ])

# Command handlers
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_photo(
        photo=START_IMAGE,
        caption=START_CAPTION,
        reply_markup=home()
    )

# Prank handler for all app buttons
@app.on_callback_query(filters.regex("^/prank$"))
async def send_prank(client, callback_query):
    await client.send_photo(
        chat_id=callback_query.from_user.id,
        photo=PRANK_IMAGE,
        reply_to_message_id=callback_query.message.id
    )
    await callback_query.answer()

# Navigation handlers
@app.on_callback_query(filters.regex("^page_"))
async def handle_pages(client, callback_query):
    page = int(callback_query.data.split("_")[1])
    if page == 1:
        await callback_query.message.edit_reply_markup(page_1())
    elif page == 2:
        await callback_query.message.edit_reply_markup(page_2())
    elif page == 3:
        await callback_query.message.edit_reply_markup(page_3())

@app.on_callback_query(filters.regex("^home$"))
async def go_home(client, callback_query):
    await callback_query.message.edit_reply_markup(home())

@app.on_callback_query(filters.regex("^close$"))
async def close_menu(client, callback_query):
    await callback_query.message.delete()

print("Bot is running...")
app.run()
