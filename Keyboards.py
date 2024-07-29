from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🌐 Больше информации о лоте", callback_data='1')],
        [InlineKeyboardButton("📝 Помощь с выкупом", callback_data='2')],
        [InlineKeyboardButton("📌 Подбор объекта", callback_data='3')],
        [InlineKeyboardButton("🔐 Закрытый каталог объектов", callback_data='4')],
        [InlineKeyboardButton("📑 Другие услуги", callback_data='5')],
       # [InlineKeyboardButton("Закрытый каталог объектов", callback_data='6')],
        #[InlineKeyboardButton("Частые вопросы", callback_data='7')],
        [InlineKeyboardButton("📞 Связь с менеджером", callback_data='8')],
        [InlineKeyboardButton("🏆 О нас", callback_data='9')],

    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_1():
    keyboard = [
        [InlineKeyboardButton("🏅 Хочу всегда видеть полную информацию без ожидания.", callback_data='1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_1_1():
    keyboard = [
        [InlineKeyboardButton("🎯 Оформить подписку", callback_data='1.2')],
        [InlineKeyboardButton("🔙 Назад", callback_data='1')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_1_2():
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='1.1')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_2():
    keyboard = [
        [InlineKeyboardButton("🚦 Этапы работы", callback_data='2.1')],
        [InlineKeyboardButton("🧮 Тарифы", callback_data='2.2')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_2_1():
    keyboard = [
        [InlineKeyboardButton("🔜 Этап 2", callback_data='2.1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_2_1_1():
    keyboard = [
        [InlineKeyboardButton("🔜 Этап 3", callback_data='2.1.2')],
        [InlineKeyboardButton("🔙 Назад", callback_data='2.1')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_2_1_2():
    keyboard = [
        [InlineKeyboardButton("🔜 Этап 4", callback_data='2.1.3')],
        [InlineKeyboardButton("🔙 Назад", callback_data='2.1.1')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_2_1_3():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='2.1.2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_2_2():
    keyboard = [
        [InlineKeyboardButton("📊 Форматы работы", callback_data='2.2.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_2_2_1():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='2.2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_3():
    keyboard = [
        [InlineKeyboardButton("🔺 Подбор объекта с торгов", callback_data='3.1')],
        [InlineKeyboardButton("🔻 Подбор объекта с открытого рынка", callback_data='3.2')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_3_1():
    keyboard = [
        [InlineKeyboardButton("🧮 Тарифы", callback_data='2.2')],
        [InlineKeyboardButton("♦ Отправить заявку", callback_data='3.1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='3')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_3_1_1():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='3.1')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_3_2():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='3')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_4():
    keyboard = [
        [InlineKeyboardButton("⛳ Земельные участки (Москва и МО)", callback_data='4.1')],
        [InlineKeyboardButton("🏛 Коммерческая недвижимость (Москва и МО)", url=Texts.url1)],
        [InlineKeyboardButton("🏡 Жилая недвижимость (Москва и МО)", url=Texts.url1)],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_4_1():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='3')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_5():
    keyboard = [
        [InlineKeyboardButton("⛳ Оформление земельного участка", callback_data='5.1')],
        [InlineKeyboardButton("🔎 Осмотр объекта", callback_data='5.2')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_5_1():
    keyboard = [
        [InlineKeyboardButton("🧮 Прайс", callback_data='5.1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='5')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_5_1_1():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='5.1')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_5_2():
    keyboard = [
        [InlineKeyboardButton("🗺 Самостоятельный осмотр", callback_data='5.2.1')],
        [InlineKeyboardButton("📸 Услуга по осмотру объекта", callback_data='5.2.2')],
        [InlineKeyboardButton("⛳ Оформление земельного участка", callback_data='5.2.3')],
        [InlineKeyboardButton("🔙 Назад", callback_data='5')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_5_2_1():
    keyboard = [
        [InlineKeyboardButton("🔎 Нет кадастрового номера", callback_data='5.2.1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='5.2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_5_2_1_1():
    keyboard = [
        [InlineKeyboardButton("🔰 Хочу всегда видеть полную информацию без ожидания.", callback_data='5.2.1.2')],
        [InlineKeyboardButton("🔙 Назад", callback_data='5.2.1')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_5_2_1_2():
    keyboard = [
        [InlineKeyboardButton("🎯 Оформить подписку", callback_data='5.2.1.3')],
        [InlineKeyboardButton("🔙Назад", callback_data='5.2.1.1')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_5_2_1_3():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='5.2.1.2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_5_2_2():
    keyboard = [
        [InlineKeyboardButton("♦ Заказать услугу", callback_data='5.2.2.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='5.2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_5_2_2_1():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='5.2.2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_5_2_3():
    keyboard = [
        [InlineKeyboardButton("🧮 Прайс", callback_data='5.2.3.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='5.2')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)
def keyboard_5_2_3_1():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='5.2.1')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_8():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_9():
    keyboard = [
        [InlineKeyboardButton("📬 Оставить заявку", callback_data='9.1')],
        [InlineKeyboardButton("📞 Связь с менеджером", callback_data='9.2')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_9_1():
    keyboard = [
        [InlineKeyboardButton("Помощь с выкупом", callback_data='2')],
        [InlineKeyboardButton("Подбор объекта", callback_data='3')],
        [InlineKeyboardButton("Осмотр объекта", callback_data='5.2')],
        [InlineKeyboardButton("Оформление земельного участка", callback_data='5.2.3')],
        [InlineKeyboardButton("Назад", callback_data='9')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_9_2():
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='9')],
        [InlineKeyboardButton("Главное меню", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_33():
    keyboard = [
        [InlineKeyboardButton("🏅 Хочу всегда видеть полную информацию без ожидания.", callback_data='1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_34():
    keyboard = [
        [InlineKeyboardButton("🏅 Хочу всегда видеть полную информацию без ожидания.", callback_data='1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)

def keyboard_35():
    keyboard = [
        [InlineKeyboardButton("🏅 Хочу всегда видеть полную информацию без ожидания.", callback_data='1.1')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back')]
    ]

    return InlineKeyboardMarkup(keyboard)