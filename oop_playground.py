class User:

    def __init__(self):
        print(">>> Вошли в __init__")

        self.first_name = "Неизвестно"

        print(">>> Записали first_name")

        self.age = 0

        print(">>> Записали age")


nik = User()

print(nik.first_name)
print(nik.age)