from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard = [
    [KeyboardButton(text='Рассчитать'),
     KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить'),
     KeyboardButton(text='Регистрация')]
]
kb = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

inline_keyboard = [
  [
    InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories'),
    InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
  ]
]
inline_kb = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

buy_menu_keyboard = [
  [
    InlineKeyboardButton(text='Product1',callback_data='product_buying'),
    InlineKeyboardButton(text='Product2', callback_data='product_buying'),
    InlineKeyboardButton(text='Product3', callback_data='product_buying'),
    InlineKeyboardButton(text='Product4', callback_data='product_buying')
  ]
]
buy_menu = InlineKeyboardMarkup(inline_keyboard=buy_menu_keyboard)

inline_keyboard = [
  [
    InlineKeyboardButton(text='Для мужчин',callback_data='for_men'),
    InlineKeyboardButton(text='Для женщин', callback_data='for_women')
  ]
]
formulas_kb = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

inline_keyboard = [
  [
    InlineKeyboardButton(text='Мужской',callback_data='men'),
    InlineKeyboardButton(text='Женский', callback_data='women')
  ]
]
gender_kb = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)