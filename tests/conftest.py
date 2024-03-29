import zipfile
import os
import pytest
import shutil

CURRENT_FILE = os.path.abspath(__file__)  # абсолютный путь к текущему файлу
PROJECT_DIR = os.path.dirname(os.path.dirname(CURRENT_FILE))  # путь к директории где находится файл с которым работаем
TEMP_DIR = os.path.join(PROJECT_DIR, 'temp')  # делаем склейку пути к текущей директории и папке tmp
RESOURCE_DIR = os.path.join(PROJECT_DIR, 'resource')  # делаем склейку пути к директории RESOURCE и папке 'resource'

@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(RESOURCE_DIR):  # проверяем существует ли папка
        os.mkdir(RESOURCE_DIR)  # создаем папку если её нет
    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, 'files.zip'),'w') as zf:  # создаем архив
        for file in os.listdir(TEMP_DIR):  # добавляем файлы в архив
            add_file = os.path.join(TEMP_DIR, file)  # склеиваем путь к файлам которые добавляют в архив
            zf.write(add_file, os.path.basename(add_file))  # добавляем файл в архив
    yield
    shutil.rmtree(RESOURCE_DIR)  # удаляем файлы после архивации
