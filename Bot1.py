
#Бот парсер для @PostCreaterTorgi_bot
import subprocess
import logging
from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup
import time
import os
import codecs
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Dictionary to store posted advertisements with hashtags
advertisements = {}


import re

def remove_inside_brackets(input_string):
    opening_bracket = input_string.find('(')
    closing_bracket = input_string.find(')', opening_bracket)

    if opening_bracket != -1 and closing_bracket != -1:
        modified_string = input_string[:opening_bracket] + input_string[closing_bracket + 1:]
        return modified_string
    else:
        return input_string

# Example usage




def download_image(url, destination):
    response = requests.get(url)

    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"Изображение успешно скачано и сохранено в {destination}")
    else:
        print(f"Не удалось скачать изображение. Код статуса: {response.status_code}")

def find_place(position):
    driver = webdriver.Chrome()
    try:
        driver.get('https://yandex.ru/maps/213/moscow/?ll=37.530605%2C55.703106&z=14')
        position = position[len("Местонахождение имущества: "):]
        field_class = 'input__control'

        wait = WebDriverWait(driver, 20)

        field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, field_class)))
        field.clear()
        field.send_keys(position)

        wait.until(EC.text_to_be_present_in_element_value((By.CLASS_NAME, field_class), position))

        current_url = driver.current_url  # Define current_url here

        field.send_keys(Keys.RETURN)

        # Wait until the URL changes

        wait.until(EC.url_changes(current_url))
        time.sleep(2)
        current_url = driver.current_url
        return current_url

    except TimeoutException:
        print("Время ожидания превышено. Производится завершение драйвера.")
        return ''
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()

def parser(link):
    # link = 'https://torgi.gov.ru/new/public/lots/lot/21000004710000008213_1'
    # Создание экземпляра веб-драйвера
    test = link.split(' ')
    option = link.split(' ')[1]
    link = link.split(' ')[0]

    if "torgi.gov.ru" in link:
        lot_num = link.split('/')[-1]
        link = link

    else:
        lot_num = link
        link ="https://torgi.gov.ru/new/public/lots/lot/"+lot_num

    coded = ""
    for i in lot_num:
        if i != "0" and i != "_":
            coded += i
    driver = webdriver.Chrome()

    # Открытие URL в браузере
    driver.get(link)

    # Получение полного HTML-кода страницы
    html_code = driver.page_source

    # Закрытие браузера
    driver.quit()

    soup = BeautifulSoup(html_code, 'html.parser')
    block1 = soup.find('div', class_='form-content')
    lot_attribute1 = block1.find_all('div', class_='lotAttribute')

    time.sleep(1)
    block2 = soup.find('div', class_='tab-form-content')
    lot_attribute2 = block2.find_all('div', class_='attr')

    lot = {}
    test1 = block2.find('app-entity-attribute-simple').text
    lot["Дата и время окончания подачи заявок"] = lot_attribute1[6].text if lot_attribute1[6] is not None else '   '
    lot["Дата проведения торгов"] = lot_attribute1[7].text if lot_attribute1[7] is not None else '   '
    lot["Предмет торгов (наименование лота)"] = soup.find('title').text if soup.find('title') is not None else '   '
    lot["Описание лота"] = block2.find('app-entity-attribute-simple',
                                       {'attributename': 'Описание лота'}).text if block2.find(
        'app-entity-attribute-simple', {'attributename': 'Описание лота'}) is not None else '   '
    lot["Местонахождение имущества"] = block2.find('app-entity-attribute-simple',
                                                   {'attributename': 'Местонахождение имущества'}).text if block2.find(
        'app-entity-attribute-simple', {'attributename': 'Местонахождение имущества'}) is not None else '   '
    lot["Начальная цена"] = block2.find('app-entity-attribute-simple',
                                        {'attributename': 'Начальная цена'}).text if block2.find(
        'app-entity-attribute-simple', {'attributename': 'Начальная цена'}) is not None else '   '
    lot["Размер задатка"] = block2.find('app-entity-attribute-simple',
                                        {'attributename': 'Размер задатка'}).text if block2.find(
        'app-entity-attribute-simple', {'attributename': 'Размер задатка'}) is not None else '   '
    # lot["Изображение"] = 'https://torgi.gov.ru/new/' + soup.find('div', class_='form-images').find_all('img', class_='selected-image-list-item')[0]['src']
    lot["Ссылка"] = "Ссылка " + link

    # n = os.path.join("C:\\Users\\Bishomon\\Desktop\\image\\", "PageSave.html")
    # f = codecs.open(n, "w", "utf−8")
    # f.write(html_code)

    image_url = 'https://torgi.gov.ru/new/' + soup.find('div', class_='form-images').find_all('img', class_='selected-image-list-item')[0]['src']
    n = os.path.join("C:\\Users\\Bishomon\\Desktop\\image\\", "info.txt")
    f = codecs.open(n, "w", "utf−8")

    info = ""
    # info = info+f'❗<b>{ lot["Описание лота"][len("Описание лота") + 2:]}\n</b>❗'

    info = info + f'❗<b>{remove_inside_brackets(lot["Предмет торгов (наименование лота)"])}</b>❗\n'
    info = info + "\n"
    info = info + "&#9200;" + f'<b>Дата и время окончания подачи заявок:</b>' + f'{lot["Дата и время окончания подачи заявок"][len("Дата и время окончания подачи заявок") + 2:]}\n'
    info = info + "&#9200;" + "<b>Дата проведения торгов:</b>" + f'{lot["Дата проведения торгов"][len("Дата проведения торгов") + 2:]}\n'
    info = info + "\n"

    info = info + f'&#128205;<b>Местонахождение имущества:</b>' + f'{lot["Местонахождение имущества"][len("Местонахождение имущества") + 1:]}' + f'<a href="{find_place(lot["Местонахождение имущества"])}"> (открыть карту)</a>\n'
    info = info + "\n"
    info = info + "&#128180;" + "<b>Начальная цена: </b>" + f'{lot["Начальная цена"][len("Начальная цена") + 2:]}\n'
    info = info + "&#128181;" + "<b>Размер задатка:</b>" + f'{lot["Размер задатка"][len("Размер задатка") + 2:]}\n'


    if option == '1':

        info = info + f'<a href="{link}">🌐Ссылка на ГИС Торги🌐</a>\n'
        info = info + "&#11036;" + "<b>Артикул: </b>" + f'{coded}\n'
        print("")

    elif option == '0':
        info = info + "&#11036;" + "<b>Артикул:</b>" + f'{coded}\n'




    download_image(image_url, "C:\\Users\\Bishomon\\Desktop\\image\\image.jpg")
    return "C:\\Users\\Bishomon\\Desktop\\image\\image.jpg", info, image_url, option

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def process_link_with_image(link: str) -> tuple:


    """Process the given link and return the result along with an image path."""
    # You can replace 'your_program.py' with the actual name of your program


    try:
        # Run the command and capture the output
        image_path, result, image_url, option = parser(link)
        return result.strip(), image_path, image_url, option
    except subprocess.CalledProcessError as e:
        print("Problem")


