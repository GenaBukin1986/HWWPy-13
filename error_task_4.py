class ScoreLimitExceededError(Exception):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'Ну {self.name} голубчик это никуда не годится.\n' \
               'Это попахивает читерством.\n' \
               f'Вы пытались добавить {self.score}'


class ScoreNaturel(Exception):
    def __init__(self,name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Ну {self.name} кто же добавляет отрицательные очки.\n" \
               f"Вы пытаетесь добавить {self.score}"


class ScoreTotal(Exception):
    def __init__(self, name, score, total):
        self.name = name
        self.score = score
        self.total = total

    def __str__(self):
        return f"Нельзя у бродяги {self.name} последние очки забрать.\n" \
               f"Вы пытаетесь забрать {self.score}, а их всего {self.total}"

