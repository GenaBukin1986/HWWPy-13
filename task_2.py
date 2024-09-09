# Задача 2. Чат
# Реализуйте программу - чат, в котором могут участвовать сразу несколько человек, то
# есть программа может работать одновременно для нескольких пользователей. При
# запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
# 1. Посмотреть текущий текст чата
# 2. Отправить сообщение (затем вводит сообщение)
# Действия запрашиваются бесконечно.

class Chat:
    def __init__(self, file='chat.txt'):
        self.file = file

    def show_messages(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                file_read = f.readlines()
                for line in file_read:
                    print(line[:-1])
        except FileNotFoundError as e:
            print("К сожалению чат пуст")

    def write_message(self, name, message):
        with open(self.file, 'a', encoding='utf-8') as f:
            f.write(f'{name}: {message}\n')

    def main_chat(self):
        print("Добро пожаловать в чат!")
        while True:
            print("""
Меню чата:
1. Посмотреть чат
2. Написать сообщение
3. Выйти из чата\n
""")
            value = input("Введите пункт чата: ")
            match value:
                case '1':
                    self.show_messages()
                case '2':
                    name=input("Введите ваше имя: ")
                    message = input("Введите текст сообщения: ")
                    self.write_message(name, message)
                case '3':
                    input("Выход из чата\n"
                          "Нажмите enter, чтобы выйти...")
                    break

if __name__ == "__main__":
    Chat().main_chat()

