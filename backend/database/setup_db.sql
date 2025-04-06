CREATE DATABASE IF NOT EXISTS inventario_db;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad INT NOT NULL
);

CREATE TABLE IF NOT EXISTS proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    telefono VARCHAR(15),
    email VARCHAR(255)
);

ALTER TABLE productos
ADD CONSTRAINT chk_precio CHECK (precio > 0),
ADD CONSTRAINT chk_cantidad CHECK (cantidad >= 0);

