from database.db_connector import DatabaseConnector
from models.producto import Producto

class ProductoController:
    def __init__(self):
        self.db = DatabaseConnector()
        self.db.connect()

    def agregar_producto(self, nombre, precio, cantidad):
        query = "INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)"
        self.db.cursor.execute(query, (nombre, precio, cantidad))
        self.db.connection.commit()
        print("Producto agregado correctamente.")
    
    def listar_productos(self):
        query = "SELECT * FROM productos"
        self.db.cursor.execute(query)
        resultados = self.db.cursor.fetchall()
        return [Producto(*row) for row in resultados]

    def cerrar(self):
        self.db.close()
        
    def verificar_producto_existente(self, nombre):
        query = "SELECT COUNT(*) FROM productos WHERE nombre = %s"
        self.db.cursor.execute(query, (nombre,))
        resultado = self.db.cursor.fetchone()
        return resultado[0] > 0

    def eliminar_producto(self, id):
        query = "DELETE FROM productos WHERE id = %s"
        self.db.cursor.execute(query, (id,))
        self.db.connection.commit()
        print(f"Producto con ID {id} eliminado correctamente.")
