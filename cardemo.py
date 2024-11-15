from prettytable import PrettyTable
import json
import sys
table = PrettyTable()
table.field_names = ['Номер', 'Марка', 'Модель', 'Цвет', 'Двигатель', 'Статус']
choose = '0'
with open('data.json') as f:
    data = json.load(f)
    if data != []:
        number = 1
        for car in data:
            car[0] = number
            table.add_row(car)
            number += 1
while choose != '6':
    print('1) Добавить машину')
    print('2) Удалить машину')
    print('3) Изменить машину')
    print('4) Найти машину')
    print('5) Вывести таблицу')
    print('6) Выйти из программы и сохранить изменения')
    print('')
    choose = input()
    if choose == '1':
        if len(data) > 0:
            number = data[-1][0] + 1
        else:
            number = 1
        mark = input('Марка: ')
        if mark == '':
            while mark == '' or mark[0] == ' ' or mark[-1] == ' ':
                print('')
                print('Некорректный ввод')
                print('')
                mark = input('Марка: ')
        model = input('Модель: ')
        if model == '':
            while model == '' or model[0] == ' ' or model[-1] == ' ':
                print('')
                print('Некорректный ввод')
                print('')
                model = input('Модель: ')
        color = input('Цвет: ')
        if color == '':
            while color == '' or color[0] == ' ' or color[-1] == ' ':
                print('')
                print('Некорректный ввод')
                print('')
                color = input('Цвет: ')
        print('Двигатель заведён? (введите 1 или 2)')
        print('1. Да')
        print('2. Нет')
        motor = input()
        while motor != 1 and motor != 2 and motor != '1' and motor != '2':
            print('')
            print('Некорректный ввод')
            print('')
            print('Двигатель заведён? (введите 1 или 2)')
            print('1. Да')
            print('2. Нет')
            motor = input()
        print('Машина открыта? (введите 1 или 2)')
        print('1. Да')
        print('2. Нет')
        openn = input()
        while openn != 1 and openn != 2 and openn != '1' and openn != '2':
            print('')
            print('Некорректный ввод')
            print('')
            print('Машина открыта? (введите 1 или 2)')
            print('1. Да')
            print('2. Нет')
            openn = input()
        if int(motor) == 1:
            motor = 'Заведён'
        else:
            motor = 'Не заведён'
        if int(openn) == 1:
            openn = 'Открыта'
        else:
            openn = 'Закрыта'
        table.add_row([number, mark, model, color, motor, openn])
        data.append([number, mark, model, color, motor, openn])
    if choose == '2':
        if len(data) > 0:
            delit = input('Введите номер машины: ')
            while delit not in [str(x[0]) for x in data]:
                print('')
                delit = input('Введите номер машины: ')
            delit = int(delit)
            table.clear_rows()
            data.pop(delit-1)
            k = 1
            for row in data:
                row[0] = k
                k += 1
            table.add_rows(data)
        else:
            print('Таблица уже пустая')
    if choose == '3':
        if len(data) > 0:
            num = input('Номер изменяемой машины: ')
            while num not in [str(x[0]) for x in data]:
                print('')
                num = input('Номер изменяемой машины: ')
            num = int(num)
            mark = input('Марка: ')
            if mark == '':
                while mark == '' or mark[0] == ' ' or mark[-1] == ' ':
                    print('')
                    print('Некорректный ввод')
                    print('')
                    mark = input('Марка: ')
            model = input('Модель: ')
            if model == '':
                while model == '' or model[0] == ' ' or model[-1] == ' ':
                    print('')
                    print('Некорректный ввод')
                    print('')
                    model = input('Модель: ')
            color = input('Цвет: ')
            if color == '':
                while color == '' or color[0] == ' ' or color[-1] == ' ':
                    print('')
                    print('Некорректный ввод')
                    print('')
                    color = input('Цвет: ')
            print('Двигатель заведён? (введите 1 или 2)')
            print('1. Да')
            print('2. Нет')
            motor = input()
            while motor != '1' and motor != '2':
                print('')
                print('Некорректный ввод')
                print('')
                print('Двигатель заведён? (введите 1 или 2)')
                print('1. Да')
                print('2. Нет')
                motor = input()
            print('Машина открыта? (введите 1 или 2)')
            print('1. Да')
            print('2. Нет')
            openn = input()
            while openn != '1' and openn != '2':
                print('')
                print('Некорректный ввод')
                print('')
                print('Машина открыта? (введите 1 или 2)')
                print('1. Да')
                print('2. Нет')
                openn = input()
            if int(motor) == 1:
                motor = 'Заведён'
            else:
                motor = 'Не заведён'
            if int(openn) == 1:
                openn = 'Открыта'
            else:
                openn = 'Закрыта'
            data[num-1] = [num, mark, model, color, motor, openn]
            table.clear_rows()
            for car in data:
                table.add_row(car)
        else:
            print('Таблица пустая')
    if choose == '4':
        if len(data) > 0:
            cars = data[:]
            table.clear_rows()
            print('Чтобы не учитывать марку / модель / цвет, введите пустое значение')
            print('')
            mark = input('Марка: ')
            model = input('Модель: ')
            color = input('Цвет: ')
            print('Двигатель заведён? (введите 1 ,2 или 3)')
            print('1. Да')
            print('2. Нет')
            print('3. Не учитывать')
            motor = input()
            while motor != '1' and motor != '2' and motor != '3':
                print('')
                print('Некорректный ввод')
                print('')
                print('Двигатель заведён? (введите 1, 2 или 3)')
                print('1. Да')
                print('2. Нет')
                print('3. Не учитывать')
                motor = input()
            print('Машина открыта? (введите 1, 2 или 3)')
            print('1. Да')
            print('2. Нет')
            print('3. Не учитывать')
            openn = input()
            while openn != '1' and openn != '2' and openn != '3':
                print('')
                print('Некорректный ввод')
                print('')
                print('Машина открыта? (введите 1, 2 или 3)')
                print('1. Да')
                print('2. Нет')
                print('3. Не учитывать')
                openn = input()
            if int(motor) == 1:
                motor = 'Заведён'
            elif int(motor) == 2:
                motor = 'Не заведён'
            if int(openn) == 1:
                openn = 'Открыта'
            elif int(openn) == 2:
                openn = 'Закрыта'
            if mark != '' and mark[-1] != ' ' and mark[0] != ' ':
                for row in cars[:]:
                    if row[1] != mark:
                        cars.remove(row)
            if model != '' and model[-1] != ' ' and model[0] != ' ':
                for row in cars[:]:
                    if row[2] != model:
                        cars.remove(row)
            if color != '' and color[-1] != ' ' and color[0] != ' ':
                for row in cars[:]:
                    if row[3] != color:
                        cars.remove(row)
            if motor != '3':
                for row in cars[:]:
                    if row[4] != motor:
                        cars.remove(row)
            if openn != '3':
                for row in cars[:]:
                    if row[5] != openn:
                        cars.remove(row)
            table.add_rows(cars)
            print('')
            print(table)
            print('')
            table.clear_rows()
            table.add_rows(data)
        else:
            print('Таблица пустая')
    if choose == '5':
        print('')
        print(table)
        print('')
    if choose == '6':
        with open('data.json', 'w') as f:
            json.dump(data, f)
        sys.exit()
    if choose not in '123456' or choose == '':
        print('Выберите номер команды')

