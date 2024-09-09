class UserException(Exception):
    def __init__(self, name):
        self.name = name


class KillError(UserException):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} вы там походу кого-то тюкнули"


class DrunkError(UserException):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} опять в стельку и лыко не вяжет!!!"


class CarCrashError(UserException):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} a машина-то не вечная! Можно и поаккуратнее"


class GluttonyError(UserException):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} ну дружок да вы обжора!!!"


class DepressionError(UserException):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} это называется лень, а не депрессия"
