from annotation import Annotation
import os, shutil, logging


def copy_dataset(path: str, path_copy: str,  ann: Annotation) -> None:
    """
    Скопировать данные из существующего каталога в другой каталог
    :param path: путь, куда вы скопировали данные
    :param path_copy: путь, куда вы хотите скопировать
    :param ann: Имя класса аннотации
    :return: нет возвращаемого значения
    """
    if not os.path.exists(path_copy):
        try:
            os.mkdir(path_copy)
        except OSError:
            logging.warning(f"Create director {path_copy} failed")

    files = os.listdir(path)
    for file in files:
        images = os.listdir(os.path.join(path, file))
        for image in images:
            shutil.copy(os.path.join(path, file, image), path_copy)
            os.rename(os.path.join(path_copy, image), os.path.join(path_copy, f"{file}_{image}"))
            ann.add_line(path_copy, f"{file}_{image}", file)

    print('The data has been copied successfully')
    print(f"File {ann.filename_dir} is created")


if __name__ == "__main__":
    path_copy = 'C:/Users/ASUS ZENBOOK/PycharmProjects/lab2_pp/dataset_copy'
    path = 'C:/Users/ASUS ZENBOOK/PycharmProjects/pythonProject/dataset'
    ann = Annotation('dataCSV_copy.csv')
    copy_dataset(path, path_copy, ann)


