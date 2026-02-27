import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message
from buttons import menu, fanlar , ustozlar

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
bot=Bot(token=TOKEN)


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu aleykum {message.from_user.full_name}\n Menulardan birini tanlang:",reply_markup=menu)

@dp.message(F.text=="16-maktab haqida🏨")
async def about(msg:Message):
    await msg.answer("""Biz haqimizda  🏫 Sirdaryo viloyati, Mirzaobod tumani, Yangi hayot mahallasida joylashgan
       16-sonli maktab — yosh avlodga sifatli ta’lim va tarbiya berishga xizmat qilayotgan ilm maskanlaridan biridir.
       Maktabda o‘quvchilarning bilim olishiga, ma’naviy jihatdan kamol topishiga va kelajakda yetuk shaxs bo‘lib shakllanishiga alohida e’tibor qaratiladi📚✨
       Bu ta’lim dargohida malakali ustozlar o‘quvchilarga zamonaviy bilimlar berib, ularning iste’dod va qobiliyatlarini rivojlantirishga harakat qiladi🌟
       Maktab jamoasi o‘quvchilarning ilmiy yutuqlari, odob-axloqi va vatanparvarlik ruhida tarbiyalanishini muhim deb biladi💛
       16-sonli maktab — orzularga qanot beruvchi, bilimga yo‘l ochuvchi maskandir🌸🏫""")

@dp.message(F.text=="📚Fanlar")
async def courses(msg:Message):
    await msg.answer("Maktab darsliklari📖:",reply_markup=fanlar)


@dp.message(F.text=="🔙orqaga")
async def courses(msg:Message):
    await msg.answer("Asosiy menyu:",reply_markup=menu)


@dp.message(F.text=="👨‍💻Ustozlar")
async def courses(msg:Message):
    await msg.answer("Maktabimiz O`qituvchilari:",reply_markup=ustozlar)


@dp.message(F.text=="📍Manzilimiz")
async def courses(msg:Message):
    await msg.answer("Bizning manzilimiz:")
    await msg.answer_location(40.37742530173317, 68.7853208146311)




@dp.message(F.contact)
async def send_contact(msg: Message):
    phone = msg.contact.phone_number
    name = msg.contact.full_name
    username = msg.from_user.username

    suxbat = f"""📥Yangi murojaat qabul qilindi!

👩Ismi: {name}
📞Nomeri: {phone}
🔗Username: @{username}"""

    await bot.send_message(chat_id=8232948737, text=suxbat)

    await msg.answer("Ariza muvaffaqiyatli ro‘yxatdan o‘tkazildi. Tez orada bog‘lanamiz.✅")




# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    print("uraaaaaa bot ishlayabdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
