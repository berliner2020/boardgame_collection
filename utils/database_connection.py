import mysql.connector


class DatabaseConnection:
    def __init__(self, host, port, user, password, database):
        self.connection = None
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
