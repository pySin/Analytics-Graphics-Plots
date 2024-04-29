import mysql.connector


class SQLConnection:

    def __init__(self, host: str, user: str, password: str):
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        return conn
