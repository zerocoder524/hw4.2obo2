"""

Разработай систему управления учетными записями пользователей для небольшой
компании. Компания разделяет сотрудников на обычных работников и администраторов.
У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
 Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
 доступа и могут добавлять или удалять пользователя из системы.

Требования:

1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и
уровень доступа ('user' для обычных сотрудников).

2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный
атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также
содержать методы add_user и remove_user, которые позволяют добавлять и удалять
пользователей из списка (представь, что это просто список экземпляров User).

3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и
модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например,
get и set методы).

В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с
реализацией задания.
"""

class User:
    def __init__(self, id, name, access_level='user'):
        self._id = id  # Инкапсуляция
        self._name = name
        self._access_level = access_level

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

class Admin(User):
    def __init__(self, id, name, access_level='admin'):
        super().__init__(id, name, access_level)
        self._users = []  # Список пользователей, управляемых администратором

    def add_user(self, user):
        self._users.append(user)

    def remove_user(self, user_id):
        for i, user in enumerate(self._users):
            if user.get_id() == user_id:
                del self._users[i]
                return True
        return False


user1 = User(1, "Иван Иванов")
user2 = User(2, "Мария Петрова")

admin = Admin(100, "Александр Сидоров")

admin.add_user(user1)
admin.add_user(user2)

print("Список пользователей:")
for user in admin._users:
    print(f"ID: {user.get_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

print("\nУдаление пользователя с ID 1:")
if admin.remove_user(1):
    print("Пользователь удален.")
else:
    print("Пользователь не найден.")

print("\nСписок пользователей после удаления:")
for user in admin._users:
    print(f"ID: {user.get_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
