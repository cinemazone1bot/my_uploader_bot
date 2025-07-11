from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

# توکن و آیدی کانال از متغیرهای محیطی گرفته می‌شن
TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

async def handle_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.video or update.message.audio
    if file:
        await update.message.reply_text("✅ فایل دریافت شد، در حال ارسال به کانال...")
        await context.bot.send_document(
            chat_id=CHANNEL_ID,
            document=file.file_id,
            caption=f"📤 ارسال توسط {update.message.from_user.first_name}"
        )
        await update.message.reply_text("✅ با موفقیت در کانال ارسال شد.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL | filters.Video.ALL | filters.Audio.ALL, handle_files))
app.run_polling()
