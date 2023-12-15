import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AppService } from '../app.service';
import { Product } from '../product-list/product.model';

@Component({
  selector: 'app-seller-page',
  templateUrl: './seller-page.component.html',
  styleUrls: ['./seller-page.component.scss']
})
export class SellerPageComponent {

  productData: Product[] = [];


  constructor(private router: Router, private appService: AppService) {}

  ngOnInit() {
    this.appService.getProducts().subscribe((data: Product[]) => {
      this.productData = data;
    });
  }

  editProduct(product: Product) {
    sessionStorage.setItem('editProduct', JSON.stringify(product));
    this.router.navigate(['/add-product']);
  }

  goToAddProduct() {
    this.router.navigate(['/add-product']);
  }
}
