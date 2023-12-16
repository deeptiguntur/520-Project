import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-product-view',
  templateUrl: './product-view.component.html',
  styleUrls: ['./product-view.component.scss']
})
export class ProductViewComponent {

  product: any;
  selectedImg: any;
  showAddToCart: boolean = true;
  cartQuantity = 0;

  constructor(private route: ActivatedRoute, private appService: AppService) { }

  ngOnInit(): void {
    this.product = JSON.parse(String(sessionStorage.getItem('selectedProduct')));
    this.selectedImg = this.product.imgData[0];
  }

  // Method to handle the click event when an image is selected to change the larger image
  imgClicked(img: any) {
    this.selectedImg = img;
  }

  // Method to update the cart quantity based on whether to increase or decrease
  updateQuantity(increase: boolean) {
    if (increase) {
      this.cartQuantity = this.cartQuantity+1;
      this.showAddToCart = false;
    } else {
      if (this.cartQuantity-1 === 0) {
        this.showAddToCart = true;
        this.cartQuantity = 0;
      } else {
        this.cartQuantity = this.cartQuantity-1;
      }
    }
  }
}


