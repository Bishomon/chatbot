import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters, CallbackQueryHandler, \
    ChatMemberHandler
from telegram.error import BadRequest
import pandas as pd
import Texts
import Keyboards
import logging

logging.basicConfig(level=logging.INFO)
msg_dict = {}
async def del_msg(effective_chat_id,context: CallbackContext)-> None:
    if effective_chat_id in msg_dict:
        for message_id in msg_dict[effective_chat_id]:
            try:
                # Проверка существования сообщения
                await context.bot.delete_message(chat_id=effective_chat_id, message_id=message_id)
            except Exception as e:
                logging.error(f"Error deleting message {message_id} in chat {effective_chat_id}: {e}")
        # Очистка списка после удаления сообщений
    msg_dict[effective_chat_id] = []

async def add_msg(msg, update: Update) -> None:
   # context.user_data['start_message_id'] = msg.message_id
    #context.user_data['start_message_text'] = msg.text
    #context.user_data['message_ids'].append(msg.message_id)
   # context.user_data['chat_id'] = update.effective_chat.id
    #context.bot.deleteMessage(message_id=msg.message_id)
   # context.bot.delete_message(message_id=msg.message_id, chat_id=update.effective_chat.id)
    if update.effective_chat.id not in msg_dict:
        msg_dict[update.effective_chat.id] = []
    msg_dict[update.effective_chat.id].append(msg.message_id)



async def start(update: Update, context: CallbackContext) -> None:
    await del_msg(update.effective_chat.id,context)
    msg = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Texts.text_start,
        reply_markup=Keyboards.main_menu(), parse_mode='HTML'
    )
    await add_msg(msg, update)

    # Сохраняем идентификатор отправленного сообщения в пользовательских данных


async def menu_option_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    await del_msg(update.effective_chat.id,context)

    # Обрабатываем выбор пользователя в зависимости от кнопки
    if query.data == '1':
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            parse_mode = 'HTML',
            text=Texts.text_1,
            reply_markup=Keyboards.keyboard_1()
        )
        await add_msg(msg, update)

    elif query.data == '1.1':


        # Здесь вы можете добавить код для обработки кнопки "Назад"
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_1_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_1_1()  # Возвращаем основное меню
            )
        await add_msg(msg, update)

    elif query.data == '1.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            parse_mode='HTML',
            text=Texts.text_1_2,
            reply_markup=Keyboards.keyboard_1_2())
        await add_msg(msg, update)

        # Обработка других кнопок

    if query.data == '2':
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_2,
            reply_markup=Keyboards.keyboard_2()
        )
        await add_msg(msg, update)
    elif query.data == '2.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_2_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_2_1())
        await add_msg(msg, update)

    elif query.data == '2.1.1':
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_2_1_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_2_1_1()

                # Возвращаем основное меню
            )
        await add_msg(msg, update)
    elif query.data == '2.1.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_2_1_2,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_2_1_2())
        await add_msg(msg, update)

    elif query.data == '2.1.3':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_2_1_3,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_2_1_3()
                # Возвращаем основное меню
            )
        await add_msg(msg, update)

    elif query.data == '2.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_2_2,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_2_2())
        await add_msg(msg, update)

    elif query.data == '2.2.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_2_2_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_2_2_1())
        await add_msg(msg, update)

    if query.data == "3":
        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_3,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_3()
        )
        await add_msg(msg, update)
    elif query.data == '3.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_3_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_3_1())
        await add_msg(msg, update)

    elif query.data == '3.1.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_3_1_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_3_1_1())
        await add_msg(msg, update)

    elif query.data == '3.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_3_2,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_3_2())
        await add_msg(msg, update)

    if query.data == "4":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_4,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_4()
        )
        await add_msg(msg, update)

    elif query.data == '4.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_4_1,
            reply_markup=Keyboards.keyboard_4_1())
        await add_msg(msg, update)

    if query.data == "5":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5,
            reply_markup=Keyboards.keyboard_5()
        )
        await add_msg(msg, update)
    elif query.data == '5.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_1())
        await add_msg(msg, update)

    elif query.data == '5.1.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_1_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_1_1())
        await add_msg(msg, update)

    elif query.data == '5.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2())
        await add_msg(msg, update)
    elif query.data == '5.2.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2_1())
        await add_msg(msg, update)

    elif query.data == '5.2.1.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_1_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2_1_1())

        await add_msg(msg, update)

    elif query.data == '5.2.1.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_1_2,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2_1_2())
        await add_msg(msg, update)

    elif query.data == '5.2.1.3':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_1_3,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2_1_3()
            )
        await add_msg(msg, update)

    elif query.data == '5.2.2':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_2,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2())
        await add_msg(msg, update)
    elif query.data == '5.2.2.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_2_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2_2_1())
        await add_msg(msg, update)

    elif query.data == '5.2.3':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_3,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2_3())

        await add_msg(msg, update)
    elif query.data == '5.2.3.1':

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_5_2_3_1,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_5_2_3_1())

        await add_msg(msg, update)

    if query.data == "8":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_8,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_8()
        )
        await add_msg(msg, update)

    if query.data == "9":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_9,
            parse_mode='HTML',
            reply_markup=Keyboards.keyboard_9()
        )
        await add_msg(msg, update)
    elif query.data == "9.1":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_9_1,
            reply_markup=Keyboards.keyboard_9_1()

        )
        await add_msg(msg, update)
    elif query.data == "9.2":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_9_2,
            reply_markup=Keyboards.keyboard_9_2()
        )
        await add_msg(msg, update)

    if query.data == "back":

        msg = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Texts.text_back,
            reply_markup=Keyboards.main_menu(), parse_mode='HTML'
        )
        # Сохраняем идентификатор отправленного сообщения в пользовательских данных
        await add_msg(msg, update)


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
    application = Application.builder().token("6789966947:AAEfNbQmhCoPoDxP-1MuCaG8CH_Uz9u4lhY").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu_option_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_messages))

    # Run the bot using asyncio.run()
    asyncio.run(application.run_polling(allowed_updates=Update.ALL_TYPES))


if __name__ == '__main__':
    main()
