from sqlalchemy.exc import IntegrityError

from server.database.connector import DataAccessLayer
from server.database.models import Client, History


class ClientMessages:
    def __init__(self, conn_string, base, echo):
        """Создать подключение к БД"""

        self.dal = DataAccessLayer(conn_string, base, echo=echo)
        self.dal.connect()
        self.dal.session = self.dal.Session()

    def add_client(self, username, password, info=None):
        """Добавление клиента"""

        if self.get_client_by_username(username):
            return f'Пользователь {username} уже существует'
        else:
            new_user = Client(username=username, password=password,
                              info=info)
            self.dal.session.add(new_user)
            self.dal.session.commit()
            print(f'Добавлен пользователь: {new_user}')

    def get_client_by_username(self, username):
        """Получение клиента по имени"""

        client = self.dal.session.query(Client).filter(
            Client.username == username).first()
        return client

    def add_client_history(self, client_username, ip_addr='8.8.8.8'):
        """добавление истории клиента"""

        client = self.get_client_by_username(client_username)

        if client:
            new_history = History(ip_addr=ip_addr, client_id=client.id)

            try:
                self.dal.session.add(new_history)
                self.dal.session.commit()
                print(f'Добавлена запись в историю: {new_history}')
            except IntegrityError as err:
                print(f'Ошибка интеграции с базой данных: {err}')
                self.dal.session.rollback()

        return f'Пользователь {client_username} не существует'

    def set_user_online(self, client_username):
        client = self.get_client_by_username(client_username)

        if client:
            client.online_status = True
            self.dal.session.commit()

        return f'Пользователь {client_username} не существует'
