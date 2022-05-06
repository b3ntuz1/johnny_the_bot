'''
Тут реалізований весь необхідний код для роботи з юзером.
Через обмеження телеграма всі небхідні дані зберігаються
в БД (add_user і get_user).
'''
from models import Person


def mute(chat, user_id, until_date):
    ''' Мютить юзера
    chat_id: ідентифікатор чату
    user_id: юнікальний ідентифікатор користувача
    until_date: до цієї дати (юнікстайм) юзер буде мовчати
    '''
    chat.restrict(user_id, until_date=until_date)


def unmute():
    pass


def ban():
    pass


def unban():
    pass


def add_user(data):
    user = Person(
                user_id = data.id,
                first_name = data.first_name if data.first_name else '',
                last_name = data.last_name if data.last_name else '',
                username = data.username if data.username else ''
                )
    user.save()


def get_user(data):
    try:
        user = Person.select().where(Person.user_id == data.id).get()
        return user.user_id
    except:
        add_user(data)
    return data.id


def is_admin(chat, user_id):
    for admin in chat.get_administrators():
        if admin.user.id == user_id:
            return True
    return False

