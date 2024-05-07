import requests
from bs4 import BeautifulSoup


def parse(soup):
    price = soup.findAll('div', class_='card-product__price')
    print(price[0].div.text)

    name = soup.findAll('a', class_='card-product__title')
    print(name[0].text)

    link = soup.findAll('a', class_='card-product__title')
    print(link[0]['href'])

    img = soup.findAll('a', class_='card-product__img')
    print(img[0]['style'])


def main(url):
    for i in range(3):
        if i == 0:
            url_next = url
        else:
            url_next = url+f'page={i+1};/'

        res = requests.get(url_next)
        soup = BeautifulSoup(res.text, "html.parser")
        parse(soup)


if __name__ == '__main__':
    url = 'https://novosibirsk.svetofors.ru/tovari/vostochnie-sladosti/'
    main(url)
