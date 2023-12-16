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
    // Retrieve products from the server using the AppService and subscribe to the response
    this.appService.getProducts().subscribe((data: Product[]) => {
      this.productData = data;
    });
  }

  // Method to navigate to the product editing page with the selected product
  editProduct(product: Product) {
    sessionStorage.setItem('editProduct', JSON.stringify(product));
    this.router.navigate(['/add-product']);
  }

  // Method to navigate to the add-product page
  goToAddProduct() {
    sessionStorage.removeItem('editProduct');
    this.router.navigate(['/add-product']);
  }
}
