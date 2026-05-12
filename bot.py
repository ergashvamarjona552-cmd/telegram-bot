from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask
from threading import Thread

# ======= KEEP ALIVE =======
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ======= BOT =======
BOT_TOKEN = "SIZNING_TOKENINGIZ"  # <-- Render da Environment Variables ga kiritasiz

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📍 Manzil", callback_data="manzil"),
            InlineKeyboardButton("👤 Admin", callback_data="admin"),
        ],
        [
            InlineKeyboardButton("📚 Kurslar", callback_data="kurslar"),
            InlineKeyboardButton("💰 Narxlar", callback_data="narxlar"),
        ],
        [
            InlineKeyboardButton("📞 Aloqa", callback_data="aloqa"),
            InlineKeyboardButton("ℹ️ Biz haqimizda", callback_data="haqimizda"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Salom 👋 do it school botiga xush kelibsiz 😊\nTanlang 👇",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "manzil":
        await query.message.reply_text(
            "📍 *Manzil:*\nBo'stonliq tumani, So'yliq qishlog'i\n11-sonli umumta'lim maktabi\n\n"
            "🗺️ Google Maps: https://maps.google.com/?q=JQ59+59Q+Saylyk+Tashkent",
            parse_mode="Markdown"
        )
        await query.message.reply_location(
            latitude=41.5672,
            longitude=69.7215
        )

    elif query.data == "admin":
        await query.message.reply_text(
            "👤 *Admin:*\n@radnoy_ustoz",
            parse_mode="Markdown"
        )

    elif query.data == "kurslar":
        await query.message.reply_text(
            "📚 *Kurslar ro'yxati:*\n\n"
            "do it school markazida:\n\n"
            "1 — Oliy ma'lumotli o'qituvchi 👨‍🏫 ✅\n"
            "2 — Honalar ⭐⭐⭐⭐⭐ ✅\n"
            "3 — Ingliz tili 🇺🇸, Matematika 👨‍🏫, Robototexnika 📍, IT (ay-ti) kurslari mavjud ✅ 😊\n"
            "4 — 12 ta yangi kompyuter 🖥 ✅\n"
            "5 — Robototexnika uchun hamma robotlar 🦾\n"
            "6 — O'quvchilar uchun hamma sharoitlar qilingan 😊\n\n"
            "Men sizga (do it school) ni tavsiya qilaman ✅",
            parse_mode="Markdown"
        )

    elif query.data == "narxlar":
        await query.message.reply_text(
            "💰 *Narxlar:*\nAdmin bilan gaplashing 😊\n👤 @radnoy_ustoz",
            parse_mode="Markdown"
        )

    elif query.data == "aloqa":
        await query.message.reply_text(
            "📞 *Aloqa:*\n\n"
            "Tel 1: +998 99 468 70 20 ✅\n"
            "Tel 2: +998 99 469 70 20 ✅",
            parse_mode="Markdown"
        )

    elif query.data == "haqimizda":
        await query.message.reply_text(
            "ℹ️ *Biz haqimizda:*\n\n"
            "🏫 Do It School — bu zamonaviy o'quv markazi!\n\n"
            "Bizda oliy ma'lumotli o'qituvchilar, qulay honalar va eng so'nggi texnologiyalar bilan jihozlangan sinf xonalari mavjud.\n\n"
            "📚 Kurslar: Ingliz tili, Matematika, Robototexnika, IT\n"
            "📍 Manzil: Bo'stonliq tumani, So'yliq qishlog'i\n"
            "📞 Tel: +998 99 468 70 20\n"
            "👤 Admin: @radnoy_ustoz",
            parse_mode="Markdown"
        )

def main():
    keep_alive()
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == "__main__":
    main()
