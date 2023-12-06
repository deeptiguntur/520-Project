import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-seller-page',
  templateUrl: './seller-page.component.html',
  styleUrls: ['./seller-page.component.scss']
})
export class SellerPageComponent {

  constructor(private router: Router) {}

  goToAddProduct() {
    this.router.navigate(['/add-product']);
  }
}
