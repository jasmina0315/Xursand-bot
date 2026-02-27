from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="16-maktab haqida🏨")],
    [KeyboardButton(text="📚Fanlar"),KeyboardButton(text="👨‍💻Ustozlar")],
    [KeyboardButton(text="📞Nomer qoldirish",request_contact=True),KeyboardButton(text="📍Manzilimiz")]
],resize_keyboard=True)

fanlar=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Ona-tili"),KeyboardButton(text="Matematika")],
    [KeyboardButton(text="Adabiyot"),KeyboardButton(text="Tarix")],
    [KeyboardButton(text="Ingilis-tili"),KeyboardButton(text="Rus-tili")],
    [KeyboardButton(text="Geografiya"), KeyboardButton(text="Texnologiya")],
    [KeyboardButton(text="Fizika"), KeyboardButton(text="Geometriya")],
    [KeyboardButton(text="Chizmachilik"), KeyboardButton(text="Informatika")],
    [KeyboardButton(text="Rus-tili"), KeyboardButton(text="Tarbiya")],
    [KeyboardButton(text="🔙orqaga")],
],resize_keyboard=True)

ustozlar=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Maktabimiz Drektori: Yorbekov Jahongir")],
    [KeyboardButton(text="Pardayev Muhammad"),KeyboardButton(text="Nazarov O`tkir")],
    [KeyboardButton(text="Mamatqobilova Gavhar"),KeyboardButton(text="Davronova Dilfuza")],
    [KeyboardButton(text="Davronov Dilmurod"),KeyboardButton(text="Norbekov Muhammad")],
    [KeyboardButton(text="Sodiqov O`tkir"), KeyboardButton(text="Ummatqulov Salohiddin")],
    [KeyboardButton(text="Muminova Niso"), KeyboardButton(text="Yarbekov Jamshid")],
    [KeyboardButton(text="Jumaboyev To`lqin"), KeyboardButton(text="Bo`yqo`ziyev Bobur")],
    [KeyboardButton(text="Maxkamov Bahtiyor"), KeyboardButton(text="Qurbonova Gulnora")],
    [KeyboardButton(text="Mavlonova Ziyoda"), KeyboardButton(text="Mirzayeva Shaxlo")],
    [KeyboardButton(text="Sodiqova Dildora"), KeyboardButton(text="Qurolova Iroda")],
    [KeyboardButton(text="Mahkamov Samandar"), KeyboardButton(text="Xalilov Elbek")],
    [KeyboardButton(text="🔙orqaga")],
],resize_keyboard=True)
