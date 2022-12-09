from copy_dataset import copy_dataset
from random_dataset import dataset_random
from annotation import Annotation
from iterator import AnnotationIterator
import sys
import os
from PyQt6.QtWidgets import (QPushButton, QInputDialog, QApplication, QMainWindow, QFileDialog, QLabel)
from PyQt6.QtCore import QSize
from PyQt6 import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Work with dataset")
        self.setStyleSheet("background-color : #99FFFF")
        self.setMinimumSize(800, 400)
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Выберите папку исходного датасета')

        anno = Annotation("dataCSV_tmp.csv")
        iter_ann = AnnotationIterator(anno)
        if not os.path.exists("dataCSV_tmp.csv"):
            anno.create_csv(self.folder_path)

        src = QLabel(f'Исходный датасет:\n{self.folder_path}', self)
        src.setStyleSheet("color : #800000")
        src.setFixedSize(QSize(300, 50))
        src.move(5, 0)

        button_open_file = self.add_button("Выбрать новый путь", 250, 50, 5, 300)
        button_open_file.clicked.connect(self.chose_file)
        button_open_file.setStyleSheet("background-color : #FF9900")

        button_create_annotation = self.add_button("Сформировать аннотацию", 250, 50, 5, 50)
        button_create_annotation.clicked.connect(self.create_annotation)
        button_create_annotation.setStyleSheet("background-color : #FF9900")

        button_copy_dataset = self.add_button("Скопировать датасет", 250, 50, 5, 100)
        button_copy_dataset.clicked.connect(self.dataset_copy)
        button_copy_dataset.setStyleSheet("background-color : #FF9900")

        button_copy_random_dataset = self.add_button("Рандом датасета", 250, 50, 5, 150)
        button_copy_random_dataset.clicked.connect(self.dataset_random)
        button_copy_random_dataset.setStyleSheet("background-color : #FF9900")

        next_dog_button = self.add_button("Следующая собака", 250, 50, 5, 200)
        next_dog_button.clicked.connect(lambda iter=iter_ann: self.next_file("dog", iter_ann))
        next_dog_button.setStyleSheet("background-color : #FF99CC")

        next_cat_button = self.add_button("Следующий кот", 250, 50, 5, 250)
        next_cat_button.clicked.connect(lambda iter=iter_ann: self.next_file("cat", iter_ann))
        next_cat_button.setStyleSheet("background-color : #999900")

        self.image = QLabel('Нажмите кнопку "Следующая собака" или "Следующий кот".', self)
        self.image.setStyleSheet("color : #800000")
        self.image.resize(400, 300)
        self.image.move(280, 60)

        self.show()

    def chose_file(self):
        self.path = QFileDialog.getExistingDirectory(self, 'Выберите папку исходного датасета')
        os.chdir(self.path)
        self.folder_path = os.getcwd()
        return self.folder_path

    def add_button(self, name: str, size_x: int, size_y: int, pos_x: int, pos_y: int):
        """
        Добавить кнопку с фиксированным размером и положением
        :param name: название кнопки
        :param size_x: широкий размер кнопки
        :param size_y: длинный размер кнопки
        :param pos_x: горизонтальные координаты кнопки
        :param pos_y: вертикальные координаты кнопки
        :return: нет значения
        """
        button = QPushButton(name, self)
        button.setFixedSize(QSize(size_x, size_y))
        button.move(pos_x, pos_y)
        return button


    def create_annotation(self) -> None:
        """Создать аннотацию набора данных с выбранным именем"""
        text, ok = QInputDialog.getText(self, 'Ввод', 'Введите название файла-аннотации:')
        if ok:
            A = Annotation(f"{str(text)}.csv")
            A.create_csv(self.folder_path)


    def dataset_copy(self) -> None:
        """Copying dataset (dataset/class_0000.jpg) and creating an annotation"""
        path_copy = QFileDialog.getExistingDirectory(self, 'Введите путь к папке, в которую будет скопирован датасет')
        if not path_copy:
            return
        A = Annotation("dataCSV_copy.csv")
        copy_dataset(self.folder_path, path_copy, A)

    def dataset_random(self) -> None:
        """Random dataset  and creating an annotation"""
        path_random = QFileDialog.getExistingDirectory(self, 'Введите путь к папке, в которую будет рандом датасет')
        if not path_random:
            return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

































































































        A = Annotation("dataCSV_random")
        dataset_random(self.folder_path, path_random, A)

    def next_file(self, label: str, iter: AnnotationIterator):
        """
        Показывает следующие фотографии
        :param label: имя файла
        :param iter: класс Итератор
        :return: нет значения
        """
        try:
            imagePath = iter.__next__(label)
            pixmap = QtGui.QPixmap(imagePath)
            self.image.setPixmap(pixmap)
            self.resize(pixmap.size())
            self.adjustSize()
        except StopIteration:
            self.image.setText(f"Изображения {label} закончились.")
        except OSError as err:
            print("error")

    def closeEvent(self, event):
        """Yдалить временный файл"""
        os.remove("dataCSV_tmp.csv")
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
