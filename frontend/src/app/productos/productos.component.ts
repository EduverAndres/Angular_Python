import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from '../services/api.service';

@Component({
  standalone: true,
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css'],
  imports: [CommonModule, FormsModule, HttpClientModule], // Registrar HttpClientModule aquí
})
export class ProductosComponent implements OnInit {
  productos: any[] = [];
  producto = { nombre: '', precio: 0, cantidad: 0 };

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.cargarProductos();
  }

  cargarProductos(): void {
    this.apiService.getProductos().subscribe((data: any) => {
      this.productos = data;
    });
  }

  agregarProducto(): void {
    if (this.producto.nombre.trim() !== '' && this.producto.precio > 0 && this.producto.cantidad > 0) {
      console.log('Datos válidos, enviando al backend:', this.producto); // Depuración
      this.apiService.addProducto(this.producto).subscribe(
        () => {
          console.log('Producto agregado exitosamente.');
          this.cargarProductos(); // Refresca la lista de productos
          this.producto = { nombre: '', precio: 0, cantidad: 0 }; // Limpia el formulario
        },
        (error) => {
          console.error('Error al agregar el producto:', error); // Manejo de errores
          alert('Hubo un problema al agregar el producto. Por favor, inténtelo nuevamente.');
        }
      );
    } else {
      console.error('Datos inválidos:', this.producto); // Mensaje de error si los datos no son válidos
      alert('Por favor, complete todos los campos con valores válidos.');
    }
  }


  eliminarProducto(id: number): void {
    this.apiService.deleteProducto(id).subscribe(() => {
      console.log(`Producto con ID ${id} eliminado.`);
      this.cargarProductos(); // Recargar la lista de productos después de eliminar
    }, error => {
      console.error(`Error al eliminar el producto con ID ${id}:`, error);
    });
  }

}
