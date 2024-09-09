class NameException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Ну голубчик это никуда не годится.\n' \
               'Имя должно состоять из хотя бы двух слов, каждое из которых начинается с заглавной буквы..\n' \
               f'Ваше имя {self.name}'

class EmailException(Exception):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'Ну {self.name} голубчик это никуда не годится.\n' \
               'Электронная почта содержит символ @ и точку . после @.\n' \
               f'Ваше email {self.email}'

class AgeException(Exception):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Ну {self.name} голубчик это никуда не годится.\n' \
               'Возраст — это положительное целое число, не меньше 0 и не больше 120.\n' \
               f'Вы указали возраст {self.age} и тип {type(self.age)}'