async def post_ad(update: Update, context: Application) -> None:
    """Post an advertisement with a link."""
    user = update.effective_user
    link = update.message.text[len('/post '):].strip()

    # Process the link and get the result along with an image path
    result, image_path, image_url, option = process_link_with_image(link)

    # If an image path is provided, send the image along with the result
    if image_path:
        with open(image_path, 'rb') as photo:
            # Use context.bot.send_photo instead of update.message.reply_photo
            #await context.bot.send_photo(chat_id=update.message.chat_id, photo=photo, caption=result, parse_mode='HTML')
            await context.bot.send_photo(chat_id='@beoger', photo=photo, caption=result, parse_mode='HTML')
    else:

        # If no image path is provided, send only the text result
        await update.message.reply_html(
            f"Result for the link: {result}",
            reply_markup=ForceReply(selective=True),
        )
        await context.bot.send_message(chat_id='@beoger', text=result, parse_mode='HTML')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message with an image."""
    link = update.message.text


    # Process the link and get the result along with an image path
    result, image_path, image_url,option = process_link_with_image(link)


    # If an image path is provided, send the image along with the result
    if image_path:
        with open(image_path, 'rb') as photo:
            #await update.message.reply_photo(photo, caption=result, parse_mode='HTML')
            #await context.bot.send_photo(chat_id='@beoger', photo=image_url, caption=result, parse_mode='HTML')
            try:
                #time.sleep(0.1)
                await context.bot.send_photo(chat_id='@beoger', photo=photo, caption=result, parse_mode='HTML')
            except Exception as e:
                print(f"Error sending photo: {e}")

    else:
        # If no image path is provided, send only the text result
        await update.message.reply_text(result, parse_mode="HTML")
        #await context.bot.send_message(chat_id='@beoger', text=result, parse_mode='HTML')


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6451213766:AAFVmiaay3U-HXvzoK5clKKVhVTbRcoCZHk").build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    # Add message handler for echoing messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()