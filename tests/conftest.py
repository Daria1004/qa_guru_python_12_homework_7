import zipfile
import os
import pytest
import shutil

CURRENT_FILE = os.path.abspath(__file__)
PROJECT_DIR = os.path.dirname(os.path.dirname(CURRENT_FILE))
TEMP_DIR = os.path.join(PROJECT_DIR, 'temp')
RESOURCE_DIR = os.path.join(PROJECT_DIR, 'resource')
print(CURRENT_FILE)
print(os.path.basename(CURRENT_FILE))

@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists('RESOURCE_DIR'):  # проверяем существует ли папка
        os.mkdir('RESOURCE_DIR')  # создаем папку если её нет

    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, 'files.zip'),'w') as zf:  # создаем архив
        for file in os.listdir(TEMP_DIR):  # добавляем файлы в архив
            add_file = os.path.join(TEMP_DIR, file)  # склеиваем путь к файлам которые добавляют в архив
            zf.write(add_file, os.path.basename(add_file))  # добавляем файл в архив
    yield
    shutil.rmtree(RESOURCE_DIR)  # удаляем файлы после архивации
