import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as KB, InlineKeyboardMarkup as KM
from pyrogram.enums import ParseMode

# Configuration
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Set in Render environment variables
ADMIN_ID = int(os.environ.get("ADMIN_ID"))  # Your Telegram user ID

# Initialize client
app = Client("prank_bot", bot_token=BOT_TOKEN)

# Database to store user IDs
user_db = set()

# Image URLs
START_IMAGE = "https://i.ibb.co/XZKGjP03/x.jpg"
PRANK_IMAGES = [
    "https://i.ibb.co/MWcnjS4/x.jpg",
    "https://i.ibb.co/6cDSfLHv/x.jpg", 
    "https://i.ibb.co/tTrJLfRW/x.jpg",
    "https://i.ibb.co/3m7J4tGJ/x.jpg",
    "https://i.ibb.co/jvD6s7KN/x.jpg"
]

# Start message
START_CAPTION = """
<b>🎓 Premium Education Content Extractor Bot 🎓</b>

<b>✨ Features:</b>
• 100+ Educational Platforms Supported
• One-Click Content Extraction
• Premium Quality Content
• Regular Updates

<b>🚀 Get started by exploring the apps below:</b>
"""

# Keyboard layouts with unique callback data for each app
def home():
    return KM([
        [KB("🌟 VIP (Normal App) 🤖", "page_1"), KB("🚀 PRO (Special App) 🚀", "page_2")],
        [KB("⚡ Legend (No Login Required) ⚡", "page_3")],
        [KB("🔐 Admin Panel", "admin_panel") if ADMIN_ID else None]
    ])

def page_1():
    return KM([
        [KB("🌐 All Appx API APP [Web Url or API] 🌐", "appx_api")],
        [KB("📱 All ClassPlus APK 📱", "classplus_apk")],
        [KB("🔑 ClassPlus Token Generator 🔑", "classplus_token")],
        [KB("📘 Edukemy 📘", "edukemy"), KB("📗 Apni Kaksha 📗", "apni_kaksha")],
        [KB("📕 Khan GS 📕", "khan_gs")],
        [KB("📙 Neon Classes 📙", "neon_classes")],
        [KB("🎓 Nidhi Academy 🎓", "nidhi_academy"), KB("🎥 KD LIVE 🎥", "kd_live")],
        [KB("📚 Physics Wallah 📚", "physics_wallah")],
        [KB("👨‍🏫 Tarun Grover Sir 👨‍🏫", "tarun_grover")],
        [KB("🏫 My Pathsala 🏫", "my_pathsala"), KB("📝 CareerWill 📝", "careerwill")],
        [KB("🌟 My Rising India 🌟", "rising_india")],
        [KB("🩺 Nursing Next 🩺", "nursing_next")],
        [KB("⏩ Next Page ➡️", "page_2")]
    ])

def page_2():
    return KM([
        [KB("🎯 Allen New V2 🎯", "allen_v2")],
        [KB("🚀 Allen Institute 🚀", "allen_institute")],
        [KB("🎓 IFAS Academy 🎓", "ifas_academy"), KB("🧑‍🏫 ICS Coaching 🧑‍🏫", "ics_coaching")],
        [KB("🌟 Sanskriti IAS 🌟", "sanskriti_ias")],
        [KB("🩺 Nursing Next 🩺", "nursing_next")],
        [KB("💡 Study IQ 💡", "study_iq"), KB("🏆 Utkarsh 🏆", "utkarsh")],
        [KB("📚 Forum IAS 📚", "forum_ias")],
        [KB("🔍 Vision IAS 🔍", "vision_ias")],
        [KB("💼 Insight IAS 💼", "insight_ias"), KB("📝 Vajiram IAS 📝", "vajiram_ias")],
        [KB("🔑 Sunya IAS 🔑", "sunya_ias")],
        [KB("📈 Level UP IAS 📈", "levelup_ias")],
        [KB("🏅 Next IAS 🏅", "next_ias"), KB("🔧 MadeEasy 🔧", "madeeasy")],
        [KB("🌐 WebSankul 🌐", "websankul")],
        [KB("💻 All Spayee Websites 💻", "spayee")],
        [KB("💻 DSL KrantiKari 💻", "dsl_kranti")],
        [KB("🔙 Back Page ⬅️", "page_1"), KB("➡️ Next Page ➡️", "page_3")]
    ])

