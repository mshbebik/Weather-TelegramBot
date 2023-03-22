import telebot
import requests
import json




# Імпорт телеграм бота, вставте свій токен
bot = telebot.TeleBot('5691607864:AAEaw3RTHE9xxD_m-5ASfq5dRCxNTSC9Cwk')


# Стартова функція запуску бота 
@bot.message_handler(commands=['start'])
def send_welcome(message): 
    bot.send_message(message.chat.id, text="Напишіть місто, в якому ви б хотіли дізнатися погоду (Місто повинно бути вказане на англійскій мові)")


# функція котра приймає написане користувачем місто, записує його до зміннної, потім виводить список по вказаному місту
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    city = message.text
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=cb1657161a4c396d7510303571ee489f".format(city)

    res = requests.get(url)
    json = res.json()
# Вирішив додати смайликів, щоб краще спримати текст виведений ботом
    WeatherInfo = {
        'Місто': json['name'],
        'Країна': (json['sys']['country']),
        'Основний тип погоди ☁' : json['weather'][0]['main'],
        'Температура🌡': round(json['main']['temp'] - 273.15, 1),
        'Мінімальна температура🌡': round(json['main']['temp_min'] - 273.15, 1),
        'Максимальна температура🌡': round(json['main']['temp_max'] - 273.15, 1),
        'Швидкість вітру 💨': json['wind']['speed']
    }
# Вивод повідомлення ботом, по 1 штукі кожний параметр з словника
    bot.send_message(message.chat.id, 'Погода в вибраному місті:')
    for key, value in WeatherInfo.items(): 
     af = f"{key}: {value}"   
     bot.send_message(message.chat.id, f'{af}')
    






bot.infinity_polling()