from annotation import Annotation
import next_file as next


class AnnIterator:
    def __init__(self, ann: Annotation):
        self.ann = ann

    def __iter__(self):
        return self

    def __next__(self, direct: str) -> str:
        """
        Возвращает следующий экземпляр аннотации по метке без повторения
        :param direct: имя текущего пути к каталогу
        :return: нет возвращаемого значения
        """
        return next.next_element(self.ann, direct)


if __name__ == "__main__":
    path = 'C:/Users/ASUS ZENBOOK/PycharmProjects/pythonProject/dataset'
    ann = Annotation('dataCSV.csv')
    iter = AnnIterator(ann)
    print(iter.__next__("cat\\0145.jpg"))
    print(iter.__next__("dog\\0999.jpg"))