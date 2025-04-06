from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.producto_controller import ProductoController  # Importa tu controlador.

# Inicializar Flask y configuración CORS
app = Flask(__name__)
CORS(app)

# Inicializar el controlador de productos
producto_controller = ProductoController()

# Endpoint para listar productos
@app.route('/api/productos', methods=['GET'])
def get_productos():
    try:
        productos = producto_controller.listar_productos()
        # Convertir objetos Producto a diccionarios JSON
        productos_json = [
            {"id": producto.id_producto, "nombre": producto.nombre, "precio": producto.precio, "cantidad": producto.cantidad}
            for producto in productos
        ]
        return jsonify(productos_json), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para agregar un producto
@app.route('/api/productos', methods=['POST'])
def add_producto():
    try:
        datos = request.json
        if not datos:
            return jsonify({"error": "No se enviaron datos"}), 400

        nombre = datos.get("nombre")
        precio = datos.get("precio")
        cantidad = datos.get("cantidad")

        if not nombre or not precio or not cantidad:
            return jsonify({"error": "Todos los campos son obligatorios"}), 400

        producto_controller.agregar_producto(nombre, precio, cantidad)
        return jsonify({"message": "Producto agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para verificar si un producto ya existe
@app.route('/api/productos/verificar', methods=['POST'])
def verificar_producto():
    try:
        datos = request.json
        nombre = datos.get("nombre")

        if not nombre:
            return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400

        existe = producto_controller.verificar_producto_existente(nombre)
        return jsonify({"existe": existe}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# Endpoint para eliminar un producto
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    try:
        # Invoca el método para eliminar producto del controlador
        producto_controller.eliminar_producto(id)
        return jsonify({"message": "Producto eliminado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
