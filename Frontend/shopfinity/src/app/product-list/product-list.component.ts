import { Component } from '@angular/core';
import { AppService } from '../app.service';
import { Product } from './product.model';
import { range } from 'rxjs';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent {

  selectedQuantity = 0;
  showAddToCart = true;

  productData: Product[] = [];
  addToCartData:any = [];

  constructor(private appService: AppService) {}

  ngOnInit() {
    this.appService.getProducts().subscribe((data: Product[]) => {
      this.productData = data;
      for (let i=0; i<data.length; i++) {
        this.addToCartData[i] = {addToCart: true, quantity: 0};
      }
    });

  }

  updateQuantity(increase: boolean, index: number) {
    if (increase) {
      this.addToCartData[index].quantity = this.addToCartData[index].quantity+1;
      this.addToCartData[index].addToCart = false;
    } else {
      if (this.addToCartData[index].quantity-1 === 0) {
        this.addToCartData[index].addToCart = true;
        this.addToCartData[index].quantity = 0;
      } else {
        this.addToCartData[index].quantity = this.addToCartData[index].quantity-1;
      }
    }
  }
 
}
