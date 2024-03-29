import os

from pypdf import PdfReader
import zipfile
from openpyxl import load_workbook
from conftest import RESOURCE_DIR
import csv


def test_csv():
    third_row = None
    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, 'files.zip')) as zip_file: # открываем архив
        with zip_file.open('schedule.csv') as csv_file: # открываем файл в архиве
            content = csv_file.read().decode('utf-8-sig')  # читаем содержимое файла и декодируем его если в файле есть символы не из английского алфавита
            csvreader = list(csv.reader(content.splitlines()))  # читаем содержимое файла и преобразуем его в список
            third_row = csvreader[2]  # получаем третью строку

    assert third_row[0] == 'школа'  # проверка значения элемента в первом столбце третьей строки
    assert third_row[5] == 'выходной'  # проверка значения элемента в седьмом столбце третьей строки

def test_pdf():
    text = None
    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, 'files.zip')) as zip_file: # открываем архив
        with zip_file.open('Колобок.pdf') as pdf_file:  # открываем файл в архиве
            reader = PdfReader(pdf_file)
            page = reader.pages[0]  # получаем первую страницу
            text = page.extract_text()  # извлекаем текст из первой страницы

    assert text.find('Автор: Русская народная') != -1

def test_xlsx():
    sheet = None
    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, 'files.zip')) as zip_file:  # открываем архив
        with zip_file.open('pers.xlsx') as xlsx_file:  # открываем файл в архиве
            workbook = load_workbook(xlsx_file)  # открываем файл
            sheet = workbook.active  # получаем активный лист

    assert sheet.cell(row=2, column=8).value == '88002000600'
