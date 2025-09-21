class User:
    # переменные класса
    total_users = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1

    @classmethod # можно вызывать только у класса
    def get_total_users(cls):
        return cls.total_users # через cls можно обратиться в наследнике

    @classmethod
    def create_user(cls, name, email):
        if not cls.validate_email(email):
            return 'Email is not valid'
        user = cls(name, email)
        return user

    @staticmethod # статический метод (не использует self или cls), можно вызвать где угодно.
    def validate_email(email):
        return '@' in email

print(User.get_total_users())

user_1 = User('Albert', 'albert@gmail.com')
user_2 = User('Igor', 'igor@gmail.com')
user_3 = User.create_user('Alice', '<EMAIL>')

print(User.total_users)
print(user_1.validate_email(user_1.email))