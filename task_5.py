# Задача 5. Валидатор Пользовательских Данных
# Создайте класс User, который содержит атрибуты name, email, и age.
# Необходимо убедиться, что:
# ● Имя состоит из хотя бы двух слов, каждое из которых начинается с заглавной буквы.
# ● Электронная почта содержит символ @ и точку . после @.
# ● Возраст — это положительное целое число, не меньше 0 и не больше 120.
# Создайте пользовательские исключения для каждой из этих проверок:
# ● NameError: Если имя не соответствует формату.
# ● EmailError: Если электронная почта не соответствует формату.
# ● AgeError: Если возраст вне допустимого диапазона.
from error_task_5 import NameException, EmailException, AgeException

class User:
    MIN_WORD_NAME = 2
    def __init__(self,name: str, email,age):

        if len(name.split()) < self.MIN_WORD_NAME:
            raise NameException(name)
        if not self.iscapitalized(name):
            raise NameException(name)
        self.name = name
        if '@.' not in email:
            raise EmailException(self.name,email)
        self.email = email
        if not isinstance(age, int) or age <= 0 or age >= 120:
            raise AgeException(self.name, age)
        self.age = age

    def iscapitalized(self, name: str):
        for i in name.split(' '):
            if not i.istitle():
                return False
        return True

    def __str__(self):
        return f"Пользователь: {self.name}\n" \
               f"Электронная почта: {self.email}\n" \
               f"Возраст: {self.age}"

if __name__ == '__main__':
    # user = User("Василий Полушин", 'kiska@.mail', 99)
    # print(user)
    user = User("Dасилий Hолушин", 'kiska@.mail', '34')
    print(user)