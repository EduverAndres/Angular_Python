import mysql.connector

class DatabaseConnector:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="inventario_db"
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as e:
            print(f"Error conectando a la base de datos: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Operación exitosa.")
        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")

