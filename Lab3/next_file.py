import csv
from annotation import Annotation


def next_element(obj: Annotation, label: str) -> str:
    """Returns the next instance of annotation by label without repetition"""
    with open(obj.filename_dir, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        for row in file_reader:
            if count < obj.viewed_files:
                count += 1
            elif obj.viewed_files < obj.rows:
                obj.viewed_files += 1
                if row[2] == label:
                    return row[0]
                else:
                    count += 1
    return None