from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ==================== [ بيانات التعديل السريع ] ====================
TOKEN = "8923734387:AAE-2xYNOoXO2IvG62EV8gCEnEUNqE6Bg8M"

ADMIN_HANDLE = "https://t.me/4m_t"
CHANNEL_URL = "https://t.me/lqp1q"

LIBYANA_NUMBER = "ضع_رقم_ليبيانا_هنا"
USDT_ADDRESS = "ضع_عنوان_محفظة_USDT_هنا"
TON_ADDRESS = "ضع_عنوان_محفظة_TON_هنا"
# ==================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 شحن ألعاب", callback_data='cat_games'), InlineKeyboardButton("📱 شحن تطبيقات", callback_data='cat_apps')],
        [InlineKeyboardButton("🚀 خدمات الرشق والزيادة", callback_data='cat_boost')],
        [InlineKeyboardButton("💳 طرق الدفع المتاحة", callback_data='payment_methods')],
        [InlineKeyboardButton("📢 قناتنا الرسمية", url=CHANNEL_URL), InlineKeyboardButton("💬 الدعم الفني", url=ADMIN_HANDLE)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = (
        "👋 **أهلاً بك في متجر الخدمات الرقمية!**\n\n"
        "ℹ️ **ملاحظة:** يتم تنفيذ الطلبات بشكل **يدوي** لضمان الأمان، وقد يستغرق الشحن بعض الوقت بعد استلام الطلب.\n\n"
        "👇 اختر القسم المطلوب من القائمة أدناه:"
    )
    
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'payment_methods':
        keyboard = [[InlineKeyboardButton("🔙 الرجوع للقائمة الرئيسية", callback_data='main_menu')]]
        pay_text = (
            "💳 **طرق الدفع المتاحة لدينا:**\n\n"
            f"📱 **رصيد ليبيانا:** `{LIBYANA_NUMBER}`\n"
            f"🪙 **USDT (TRC20):** `{USDT_ADDRESS}`\n"
            f"💎 **TON Network:** `{TON_ADDRESS}`\n\n"
            "📌 عند التحويل، يرجى الاحتفاظ بصورة أو إثبات التحويل وإرسالها للإدارة."
        )
        await query.edit_message_text(pay_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif query.data == 'cat_games':
        keyboard = [
            [InlineKeyboardButton("💎 شدات ببجي", callback_data='item_pubg'), InlineKeyboardButton("🔥 جواهر فري فاير", callback_data='item_ff')],
            [InlineKeyboardButton("🔙 الرجوع للقائمة الرئيسية", callback_data='main_menu')]
        ]
        await query.edit_message_text("🎮 **قسم شحن الألعاب**\n\nاختر الخدمة المطلوبة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif query.data == 'cat_apps':
        keyboard = [
            [InlineKeyboardButton("⭐ اشتراك تليجرام مميز", callback_data='item_tg'), InlineKeyboardButton("🟡 كواي / تيك توك", callback_data='item_coins')],
            [InlineKeyboardButton("🔙 الرجوع للقائمة الرئيسية", callback_data='main_menu')]
        ]
        await query.edit_message_text("📱 **قسم شحن التطبيقات**\n\nاختر الخدمة المطلوبة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif query.data == 'cat_boost':
        keyboard = [
            [InlineKeyboardButton("👥 أعضاء تليجرام", callback_data='item_boost_tg'), InlineKeyboardButton("❤️ متابعين / لايكات", callback_data='item_boost_social')],
            [InlineKeyboardButton("🔙 الرجوع للقائمة الرئيسية", callback_data='main_menu')]
        ]
        await query.edit_message_text("🚀 **قسم خدمات الرشق والزيادة**\n\nاختر الخدمة المطلوبة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif query.data.startswith('item_'):
        keyboard = [
            [InlineKeyboardButton("💳 عرض بيانات الدفع", callback_data='payment_methods')],
            [InlineKeyboardButton("📩 إرسال الطلب والإثبات للدعم", url=ADMIN_HANDLE)],
            [InlineKeyboardButton("🔙 الرجوع للقائمة الرئيسية", callback_data='main_menu')]
        ]
        
        await query.edit_message_text(
            "📝 **خطوات إتمام الطلب اليدوي:**\n\n"
            "1️⃣ قم باختيار طريقة الدفع المناسبة (ليبيانا / USDT / TON).\n"
            "2️⃣ قم بتحويل المبلغ المطلوب لحساب الدفع.\n"
            "3️⃣ أرسل **الـ ID أو رابط الحساب** + **صورة إثبات التحويل** إلى الدعم الفني.\n\n"
            "⏳ *ملاحظة: يتم تنفيذ الطلب يدويًا في أقرب وقت ممكن بعد التحقق من التحويل.*",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif query.data == 'main_menu':
        await start(update, context)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("البوت يعمل الآن...")
    app.run_polling()
