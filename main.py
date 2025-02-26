
import telebot
import requests
from model import get_class

# Замени 'YOUR_TELEGRAM_BOT_TOKEN' на токен своего бота
bot = telebot.TeleBot('7942580721:AAH3B3fsVkm14IDS7iHLZ8YrkEvMz3Iof2o')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я бот который рассказывает о глобальных катастрофах. Имеется команды: /catastrophe")

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде /duck возвращает фото утки'''
    image_url = get_duck_image_url()
    bot.send_message(message.chat.id, image_url)

@bot.message_handler(commands=['catastrophe'])
def catasrophe(message):

    bot.send_message(message.chat.id, "Отправьте картинку глобальной катастрофы.")

    @bot.message_handler(content_types=['photo'])
    def handle_docs_photo(message):
        
        '''При отправке изображения, проводит его анализ'''
        # Проверяем, есть ли фотографии
        if not message.photo:
            return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")

        # Получаем файл и сохраняем его
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = file_info.file_path.split('/')[-1]

        # Загружаем файл и сохраняем
        downloaded_file = bot.download_file(file_info.file_path)
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Анализируем изображение
        result = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=file_name)

        if result == "Iceberg":
            bot.send_message(message.chat.id, "Глобальное потепление ускоряет таяние ледников, что повышает уровень океанов и угрожает экосистемам. Чтобы замедлить этот процесс, можно ехать на велосипеде или ходить пешком, а также экономить энергию, выбирая энергосберегающие лампочки и выключая приборы.")

        if result == "Volcano":
            bot.send_message(message.chat.id, "Вулканы опасны для людей. Лавовые потоки и пирокластические облака уничтожают всё на пути. Пепел загрязняет воздух и воду, а лахары сметают целые поселения. Токсичные газы вызывают удушье, а подводные извержения – цунами. Крупные извержения могут изменить климат. Эвакуация и мониторинг помогают снизить риски.")

        if result == "Plastic":
            bot.send_message(message.chat.id, "Пластик загрязняет природу, убивает животных и разлагается сотни лет. Микропластик уже найден в пище и воде.Решение – сократить использование: выбирать многоразовые вещи, перерабатывать отходы, поддерживать экологичные материалы. Законы и запреты на пластик также помогают. Маленькие шаги каждого могут спасти планету.")

        if result == "Hurricane":
            bot.send_message(message.chat.id, "Ураганы – мощные штормы, разрушающие дома и вызывающие наводнения. Сильный ветер и ливни приводят к жертвам. Защита – эвакуация, укрепление зданий и климатические меры для снижения их силы.")

        if result == "Nuclear":
            bot.send_message(message.chat.id, "Ядерное оружие уничтожает города, убивает миллионы и загрязняет природу. Взрывы вызывают пожары, радиацию и ядерную зиму. Предотвратить катастрофу можно через разоружение, международные договоры и контроль.")

@bot.message_handler(commands=['facts'])
def facts(message):
    bot.send_message(message.chat.id, "Отправьте картинку глобальной катастрофы")

    @bot.message_handler(content_types=['photo'])
    def handle_docs_photo(message):
        # Проверяем, есть ли фотографии
        if not message.photo:
            return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")

        # Получаем файл и сохраняем его
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = file_info.file_path.split('/')[-1]

        # Загружаем файл и сохраняем
        downloaded_file = bot.download_file(file_info.file_path)
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

            result_one = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=file_name)

            if result_one == "Iceberg":
                bot.send_message(message.chat.id, "1. Глобальное потепление повышает температуру и уровень океанов.")
                bot.send_message(message.chat.id, "2. Главная причина — выбросы парниковых газов.")
                bot.send_message(message.chat.id, "3. Потепление вызывает экстремальные погодные явления.")

            if result_one == "Volcano":
                bot.send_message(message.chat.id, "1. Вулканы извергают лаву, пепел и газы.")
                bot.send_message(message.chat.id, "2. Извержения могут вызывать разрушения и цунами.")
                bot.send_message(message.chat.id, "3. Вулканическая активность влияет на климат, повышая температуру.")

            if result_one == "Plastic":
                bot.send_message(message.chat.id, "1. Пластик разлагается сотни лет, загрязняя природу.")
                bot.send_message(message.chat.id, "2. Микропластик попадает в воду и пищу.")
                bot.send_message(message.chat.id, "3. Переработка пластика помогает снизить его воздействие.")

            if result_one == "Hurricane":
                bot.send_message(message.chat.id, "1. Ураганы — это мощные тропические штормы с сильными ветрами и дождями.")
                bot.send_message(message.chat.id, "2. Они могут вызывать разрушения, наводнения и жертвы.")
                bot.send_message(message.chat.id, "3. Ураганы усиливаются из-за глобального потепления. ")

            if result_one == "Nuclear":
                bot.send_message(message.chat.id, "1. Ядерное оружие вызывает массовые разрушения и гибель людей.")
                bot.send_message(message.chat.id, "2. Радиоактивное загрязнение от взрывов остается на десятки лет.")
                bot.send_message(message.chat.id, "3. Ядерные взрывы могут вызвать ядерную зиму и глобальный голод.")



# Запускаем бота
bot.polling()