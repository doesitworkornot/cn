import requests
from bs4 import BeautifulSoup
import json

def parse_website(url):
    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-кода страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Найдем элемент <script> с указанным id и типом
        script_element = soup.find('script', id='json-beatmaps', type='application/json')

        # Получаем содержимое элемента в формате JSON
        if script_element:
            json_data = json.loads(script_element.string)
            print(json_data)
        else:
            print("Элемент не найден.")
    else:
        print("Ошибка при запросе:", response.status_code)


# Пример использования:
url = 'https://osu.ppy.sh/beatmapsets'
parse_website(url)