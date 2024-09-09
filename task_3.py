# Задача 3. Счастливое число
# Напишите программу, которая запрашивает у пользователя число до тех пор,
# пока сумма этих чисел не станет больше либо равна 777. Каждое введенное число при этом
# дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с
# вероятностью 1 к 13 выбрасывала пользователю случайное исключение и
# завершалась.
from random import randint
import os


class LuckyNumber:
    LUCKY_NUM = 777

    def __init__(self, file: str = "lucky_number.txt"):
        self.file = file
        self.number = 0

    def choice_exceprion(self):
        num = randint(1, 13)
        if num == 3:
            raise Exception('Выпало исключение')

    def write_file(self, data):
        with open(self.file, 'a', encoding='utf-8') as f:
            f.write(f'{data}\n')

    def is_end(self):
        if self.LUCKY_NUM <= self.number:
            return True
        return False

    def del_file(self):
        if os.path.isfile(self.file):
            os.remove(self.file)

    def create_file(self):
        if not os.path.isfile(self.file):
            open(self.file, 'w', encoding='utf-8')

    def lucky_game(self):
        self.del_file()


        while True:

            num = input("Введите целое число: ")
            try:
                self.choice_exceprion()
            except Exception as e:
                return "Вас постигла неудача!"
            try:
                    num = int(num)
            except ValueError as e:
                print("Нужно ввести целое число.\n"
                      f"Ваш ввод привел к ошибке {e}")
            else:
                self.number += num
                try:
                    self.write_file(num)
                except FileNotFoundError as e:
                    self.create_file()
                if self.is_end():
                    return 'Вы успешно выполнили условие для выхода из порочного цикла!'


if __name__ == "__main__":
    print(LuckyNumber().lucky_game())
