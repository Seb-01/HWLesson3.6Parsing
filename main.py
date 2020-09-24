# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pprint
from bs4 import BeautifulSoup

# определяем список ключевых слов
WEBSITE = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python','CMS','Астрономия', 'Разработка игр', 'IT-инфраструктура','Научно-популярное', 'Софт', 'Компьютерное железо']
desired_hubs=set(KEYWORDS)


def main():

    #получаем страницу со свежими статьями
    ret=requests.get(WEBSITE)
    bs=BeautifulSoup(ret.text,'html.parser')

    #ищем статьи
    articles=bs.find_all('article',class_='post post_preview')
    print(f'Всего найдено статей: {len(articles)}')
    print('_____________________________')
    print('Интересующие нас статьи:')

    #разбираем все статьи и ищем <дата> - <заголовок> - <ссылка>
    art_list=[]
    for i, article in enumerate(articles):
        #ищем нужные нам хабы и складываем их в hubs
        #print(f'Поиск хабов в статье номер {i+1}:')

        site_hubs=article.find_all('a',class_='hub-link')
        for hub in site_hubs:
            pass
            #print(hub.text)

        hubs=set(map(lambda h: h.text,site_hubs))
        #print(hubs)
        #print(desired_hubs)
        #print(desired_hubs.intersection(hubs))

        #проверяем пересечение с заданным списком
        if desired_hubs.intersection(hubs):

            #собираем информацию:
            choice=dict()
            date_=article.find('span','post__time')
            choice['дата']=date_.text
            #print(date_.text)
            header_=article.find('a','post__title_link')
            choice['заголовок'] = header_.text
            #print(header_.text)
            #внимание! Здесь аттрибут ищем:
            ref_=header_.attrs.get('href')
            choice['ссылка'] = ref_
            #print(ref_)

            art_list.append(choice)


    #Результат:
    pprint.pprint(art_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
