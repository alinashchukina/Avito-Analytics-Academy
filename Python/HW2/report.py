import csv
from math import inf


def csv_read(file: str) -> list:
    """
    Функция принимает на вход название csv-файла, считывает его
    и превращает его в список словарей, каждый из которых
    представляет данные по одному сотруднику. Функция нужна для
    дальнейшего удобства работы с данными.
    """
    with open(file, newline='') as csvfile:
        raw_data = csv.reader(csvfile, delimiter=';')
        data = []
        for row in raw_data:
            data.append(', '.join(row))
        employees = []
        dict_keys = data[0].split(', ')
        for row in data[1:]:
            employees.append({dict_keys[i]: row.split(', ')[i]
                              for i in range(len(dict_keys))})
    return employees


def report(data: list) -> None:
    """
    Функция считывает выбор пользователя и выполняет одну из трёх фукнций:
    вывести все отделы, вывести сводный отчёт по отделам и
    сохранить сводный отчёт в csv-файл
    """
    print('Здравствуйте! Выберете, пожалуйста, одну из следующих опций:\n'
          '(1) Вывести все отделы \n'
          '(2) Вывести сводный отчёт по отделам \n'
          '(3) Сохранить сводный отчёт в csv-файл'
          )
    option = ''
    options = {'1': departments_info, '2': show_report, '3': save_report}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()
    return options[option](data)


def departments_info(data: list, show: bool = True) -> set:
    """
    Функция печатает все уникальные отделы. Также функция
    возвращает уникальный набор отделов, необходимый
    для работы других функций.
    """
    departments = set()

    for person in data:
        if person['Отдел'].find('->') != -1:
            departments.add(person['Отдел'].split(' -> ')[1])
        else:
            departments.add(person['Отдел'])

    if show:
        print(*departments, sep=', ')
    return departments


def show_report(data: list, show: bool = True) -> list:
    """
     Функция печатает сводный отчёт по отделам:
     название, численность,
     минимальная и максимальная зарплата,
     средняя зарплата. Также, функция возвращает
     список с характеристиками каждого отдела
     для использования его в функции сохранения
     в csv-файл.
    """
    departments = departments_info(data, show=False)

    numbers = {k: 0 for k in departments}
    minimum = {k: inf for k in departments}
    maximum = {k: 0 for k in departments}
    summ = {k: 0 for k in departments}

    for person in data:
        if person['Отдел'].find('->') != -1:
            depart = person['Отдел'].split(' -> ')[1]
        else:
            depart = person['Отдел']
        numbers[depart] += 1
        if int(person['Оклад']) < minimum[depart]:
            minimum[depart] = int(person['Оклад'])
        if int(person['Оклад']) > maximum[depart]:
            maximum[depart] = int(person['Оклад'])
        summ[depart] += int(person['Оклад'])

    average = {k: round(summ[k] / numbers[k], 2) for k in departments}
    final = [[k, numbers[k], minimum[k], maximum[k], average[k]]
             for k in departments]

    if show:
        s = "{:^20} | " * 4 + "{:^20}"
        print(s.format('Название', 'Количество',
                       'Минимум', 'Максимум', 'Среднее'))
        print('_' * 108)
        for i in final:
            print(s.format(*i))
    return final


def save_report(data: list) -> None:
    """
    Функция сохраняет сводный отчёт в виде csv-файла
    """
    final = show_report(data, show=False)

    with open('report.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Название', 'Количество',
                         'Минимум', 'Максимум', 'Среднее'])
        for i in final:
            writer.writerow(i)


if __name__ == '__main__':
    my_file = 'employees_sample.csv'
    my_data = csv_read(my_file)
    report(my_data)
