import requests
from bs4 import BeautifulSoup as bs


def parse_url(url: str):
    out_data = []
    for page in range(2, 100):
        req = requests.get(url + f'?page={page}')
        if req.status_code == 200:
            html = bs(req.content, 'html.parser')
            cars = html.find_all('div', class_='card')
            for car in cars:
                name = car.find('a', 'card__name').text.strip()
                date = car.find('div', 'card__date').text.strip().split()[2]
                price = car.find('span', 'card__price-num').text.strip()
                text = car.find('div', 'card__text').text.strip().split()[1]
                out_data.append({'name': name, 'date': date, 'price': price, 'text': text})  # Преобразование в словарь
        else:
            break
    return out_data

def main(url):
    out_data = []
    for i in range(3):
        if i == 0:
            url_next = url
        else:
            url_next = url+f'page={i+1};/'

        res = requests.get(url_next)
        soup = BeautifulSoup(res.text, "html.parser")
        ret = parse(soup)
        out_data.append(ret)
    return out_data


if __name__ == '__main__':
    url = 'https://novosibirsk.svetofors.ru/tovari/vostochnie-sladosti/'
    out = main(url)
    print(out)
