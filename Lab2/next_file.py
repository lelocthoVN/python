import csv
from annotation import Annotation


def next_element(ann: Annotation, direct: str) -> str:
    """
    Возвращает следующий экземпляр аннотации по метке без повторения
    :param ann: имя класса аннотации
    :param direct: имя текущего пути к каталогу
    :return: нет возвращаемого значения
    """
    with open(ann.filename_dir, 'r', newline='') as file:
        wr = csv.reader(file, delimiter= ',')
        i = 0
        is_instance = False
        for row in wr:
            if i != 0:
                exist = direct in row[0]
                if is_instance:
                    return "Next instance: " + str(row[0])
                if exist:
                    status = True
            i += 1
    return None

