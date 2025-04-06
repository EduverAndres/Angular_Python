import { bootstrapApplication } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { provideHttpClient } from '@angular/common/http';
import { ProductosComponent } from './app/productos/productos.component';
import { provideRouter, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', component: ProductosComponent }, // Ruta base.
  { path: 'productos', component: ProductosComponent }, // Ruta explícita para 'productos'.
];

bootstrapApplication(ProductosComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient() // Registrar HttpClientModule como proveedor.
  ],
});
