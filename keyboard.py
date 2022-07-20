from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram import types

AdminMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать рассылку"),
        ],
        [
            KeyboardButton(text="Редактировать каталог"),
        ],
        [
            KeyboardButton(text="Статистика"),
            KeyboardButton(text="Базы данных")
        ]
    ],
    resize_keyboard=True
)

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог видеокарт"),
        ],
        [
            KeyboardButton(text="Подробнее о видеокартах"),
        ],
        [
            KeyboardButton(text="О нас"),
            KeyboardButton(text="Сделать предзаказ")
        ],
    ],
    resize_keyboard=True
)
about_us = InlineKeyboardMarkup()
about_us.add(types.InlineKeyboardButton(text="Инстаграм", url="https://www.instagram.com/f1car_ds/"))
about_us.add(types.InlineKeyboardButton(text="Администратор", url="tg://user?id=787329642"))


cards_inf = InlineKeyboardMarkup()
cards_inf.add(types.InlineKeyboardButton(text="3090ti LHR", callback_data="3090ti LHR"))
cards_inf.add(types.InlineKeyboardButton(text="3090", callback_data="3090"))
cards_inf.add(types.InlineKeyboardButton(text="3080ti LHR", callback_data="3080ti LHR"))
cards_inf.add(types.InlineKeyboardButton(text="3080", callback_data="3080"))
cards_inf.add(types.InlineKeyboardButton(text="3070ti LHR ", callback_data="3070ti LHR"))
cards_inf.add(types.InlineKeyboardButton(text="3070 LHR", callback_data="3070 LHR"))
cards_inf.add(types.InlineKeyboardButton(text="3060ti LHR ", callback_data="3060ti LHR"))
cards_inf.add(types.InlineKeyboardButton(text="3060 LHR ", callback_data="3060 LHR"))
cards_inf.add(types.InlineKeyboardButton(text="3050 LHR ", callback_data="3050 LHR"))
cards_inf.add(types.InlineKeyboardButton(text="2060 super", callback_data="2060 super"))
cards_inf.add(types.InlineKeyboardButton(text="1660ti", callback_data="1660ti"))
cards_inf.add(types.InlineKeyboardButton(text="1660 super", callback_data="1660 super"))
cards_inf.add(types.InlineKeyboardButton(text="90HX", callback_data="90HX"))
cards_inf.add(types.InlineKeyboardButton(text="6900XT", callback_data="6900XT"))
cards_inf.add(types.InlineKeyboardButton(text="6800XT", callback_data="6800XT"))
cards_inf.add(types.InlineKeyboardButton(text="6800", callback_data="6800"))
cards_inf.add(types.InlineKeyboardButton(text="6700XT", callback_data="6700XT"))
cards_inf.add(types.InlineKeyboardButton(text="6600XT", callback_data="6600XT"))


preorder = InlineKeyboardMarkup()
preorder.add(types.InlineKeyboardButton(text="Продолжить", callback_data="enter"))
preorder.add(types.InlineKeyboardButton(text="Отмена", callback_data="cancel"))


database = InlineKeyboardMarkup()
database.add(types.InlineKeyboardButton(text="Все пользователи", callback_data="alluser"))
database.add(types.InlineKeyboardButton(text="Каталог", callback_data="cat"))
database.add(types.InlineKeyboardButton(text="Статистика каталога", callback_data="stat_cat"))


mailing_list= InlineKeyboardMarkup()
mailing_list.add(types.InlineKeyboardButton(text="Отмена", callback_data="cancel_mail"))


edit_cat= InlineKeyboardMarkup()
edit_cat.add(types.InlineKeyboardButton(text="Отмена", callback_data="cancel_cat"))