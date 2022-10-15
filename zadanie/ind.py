#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime


def select(line, humans):
    """Выбор знака зодиака по дате рождения"""
    nom = input('Введите знак зодиака: ')
    count = 0
    print(line)
    print(
        f'| {"№":^4} | {"Ф.И.О.":^20} | {"знак зодиака":^15} | {"Дата рождения":^16} |')
    print(line)
    for i, num in enumerate(humans, 1):
        if nom == num.get('zodiac', ''):
            count += 1
            print(
                '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                    count,
                    num.get('name', ''),
                    num.get('zodiac', ''),
                    num.get('daytime', 0)))
    print(line)
    if count == 0:
        print('Таких людей нет')


def table(line, humans):
    """Вывод скиска людей"""
    print(line)
    print(
        '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
            "№",
            "Ф.И.О.",
            "Знак зодиака",
            "Дата рождения"))
    print(line)
    for i, num in enumerate(humans, 1):
        print(
            '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                i,
                num.get('name', ''),
                num.get('zodiac', ''),
                num.get('daytime', 0)
            )
        )
    print(line)


def add(humans):
    """Добавление новых людей"""
    daytime = input('Введите дату рождения: ')
    zodiac = input('Введите знак зодиака: ')
    name = input('Введите Ф.И.О.: ')
    air = {
        'zodiac': zodiac,
        'name': name,
        'daytime': daytime
    }
    humans.append(air)
    if len(humans) > 1:
        humans.sort(key=lambda x: x.get('name', ''))


def main():
    humans = []
    print('Список комманд: \n exit - Завершить работу'
          ' \n add - Добавить человека \n'
          ' list - Показать список людей'
          ' \n select - Выбрать знак зодиака по дате рождения')
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 15,
        '-' * 16
    )
    while True:
        com = input('Введите команду: ').lower()
        if com == 'exit':
            break
        elif com == "add":
            add(humans)
        elif com == 'list':
            table(line, humans)
        elif com == 'select':
            select(line, humans)
        else:
            print(f"Неизвестная команда {com}", file=sys.stderr)


if __name__ == '__main__':
    main()