def page_3():
    return KM([
        [KB("🌐 Appx All API (Nothing Required) 🌐", "appx_free")],
        [KB("🎲 Adda 247 (Any Random Login) 🎲", "adda247")],
        [KB("📘 Abhinav Maths (Nothing Required) 📘", "abhinav_maths")],
        [KB("🚀 CDS Journey (Any Random Login) 🚀", "cds_journey")],
        [KB("📱 ClassPlus (Org Code Required) 📱", "classplus_org")],
        [KB("🎓 Awadh Ojha App (Nothing Required) 🎓", "awadh_ojha")],
        [KB("📕 Khan Sir (Nothing Required) 📕", "khan_sir")],
        [KB("🧑‍🏫 ICS Coaching (Any Random Login) 🧑‍🏫", "ics_free")],
        [KB("🧑‍🏫 IFAS Academy (Any Random Login) 🧑‍🏫", "ifas_free")],
        [KB("📚 Forum IAS (Any Random Token) 📚", "forum_free")],
        [KB("📚 JRF Adda (Nothing Required) 📚", "jrf_adda")],
        [KB("🏫 My Pathsala (Nothing Required) 🏫", "pathsala_free")],
        [KB("🔑 Physics Wallah (Any Random Token) 🔑", "pw_free")],
        [KB("🎓 Quality Education (Nothing Required) 🎓", "quality_free")],
        [KB("💡 Study IQ (Nothing Required) 💡", "iq_free")],
        [KB("📘 Sunya IAS (Nothing Required) 📘", "sunya_free")],
        [KB("📝 Test Paper (Nothing Required) 📝", "test_paper")],
        [KB("🎯 TestBook (Any Random Login) 🎯", "testbook")],
        [KB("🚀 Verbal Math (Nothing Required) 🚀", "verbal_math")],
        [KB("🔙 Back Page ⬅️", "page_2"), KB("🏠 Home 🏠", "home")]
    ])

# Notification function
async def notify_admin(user, action="started"):
    try:
        await app.send_message(
            ADMIN_ID,
            f"👤 <b>New User {action}:</b>\n\n"
            f"• Name: {user.first_name}\n"
            f"• ID: <code>{user.id}</code>\n"
            f"• Username: @{user.username}" if user.username else "• No username",
            parse_mode=ParseMode.HTML
        )
    except Exception as e:
        print(f"Error sending notification: {e}")

# Start command
@app.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user
    if user.id not in user_db:
        user_db.add(user.id)
        await notify_admin(user)
    
    await message.reply_photo(
        photo=START_IMAGE,
        caption=START_CAPTION,
        reply_markup=home()
    )

# Forward all messages to admin
@app.on_message(filters.private & ~filters.command(["start", "broadcast", "users"]))
async def forward_to_admin(client, message):
    if message.from_user.id not in user_db:
        user_db.add(message.from_user.id)
        await notify_admin(message.from_user, "messaged")
    
    try:
        await app.send_message(
            ADMIN_ID,
            f"📩 <b>New Message from {message.from_user.first_name}:</b>\n\n"
            f"<code>{message.text}</code>\n\n"
            f"User ID: <code>{message.from_user.id}</code>",
            parse_mode=ParseMode.HTML
        )
    except Exception as e:
        print(f"Error forwarding message: {e}")

# Broadcast command (admin only)
@app.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast(client, message):
    if len(message.text.split()) < 2:
        await message.reply("Usage: /broadcast your_message")
        return
    
    text = message.text.split(maxsplit=1)[1]
    success = 0
    failed = 0
    
    for user_id in user_db:
        try:
            await app.send_message(user_id, text)
            success += 1
        except:
            failed += 1
            user_db.remove(user_id)  # Remove inactive users
    
    await message.reply(
        f"📢 <b>Broadcast Report:</b>\n\n"
        f"• Total users: {len(user_db)}\n"
        f"• ✅ Success: {success}\n"
        f"• ❌ Failed: {failed}",
        parse_mode=ParseMode.HTML
    )

# Show user count (admin only)
@app.on_message(filters.command("users") & filters.user(ADMIN_ID))
async def show_users(client, message):
    await message.reply(f"👥 Total users: {len(user_db)}")

# Admin panel
@app.on_callback_query(filters.regex("^admin_panel$"))
async def admin_panel(client, callback_query):
    if callback_query.from_user.id != ADMIN_ID:
        await callback_query.answer("⚠️ Access denied!", show_alert=True)
        return
    
    await callback_query.message.edit_reply_markup(
        KM([
            [KB("📢 Broadcast", "broadcast_panel"), KB("👥 User Count", "user_count")],
            [KB("🔙 Back", "home")]
        ])
    )
    await callback_query.answer()

# Prank handler for all app buttons
@app.on_callback_query(filters.regex(r"^(appx_|classplus_|edukemy|apni_kaksha|khan_|neon_|nidhi_|kd_|physics_|tarun_|my_pathsala|careerwill|rising_|nursing_|allen_|ifas_|ics_|sanskriti_|study_|utkarsh|forum_|vision_|insight_|vajiram_|sunya_|levelup_|next_|madeeasy|websankul|spayee|dsl_|adda247|abhinav_|cds_|awadh_|jrf_|pathsala_|pw_|quality_|iq_|test_|verbal_)"))
async def send_prank(client, callback_query):
    prank_image = random.choice(PRANK_IMAGES)
    await callback_query.message.reply_photo(
        photo=prank_image,
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
    await callback_query.answer()

@app.on_callback_query(filters.regex("^home$"))
async def go_home(client, callback_query):
    await callback_query.message.edit_reply_markup(home())
    await callback_query.answer()

@app.on_callback_query(filters.regex("^close$"))
async def close_menu(client, callback_query):
    await callback_query.message.delete()
    await callback_query.answer()

print("✅ Bot is running with all features!")
app.run()
