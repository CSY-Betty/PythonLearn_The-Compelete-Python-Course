import sqlite3


class DatabaseConnection:
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb: # if exc_type is not none or exc_val is not none or exc_tb is not none
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()