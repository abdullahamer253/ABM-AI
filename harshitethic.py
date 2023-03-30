
import telebot
import openai

# إنشاء كائن من فئة TeleBot وإدخال رمز الترميز الخاص بالبوت
bot = telebot.TeleBot("5794438845:AAGwYnguPlnRwH7gMSyjIUZSjkx8OF6fg9Y")

# تعيين مفتاح واجهة برمجة التطبيقات الخاص بGPT3
openai.api_key = "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"

# تعريف دالة للتعامل مع جميع أنواع الرسائل
@bot.message_handler(func=lambda message: True)
def chat_message(message):
    # إرسال رسالة تفيد بأن البوت يقوم بالكتابة
    bot.send_chat_action(message.chat.id, "typing")
    # استخدام نموذج davinci من GPT3 لتوليد رد على الرسالة التي تلقاها البوت
    response = openai.Completion.create(
        engine="davinci",
        prompt=message.text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n"]
    )
    # إرسال الرد المولد إلى المستخدم
    bot.reply_to(message, response["choices"][0]["text"])

# بدء حلقة التلقي (polling) للاستماع إلى الرسائل
bot.polling()
