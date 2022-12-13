import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def add_numerical (df: pd.DataFrame) -> None:
    """
    Добавление столбца с числовыми метками
    :param df: исходный кадр данных
    :return: нет значения
    """
    i = 0
    labels_number = []
    while i < len(df):
        labels_number.append(int(df['label'].iloc[i] == 'dog'))
        i += 1
    df["numerical_class"] = labels_number

def add_columns_size(df: pd.DataFrame)-> None:
    """
    Добавьте информацию об изображении (ширину, высоту, каналы) в DataFrame.
    :param df: исходный кадр данных
    :return: нет значения
    """
    width=[]
    height=[]
    channels=[]
    for image_path in df['Absolute_Path']:
        img = cv2.imread(image_path)
        img_height, img_width, img_channels = img.shape
        width.append(img_width)
        height.append(img_height)
        channels.append(img_channels)
    df["width"] = width
    df["height"] = height
    df["channels"] = channels

def filter(df: pd.DataFrame, label: str) -> pd.DataFrame:
    """
    Создайте новый индексированный фрейм данных по метке
    :param df: исходный кадр данных
    :param label: имя изображения
    :return: новый индексированный фрейм
    """
    tmp = df[df.label == label]
    return tmp.reset_index(drop=True, inplace=True)

def filter_options(df: pd.DataFrame, label: str, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Создайте новый индексированный фрейм данных по метке и максимальным размерам
    :param df: исходный кадр данных
    :param label: имя изображения
    :param max_height: максимальное значение высоты
    :param max_width: максимальное значение ширины
    :return: новый индексированный фрейм
    """
    tmp = df[((df.label == label) & (df.width <= max_width) & (df.height <= max_height))]
    return tmp.reset_index(drop=True, inplace=True)

def grouping(df: pd.DataFrame) -> tuple:
    """
    Группировка датафрейма по метке класса и вычисление максимального, минимального и среднего значения по количеству
    пикселей.
    :param df: Датафрейм.
    """
    df["pixels"] = df["width"] * df["height"] * df["channels"]
    return df.groupby("label").max(), df.groupby("label").min(), df.groupby("label").mean()

def histogram_build(df: pd.DataFrame, label: str) -> list:
    """
    Построение гистограммы.
    :param df: Датафрейм.
    :param label: Метка класса.
    """
    image = cv2.imread(np.random.choice(filter(df, label).Absolute_Path.to_numpy()))
    img_height, img_width, img_channels = image.shape
    return [cv2.calcHist([image], [0], None, [256], [0, 256]) / (img_height * img_width),
            cv2.calcHist([image], [1], None, [256], [0, 256]) / (img_height * img_width),
            cv2.calcHist([image], [2], None, [256], [0, 256]) / (img_height * img_width)]

def draw(df: pd.DataFrame, label: str) -> None:
    """
    Отрисовка гистограмм, которые возвращаются из histogram_construction .
    :param df: Датафрейм.
    :param class_label: Метка класса.
    """
    plt.title('Image Histogram')
    plt.xlabel('Intensity color')
    plt.ylabel('Density pixel')
    plt.xlim([0, 256])
    hist = histogram_build(df, label)
    colors = ['b', 'g', 'r']
    for i in range(3):
        plt.plot(hist[i], color=colors[i])
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data.csv", usecols = ['Absolute_Path','label'])
    add_numerical(df)
    add_columns_size(df)
    df.to_csv('resultDF.csv')
    filtered_dataFarm = filter_options(df, 'dog', 350, 350)
    print(filtered_dataFarm)
    draw(df, "dog")