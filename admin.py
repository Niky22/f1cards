from itertools import chain
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from Init import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types
from keyboard import AdminMenu, database, mailing_list, edit_cat
from mysql_connect import write_catalog, get_numberusers, get_numbercatalog, get_id_allusers, allusers, catalog, stat_catalog
NewCatalog = ""

class reg(StatesGroup):
    Admin = State()
    Catalog = State()
    ColdCalling = State()
    db = State()

@dp.message_handler(commands=['admin'], state="*")
async def admin(message: Message, state: FSMContext):
    await message.answer(text="Введите пароль", reply_markup=ReplyKeyboardRemove())
    await reg.Admin.set()

    @dp.message_handler(state=reg.Admin)
    async def check_password(message: Message, state: FSMContext):
        if message.text == "Nikita2303":
            await message.answer(text="Вы успешно вошли в меню админа", reply_markup=AdminMenu)
        pass

    pass


@dp.message_handler(Text(equals=["Редактировать каталог"]), state=reg.Admin)
async def edit_catalog(message: Message, state: FSMContext):
    await message.answer(text="Введите новый каталог", reply_markup=edit_cat)
    await reg.Catalog.set()
    pass


@dp.callback_query_handler(text="cancel_cat", state=reg.Catalog)
async def cancelcat(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Редактирование каталога отменено')
    await reg.Admin.set()
    pass


@dp.message_handler(state=reg.Catalog)
async def get_catalog(message: Message, state: FSMContext):
    date = message.date
    write_catalog(str(message.text), date)
    await message.answer(text="Каталог обновлен")
    await reg.Admin.set()
    pass


@dp.message_handler(Text(equals=["Создать рассылку"]), state=reg.Admin)
async def make_coldcalling(message: Message, state: FSMContext):
    await message.answer(text="Введите текст рассылки", reply_markup=mailing_list)
    await reg.ColdCalling.set()
    pass


@dp.callback_query_handler(text="cancel_mail", state=reg.ColdCalling)
async def cancelmail(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="Создание рассылки отменено")
    await reg.Admin.set()
    pass


@dp.message_handler(state=reg.ColdCalling)
async def get_coldcalling(message: Message, state: FSMContext):
    allusers = chain.from_iterable(get_id_allusers())
    count = 0
    for i in allusers:
        await bot.send_message(chat_id=i, text=message.text)
        count = count + 1
    await message.answer(text="Рассылка отправлена для "+str(count)+" пользователей")
    await reg.Admin.set()
    pass


@dp.message_handler(Text(equals=["Статистика"]), state=reg.Admin)
async def show_preorders(message: Message, state: FSMContext):
    numberusers = get_numberusers()[0][0]
    numbercatalog = get_numbercatalog()[0][0]
    text = "Хьюстон у нас проблемы"+"\nВсего зарегистрировалось пользователей: "+str(numberusers)+"\nКоличество просмотров каталога: "+str(numbercatalog)
    await message.answer(text=text)
    pass


@dp.message_handler(Text(equals=["Базы данных"]), state=reg.Admin)
async def show_preorders(message: Message, state: FSMContext):
    await message.answer(text="Выберите базу данных", reply_markup=database)
    await reg.db.set()
    pass


@dp.callback_query_handler(text="alluser", state=reg.db)
async def show_allusers(call: types.CallbackQuery, state: FSMContext):
    text = ""
    await call.message.answer(text=allusers())
    await reg.Admin.set()
    pass


@dp.callback_query_handler(text="cat", state=reg.db)
async def show_catalog(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text=catalog())
    await reg.Admin.set()
    pass


@dp.callback_query_handler(text="stat_cat", state=reg.db)
async def show_catalogstat(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text=stat_catalog())
    await reg.Admin.set()
    pass