import requests

def get_weather(update, context):
    city = update.message.text
    print(city)
    params = {
        "query": city
    }
    # Задаем значение ключа API
    api_key = '7eac76e1c04f388e46a498c507a7c0a6'

    # Задаем URL API
    url = 'http://api.weatherstack.com/current?access_key=7eac76e1c04f388e46a498c507a7c0a6'

    # Делаем запрос к API
    response = requests.get(url, params=params)

    # Проверяем статус ответа
    if response.status_code == 200:
        # Преобразуем ответ в JSON формат
        data = response.json()
        update.message.reply_text(
            f'Температура воздуха: {data["current"]["temperature"]} °C '
            f'\n Ощущается как: {data["current"]["feelslike"]} °C \n Скорость ветра: {data["current"]["wind_speed"]} м/с'
            f' \n Давление: {data["current"]["pressure"]} мм рт. ст. \n Влажность: {data["current"]["humidity"]} %')
    else:
        # Выводим код ошибки
        update.message.reply_text(f'Ошибка: {response.status_code}')

