from annotation import Annotation
import next_file as next


class AnnotationIterator:

    def __init__(self, a: Annotation):
        self.ann = a
        self.counter = 0

    def __next__(self, label) -> str:
        """Returns the next instance of annotation by label without repetition"""
        if self.counter < (self.ann.rows-1):
            copy = next.next_element(self.ann, label)
            self.counter = self.ann.viewed_files
            return copy
        else:
            raise StopIteration


if __name__ == "__main__":
    path = 'C:/Users/ASUS ZENBOOK/PycharmProjects/pythonProject/dataset'
    ann = Annotation('dataCSV.csv')
    ann.create_csv(path)
    iter = AnnotationIterator(ann)
    print(iter.__next__("dog"))
