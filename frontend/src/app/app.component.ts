import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root', // Cambiado a algo único
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'], // Corregido a "styleUrls"
})
export class AppComponent {
  title = 'frontend';
}
