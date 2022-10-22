from bs4 import BeautifulSoup
import requests
import os

URL = "https://yandex.ru/images/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}


def get_image(image_url, name, index):
    """
    сохранение спарсенной картинки в определенную папку

    :param image_url: местоположение (URL) внешнего изображения на который ссылается тег
    :param name: имя папки, в которой сохранены фотографии, а также ключевое слово для поиска
    :param index: порядковый номер изображения в файле
    :return: Нет возвращаемого значения
    """

    if not os.path.isdir(name):  # проверить наличие каталога "name"
        os.mkdir(name)  # если "name" не существует, создайте каталог "name"
    picture = requests.get(f"https:{image_url}", HEADERS)
    saver = open(os.path.join(f"{name}/{str(index).zfill(4)}.jpg"), "wb")
    saver.write(picture.content)
    saver.close()


def download_img(path, key):
    """
    :param path: путь к папке, в которой сохранено изображение
    :param key: имя папки, в которой сохранены фотографии, а также ключевое слово для поиска
    :return: Нет возвращаемого значения
    """

    os.chdir(path)  # перейти к работе с каталогом "path"
    if not os.path.isdir("dataset"):  # проверить наличие каталога "dataset"
        os.mkdir("dataset")  # если "dataset" не существует, создайте каталог "dataset"
    os.chdir("dataset")  # перейти к работе с каталогом "dataset"

    page = 0
    count = 0
    data = []
    url = f'{URL}search?p={page}&text={key}'
    rep = requests.get(url, HEADERS)
    soup = BeautifulSoup(rep.text, "lxml")
    images = soup.findAll('img', class_='serp-item__thumb justifier__thumb')  # 30 len(image
    while count < 1000:
        print(page)
        for image in images:
            if count == 1000:
                return None
            image_url = image.get("src")  # получить тег SRC со ссылкой на изображение
            data.append([image_url])
            if (image_url != ""):
                get_image(image_url, key, count)
                count += 1
            page += 1
        print("Nice save images")


if __name__ == "__main__":
    directory = os.getcwd()
    # download_img(directory, 'dog')
    download_img(directory, 'cat')
