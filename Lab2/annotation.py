import os, csv

class Annotation:

    def __init__(self, filename: str) -> None:
        self.rows = 0
        self.filename_dir = filename

    def add_line(self, path: str, filename: str, label: str) -> None:
        """
        Добавление строки в аннотацию
        :param path: путь к каталогу, содержащему данные
        :param filename: имя данных
        :param label: метка данных
        :return: нет возвращаемого значения
        """
        with open(self.filename_dir, "a", encoding="utf-8", newline="") as f:

            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            if self.rows == 0:
                writer.writerow(["Absolute Path", "Relative Path", "Label"])

                self.rows += 1
            writer.writerow([os.path.join(path, filename), os.path.relpath(os.path.join(path, filename)), label])
            self.rows += 1


    def create_csv(self, path: str) -> None:
        """
        Создать аннотацию
        :param path: путь к каталогу, содержащему коллекцию данных
        :return: нет возвращаемого значения
        """
        files = []
        i = 0
        for dirs, file, images in os.walk(path):
            if i == 0:
                files = file
            else:
                for image in images:
                    self.add_line(dirs, image, files[i - 1])
            i += 1
        print(f"File {self.filename_dir} is created successfully" )


if __name__ == "__main__":
    path_data = 'C:/Users/ASUS ZENBOOK/PycharmProjects/pythonProject/dataset'
    ann = Annotation("dataCSV.csv")
    ann.create_csv(path_data)



