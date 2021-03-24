from bs4 import Tag, BeautifulSoup as bs
import requests
import time
import lxml


def get_request(url):
    response = requests.get(url)
    content = response.content.decode('utf-8')
    soup = bs(content, 'lxml')
    return soup


def get_initial_urls(soup):
    letters = soup.find('span', {'style': 'white-space:nowrap'}).contents
    return list(map(lambda letter: letter.get('href'), filter(lambda letter: type(letter) == Tag, letters)))


def each_page(url):
    soup = get_request(url)
    animals_blocks = soup.select('div.mw-category-group')
    alpha = animals_blocks[0].next.text
    while True:
        _next_page = soup.find('div', {'id': 'mw-pages'}).contents
        next_page = (map(lambda item: 'https://ru.wikipedia.org' + item.get('href'),
                     filter(lambda item: type(item) == Tag and 'След' in item.text, _next_page))).__next__()
        if register_animals(animals_blocks[0], alpha) is False:
            break
        soup = get_request(next_page)
        animals_blocks = soup.select('div.mw-category-group')


animals_dict = {'name': 'count'}


def register_animals(animals_block: Tag, main_alpha):
    alpha = animals_block.next.text
    if main_alpha != alpha:
        return False
    global animals_dict
    full_animals_list = animals_block.select('ul')[0].contents
    animal_count = len(list(map(lambda animal: 1, filter(lambda animal: type(animal) == Tag, full_animals_list))))
    animal_new_count = animals_dict.get(alpha)
    if animal_new_count is None:
        animal_new_count = 0
    animals_dict.update({alpha: animal_count + int(animal_new_count)})
    return True


def main():
    start = time.time()
    url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:' \
          '%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%' \
          'D1%83&from=%D0%90'
    soup = get_request(url)
    urls = get_initial_urls(soup)
    list(map(each_page, urls))
    stop = time.time() - start
    global animals_dict
    for key, value in animals_dict.items():
        print(f'{key}: {value}')
    del animals_dict
    print('\n**************************\n')
    print(stop, 'sec')


if __name__ == '__main__':
    main()
