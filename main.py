from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from Init import dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types
from send_mail import send_mail_preorder
from keyboard import Menu, about_us, cards_inf, preorder
from mysql_connect import sql_write_AllUsers, get_catalog, get_url_allusers, write_catalog_stat
from itertools import chain
class main(StatesGroup):
    PreOrder = State()
    Female = State()
    PreOrderEnter = State()


@dp.message_handler(commands=['start'], state="*")
async def start(message: Message, state: FSMContext):
    await message.answer(text="Здравствуйте! Меня зовут ВАЛЛ-И. Я помогу вам подобрать видеокарту. Чтобы посмотреть все видеокарты "
                              "перейдите во вкладку <b>Каталог видеокарт</b>. Полное описание с прибыльностью в майнинге вы можете "
                              "найти во вкладке <b>Подробнее о видеокартах</b>. Подробная информация об осуществлении предзаказа находится во вкладке <b>сделать предзаказ</b>. "
                              "Для покупки видеокарты напишите админу или в наш инстаграм аккаунт, ссылка на который находится в категории <b>О Нас</b>.", reply_markup=Menu)
    username = message.from_user.username
    user_id = message.from_user.id
    url = message.from_user.url
    fullname = message.from_user.full_name
    all_url = chain.from_iterable(get_url_allusers())
    for i in all_url:
        if i == url:
            return
    sql_write_AllUsers(username, url, fullname, user_id)
    await state.finish()
    pass


@dp.message_handler(Text(equals=["Каталог видеокарт"]), state="*")
async def catalog(message: Message):
    user = message.from_user.id
    date = message.date
    text = list(get_catalog()[0])
    await message.answer(text=text[0])
    write_catalog_stat(user, date)
    pass


@dp.message_handler(Text(equals=["Сделать предзаказ"]), state="*")
async def catalog(message: Message, state: FSMContext):
    await message.answer(text="По предзаказу доступны все видеокарты, представленные в каталоге. При покупке по предзаказу, вы получите скидку 10-20% в зависимости от суммы заказа:\n"
                              "до 1000$ - 10%\n1000$-3000$-15%\n3000$-5000$-20%\nДоставка по предзаказу займет 4-8 недель. Вы можете сделать предзаказ через меня, нажав кнопку продолжить."
                              "Также вы можете написать администратору в телеграм или в наш инстаграм аккаунт", reply_markup=preorder)
    await main.PreOrder.set()
    pass


@dp.callback_query_handler(text="enter", state=main.PreOrder)
async def pre_order(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="Напишите ваш предзаказ", reply_markup=Menu)
    await main.PreOrderEnter.set()
    pass


@dp.message_handler(state=main.PreOrderEnter)
async def catalog(message: Message, state: FSMContext):
    TextPreOrder = message.text
    InfPreOrder = message.from_user.username
    user = message.from_user.id
    send_mail_preorder(TextPreOrder, str(user))
    await message.answer(text="Ваш заказ получен.", reply_markup=Menu)
    await state.finish()
    pass


@dp.callback_query_handler(text="cancel", state=main.PreOrder)
async def cancel_pre_order(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="Предзаказ отменен", reply_markup=Menu)
    await state.finish()
    pass

@dp.message_handler(Text(equals=["Подробнее о видеокартах"]), state='*')
async def catalog(message: Message, state: FSMContext):
    await message.answer(text="Подробнее о видеокарте:", reply_markup=cards_inf)
    pass


@dp.message_handler(Text(equals=["О нас"]), state='*')
async def about_uss(message: Message, state: FSMContext):
    await message.answer(text="F1-cards поставляет оригинальные видеокарты Gigabyte, Asus, Palit и других производителей по самым низким ценам."
                          "Вы можете как приобрести карты со склада, так и сделать предзаказ. При покупке по предзаказу вы получите скидку 10-20%."
                          "Подробнеее во вкладке сделать предзаказ. Чтобы сделать заказ, напишите администратору в телеграм или в инстаграм аккаунт."
             "до 20%.", reply_markup=about_us)
    pass
