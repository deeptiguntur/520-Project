import { Component } from '@angular/core';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent {

  showDiscount = true;
  selectedQuantity = 0;
  showAddToCart = true;

  updateQuantity(increase: boolean) {
    if (increase) {
      this.selectedQuantity = this.selectedQuantity+1;
      this.showAddToCart = false;
    } else {
      if (this.selectedQuantity-1 === 0) {
        this.showAddToCart = true;
        this.selectedQuantity = 0;
      } else {
        this.selectedQuantity = this.selectedQuantity-1;
      }
    }
  }
 
}
