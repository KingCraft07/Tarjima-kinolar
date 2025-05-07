import json
def save_kino_baza(data):
    with open('kino_baza.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


import telebot


TOKEN = '7660246680:AAGTpzX2_JO5hh8HYLYArBZm8v1mLcYDIFc'
bot = telebot.TeleBot(TOKEN)


def load_kino_baza():
    try:
        with open('kino_baza.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

kino_baza = load_kino_baza()

@bot.message_handler(func=lambda message: True)
def kod_bilan_izlash(message):
    kod = message.text.strip()
    if kod in kino_baza:
        bot.send_message(message.chat.id, f"Kino topildi: {kino_baza[kod]}")
    else:
        bot.send_message(message.chat.id, "❌ Uzr, bunday kod topilmadi.")
        if kod == "/start":
            bot.send_message(message.chat.id, "Kino kodini yozing")
        elif kod == "/kanal":
            bot.send_message(message.chat.id, "https://t.me/komediya_tarjima_kinolar")

bot.polling()

@bot.message_handler(commands=['add'])
def add_kod(message):
    try:
        _, kod, link = message.text.split(maxsplit=2)


        kino_baza = load_kino_baza()

        kino_baza[kod] = link
        save_kino_baza(kino_baza)

        bot.reply_to(message, f"✅ Kod '{kod}' muvaffaqiyatli qo‘shildi.")
    except:
        bot.reply_to(message, "❌ Noto‘g‘ri format. To‘g‘ri yozing:\n/add kod https://t.me/kanal/123")

