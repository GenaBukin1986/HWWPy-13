# Задача 4. Счетчик Очков в Игрe
# Создайте класс GameScore для отслеживания очков игрока. В этом классе
# должны быть методы для добавления и уменьшения очков. Однако:
# ● Очки не могут быть отрицательными.
# ● Если игрок пытается добавить больше очков, чем 1000, должно быть
# выброшено исключение ScoreLimitExceededError.
# Создайте пользовательское исключение ScoreLimitExceededError.
from error_task_4 import ScoreLimitExceededError, ScoreNaturel, ScoreTotal
from random import choice


class GameScore:
    def __init__(self, name: str):
        self.name = name
        self.scores_user = 0

    def add_score(self, score):
        if not isinstance(score, int):
            raise TypeError("Это не целое число")
        if score < 0:
            raise ScoreNaturel(self.name, score)
        if score >= 1000:
            raise ScoreLimitExceededError(self.name, score)
        self.scores_user += score

    def remove_score(self, score):
        if not isinstance(score, int):
            raise TypeError("Это не целое число")
        if score < 0:
            raise ScoreNaturel(self.name, score)
        # if self.scores_user < score:
        #     raise ScoreTotal(self.name, score, self.scores_user)
        self.scores_user -= score

    def __str__(self):
        return f"Игрок: {self.name}.\n" \
               f"Количество очков: {self.scores_user}"


if __name__ == "__main__":
    player = GameScore("John")
    while True:
        num = input("Введите целое число очков: ")
        try:
            num = int(num)
            ch = choice([1, 2])
            if ch == 1:
                try:
                    player.add_score(num)
                    print(f"Добавляем {num} очков")
                    print(player)
                except ScoreNaturel as e:
                    print(f"Выпала ошибка {e}")
                except TypeError as e:
                    print(f"Выпала ошибка {e}")
                except ScoreLimitExceededError as e:
                    print(f"Выпала ошибка {e}")
            elif ch == 2:
                try:
                    player.remove_score(num)
                    print(f"Вычитаем {num} очков")
                    print(player)
                except TypeError as e:
                    print(f"Выпала ошибка {e}")
                except ScoreNaturel as e:
                    print(f"Выпала ошибка {e}")
                except ScoreTotal as e:
                    print(f"Выпала ошибка {e}")

            if player.scores_user < 0:
                print(f"Игра подошла к концу на счету {player.name} {player.scores_user}")
                break
            if player.scores_user > 2000:
                print(f"{player.name} выиграл! На его счету {player.scores_user} очков")
                break
        except ValueError as e:
            print(f"Выпала ошибка {e}")
