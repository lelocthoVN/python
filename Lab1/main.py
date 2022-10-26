import logging
from bs4 import BeautifulSoup
import requests
import os

URL = "https://yandex.ru/images/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

def creat_directory(path,folder):
    """
    Создать путь для сохранения изображения
    :param path: путь к файлу для работы
    :param folder: имя файла для создания
    :return: Нет возвращаемого значения
    """
    try:
        new_directory = os.path.join(path,folder)
        os.makedirs(new_directory)
    except OSError as err:
        logging.info(f'При создании файл {folder} есть ошибки \n {err}')

def save_image(image_url, name, index):
    """
    сохранение спарсенной картинки в определенную папку

    :param image_url: местоположение (URL) внешнего изображения на который ссылается тег
    :param name: имя папки, в которой сохранены фотографии, а также ключевое слово для поиска
    :param index: порядковый номер изображения в файле
    :return: Нет возвращаемого значения
    """

    picture = requests.get(f"https:{image_url}", HEADERS)
    with open(os.path.join("dataset",name,f"{index:04d}.jpg"), "wb") as f:
        f.write(picture.content)

def download_img(key):
    """
    сохранить изображение из ссылки в файл по ключевому слову

    :param path: путь к папке, в которой сохранено изображение
    :param key: имя папки, в которой сохранены фотографии, а также ключевое слово для поиска
    :return: Нет возвращаемого значения
    """
    page = 0
    count = 1
    rep = requests.get(f'{URL}search?p={page}&text={key}', HEADERS)
    soup = BeautifulSoup(rep.text, "lxml")
    images = soup.findAll('img', class_='serp-item__thumb justifier__thu
    while count <= 1000:
        print(page)
        for image in images:
            if count > 1000:
                print('Загрузка завершена')
                return
            image_url = image.get("src")  # получить тег SRC со ссылкой на изображение
            if (image_url != ""):
                save_image(image_url, key, count)
                count += 1
            page += 1
        print("Cохранения изображений")


if __name__ == "__main__":
    path = os.path.join(os.getcwd(),'dataset')
    creat_directory(path, 'dog')
    creat_directory(path, 'cat')
    download_img('dog')
    download_img('cat')

