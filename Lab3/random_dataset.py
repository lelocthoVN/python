import os
import random
import shutil
import logging
from annotation import Annotation


def dataset_random(path: str, path_random: str, ann: Annotation) -> None:
    """
    Копирование набора данных в другую директорию (dataset/номер.jpg) и создание аннотации
    :param path: путь, куда вы скопировали данные
    :param path_random: путь, куда вы хотите скопировать
    :param ann: Имя класса аннотации
    :return: нет возвращаемого значения
    """
    if not os.path.exists(path_random):
        try:
            os.mkdir(path_random)
        except OSError:
            logging.warning(f"Create director {path_random} failed")
            return;

    files = os.listdir(path)
    for file in files:
        sub_images = os.listdir(os.path.join(path, file))
        for sub_image in sub_images:
            try:
                shutil.copy(os.path.join(path, file, sub_image), path_random)
                img_random = f"{random.randint(0, 10000)}.jpg"
            except:
                logging.warning("Error occurred while copying file.")
            while os.path.exists(os.path.join(path_random, img_random)):
                img_random = f"{random.randint(0, 10000)}.jpg"
            os.rename(os.path.join(path_random, sub_image), os.path.join(path_random, img_random))
            ann.add_line(path_random, img_random, file)

    print("The data with random number has been copied successfully")
    print(f"File {ann.filename_dir} is created")


if __name__ == "__main__":
    path_data = 'C:/Users/ASUS ZENBOOK/PycharmProjects/pythonProject/dataset'
    path_random = 'C:/Users/ASUS ZENBOOK/PycharmProjects/lab3/data_random'
    ann = Annotation("dataCSV_random.csv")
    dataset_random(path_data, path_random, ann)