import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';


@Injectable({
  providedIn: 'root', // Declarar como proveedor de toda la aplicación
})
export class ApiService {
  private baseUrl = 'http://localhost:5000/api'; // URL de tu backend

  constructor(private http: HttpClient) {}

  getProductos(): Observable<any> {
    return this.http.get(`${this.baseUrl}/productos`);
  }

  addProducto(producto: any): Observable<any> {
    console.log('Enviando producto al backend:', producto); // Depuración
    return this.http.post(`${this.baseUrl}/productos`, producto).pipe(
      catchError((error) => {
        console.error('Error en la petición POST:', error); // Manejo de errores
        return throwError(error); // Devuelve el error para que sea manejado en el componente
      })
    );
  }


  deleteProducto(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/productos/${id}`);
  }

}
