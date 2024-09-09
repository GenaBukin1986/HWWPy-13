# Задание 1. Карма
# Один буддист-программист решил создать свой симулятор жизни, в котором
# нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
# Каждый день вызывается специальная функция one_day(), которая возвращает
# количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из
# исключений:
# ● KillError,
# ● DrunkError,
# ● CarCrashError,
# ● GluttonyError,
# ● DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от
# Exception.)
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из
# которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.
# По итогу у вас может быть примерно такая структура программы:
# открываем файл
# цикл по набору кармы
# try
# карма += one_day()
# except(ы) с указанием классов исключений, которые нужно поймать
# добавляем запись в файл
# закрываем файл
from random import randint
from errors_1 import KillError, DrunkError, DepressionError, CarCrashError, GluttonyError
import os


class LiveOfProgrammer:
    SCORE = 500

    def __init__(self, name):
        self.name = name
        self.live_score = 0

    def __str__(self):
        return f"Программист {self.name} и его количество кармы {self.live_score}"

    def check_karma(self):
        return self.live_score >= self.SCORE


def programm(file: str):
    print("Симулятор жизни программиста")
    name = input("Введите ваше имя или имя знакомого вам программиста: ")
    programmer = LiveOfProgrammer(name)
    if os.path.isfile(file):
        with open(file, 'w', encoding='utf-8') as f:
            day = 0
            while True:

                try:
                    day += 1
                    number_karma = one_day(name)
                except KillError as e:
                    print(f"Сработало исключение {e}")
                    f.write(str(e) + "\n")
                except DrunkError as e:
                    print(f"Сработало исключение {e}")
                    f.write(str(e) + "\n")
                except DepressionError as e:
                    print(f"Сработало исключение {e}")
                    f.write(str(e) + "\n")
                except CarCrashError as e:
                    print(f"Сработало исключение {e}")
                    f.write(str(e) + "\n")
                except GluttonyError as e:
                    print(f"Сработало исключение {e}")
                    f.write(str(e) + "\n")
                    # f.write()
                else:
                    programmer.live_score += number_karma
                    print(f"{programmer}", f"Идет {day} день.")
                    if programmer.check_karma():
                        print(f"{programmer.name} достиг просветления.\n"
                              f"Его уровень кармы: {programmer.live_score}")
                        print("Программа завершает свою работу")
                        break

    else:
        open(file, 'w', encoding='utf-8')


def one_day(name):
    day_karma = randint(1, 7)
    if num := randint(1, 10) == 5:
        exception = [KillError(name), DrunkError(name), DepressionError(name), CarCrashError(name), GluttonyError(name)][randint(0, 4)]
        raise exception
    return day_karma


if __name__ == "__main__":
    programm("karma.log")
