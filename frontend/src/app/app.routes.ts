import { Routes } from '@angular/router';
import { ProductosComponent } from './productos/productos.component';

export const appRoutes: Routes = [
  { path: 'productos', component: ProductosComponent },
  { path: '', redirectTo: '/productos', pathMatch: 'full' },
];
