import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters, CallbackQueryHandler, \
    ChatMemberHandler
from telegram.error import BadRequest
import pandas as pd
import Texts



async def start(update: Update, context: CallbackContext) -> None:
    sent_message = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Texts.text1,
        reply_markup=main_menu(), parse_mode='HTML'

    )

    # Сохраняем идентификатор отправленного сообщения в пользовательских данных
    context.user_data['start_message_id'] = sent_message.message_id


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


async def menu_option_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    try:
        await context.bot.delete_message(chat_id=update.effective_chat.id,
                                         message_id=context.user_data.get('start_message_id'))
    except BadRequest:
        print("Start message not found or unable to delete.")

    # Обрабатываем выбор пользователя в зависимости от кнопки
    if query.data == '1':
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            parse_mode = 'HTML',
            text=Texts.text2,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏅 Хочу всегда видеть полную информацию без ожидания.", callback_data='1.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back')]

            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '1.1':
        text2 = Texts.text3

        # Здесь вы можете добавить код для обработки кнопки "Назад"
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text2,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎯 Оформить подписку", callback_data='1.2')],
                [InlineKeyboardButton("🔙 Назад", callback_data='1')]]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '1.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            parse_mode='HTML',
            text=Texts.text4,
            reply_markup=InlineKeyboardMarkup([

                [InlineKeyboardButton("Назад", callback_data='1.1')]]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text

        # Обработка других кнопок

    if query.data == '2':
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Выберите интересующую помощь",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🚦 Этапы работы", callback_data='2.1')],
                [InlineKeyboardButton("🧮 Тарифы", callback_data='2.2')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '2.1':
        text3 = Texts.text5
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text3,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔜 Этап 2", callback_data='2.1.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '2.1.1':
        text4 = Texts.text6
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text4,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔜 Этап 3", callback_data='2.1.2')],
                [InlineKeyboardButton("🔙 Назад", callback_data='2.1')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]]
                # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '2.1.2':
        text5 = Texts.text7
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text5,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔜 Этап 4", callback_data='2.1.3')],
                [InlineKeyboardButton("🔙 Назад", callback_data='2.1.1')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]]
                # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '2.1.3':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text8,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data='2.1.2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]]
                # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '2.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text9,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📊 Форматы работы", callback_data='2.2.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '2.2.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text10,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data='2.2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text

    if query.data == "3":
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Выберите интересующую помощь",
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔺 Подбор объекта с торгов", callback_data='3.1')],
                [InlineKeyboardButton("🔻 Подбор объекта с открытого рынка", callback_data='3.2')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '3.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text11,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🧮 Тарифы", callback_data='2.2')],
                [InlineKeyboardButton("♦ Отправить заявку", callback_data='3.1.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='3')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '3.1.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text12,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data='3.1')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '3.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text13,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data='3')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text

    if query.data == "4":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text14,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⛳ Земельные участки (Москва и МО)", callback_data='4.1')],
                [InlineKeyboardButton("🏛 Коммерческая недвижимость (Москва и МО)",url='https://web.telegram.org/a/#-1002035303018')],
                [InlineKeyboardButton("🏡 Жилая недвижимость (Москва и МО)", url='https://web.telegram.org/a/#-1002035303018')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '4.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text15,
            reply_markup=InlineKeyboardMarkup([

                [InlineKeyboardButton("🔙 Назад", callback_data='3')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text



    if query.data == "5":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text16,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⛳ Оформление земельного участка", callback_data='5.1')],
                [InlineKeyboardButton("🔎 Осмотр объекта", callback_data='5.2')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text17,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🧮 Прайс", callback_data='5.1.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='5')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.1.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text18,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([

                [InlineKeyboardButton("🔙 Назад", callback_data='5.1')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text19,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🗺 Самостоятельный осмотр", callback_data='5.2.1')],
                [InlineKeyboardButton("📸 Услуга по осмотру объекта", callback_data='5.2.2')],
                [InlineKeyboardButton("⛳ Оформление земельного участка", callback_data='5.2.3')],
                [InlineKeyboardButton("🔙 Назад", callback_data='5')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text20,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔎 Нет кадастрового номера", callback_data='5.2.1.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='5.2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.1.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text21,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔰 Хочу всегда видеть полную информацию без ожидания.", callback_data='5.2.1.2')],
                [InlineKeyboardButton("🔙 Назад", callback_data='5.2.1')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.1.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text22,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎯 Оформить подписку", callback_data='5.2.1.3')],
                [InlineKeyboardButton("🔙Назад", callback_data='5.2.1.1')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.1.3':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text23,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([

                [InlineKeyboardButton("🔙 Назад", callback_data='5.2.1.2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text24,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("♦ Заказать услугу", callback_data='5.2.2.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='5.2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.2.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text25,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([

                [InlineKeyboardButton("🔙 Назад", callback_data='5.2.2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.3':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text26,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🧮 Прайс", callback_data='5.2.3.1')],
                [InlineKeyboardButton("🔙 Назад", callback_data='5.2')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == '5.2.3.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text27,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([

                [InlineKeyboardButton("🔙 Назад", callback_data='5.2.1')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ]  # Возвращаем основное меню
            ))
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text

    if query.data == "8":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text28,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([

                [InlineKeyboardButton("🔙 Назад", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text

    if query.data == "9":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text29,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📬 Оставить заявку", callback_data='9.1')],
                [InlineKeyboardButton("📞 Связь с менеджером", callback_data='9.2')],
                [InlineKeyboardButton("🔙 Назад", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == "9.1":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text30,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Помощь с выкупом", callback_data='2')],
                [InlineKeyboardButton("Подбор объекта", callback_data='3')],
                [InlineKeyboardButton("Осмотр объекта", callback_data='5.2')],
                [InlineKeyboardButton("Оформление земельного участка", callback_data='5.2.3')],
                [InlineKeyboardButton("Назад", callback_data='9')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text
    elif query.data == "9.2":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text31,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Назад", callback_data='9')],
                [InlineKeyboardButton("Главное меню", callback_data='back')]
            ])
        )
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text

    if query.data == "back":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text32,
            reply_markup=main_menu(), parse_mode='HTML'

        )

        # Сохраняем идентификатор отправленного сообщения в пользовательских данных
        context.user_data['start_message_id'] = msg.message_id
        context.user_data['start_message_text'] = msg.text


async def handle_user_messages(update: Update, context: CallbackContext) -> None:
    # Проверяем, что сообщение пришло в ответ на предыдущее меню
    if 'start_message_id' in context.user_data:
        # Получаем данные пользователя из context.user_data
        user_data = context.user_data.get('user_data', {})

        # Получаем текст сообщения пользователя
        user_input = update.message.text

        # Получаем имя пользователя
        username = update.message.from_user.username

        # Добавляем данные в словарь пользователя
        user_data['user_input'] = user_input
        user_data['username'] = username
        user_data['question'] = context.user_data['start_message_text']

        # Обновляем данные пользователя в context.user_data
        context.user_data['user_data'] = user_data

        # Прочитайте существующий файл Excel, если он существует
        try:
            existing_df = pd.read_excel('user_data.xlsx')
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Создайте новый DataFrame из текущих данных пользователя
        new_data = pd.DataFrame.from_dict(user_data, orient='index').T

        # Объедините существующий DataFrame с новыми данными
        updated_df = pd.concat([existing_df, new_data], ignore_index=True)

        # Запишите обновленные данные в Excel-файл
        updated_df.to_excel('user_data.xlsx', index=False)

        # Добавьте вашу логику для реагирования на сообщение пользователя
        # Например, отправка ответа пользователю
        await update.message.reply_text(f"Спасибо, {username}, для продолжения работы нажмите кнопку рестарт в меню")


def main():
    """Start the bot."""
    application = Application.builder().token("6838830099:AAGbGCibVjtsNMLJ4_K57htuS-R5AZa4Hf4").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu_option_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_messages))

    # Run the bot using asyncio.run()
    asyncio.run(application.run_polling(allowed_updates=Update.ALL_TYPES))


if __name__ == '__main__':
    main()
