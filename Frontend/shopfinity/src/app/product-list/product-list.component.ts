import { Component } from '@angular/core';
import { AppService } from '../app.service';
import { Product } from './product.model';
import { range } from 'rxjs';
import { Router } from '@angular/router';

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

  constructor(private appService: AppService, private router: Router) {}

  ngOnInit() {
    this.appService.getProducts().subscribe((data: Product[]) => {
      this.productData = data;
      for (let i=0; i<data.length; i++) {
        this.addToCartData[i] = {addToCart: true, quantity: 0};
      }
      this.appService.getOrders().subscribe((cartData:any) => {
        let index = 0;
        for (let j=0; j<data.length; j++) {
          index = this.productData.findIndex(p => p._id === cartData[j]?.product_id)
          this.addToCartData[index].quantity = cartData[j].quantity;
          this.addToCartData[index].addToCart = false;
        }
      });
    });
  }

  categoryFilter(category: string) {
    const categoryData = {category: category};
    this.appService.getCategoryProducts(categoryData).subscribe((data: Product[]) => {
      this.productData = data;
    });
  }

  search(keyword: any) {
    const keywordData = {
      keyword: keyword
    }
    this.appService.searchByKeyword(keywordData).subscribe((data: Product[]) => {
      this.productData = data;
    });
  }

  updateQuantity(increase: boolean, index: number, event:any) {
    event.stopPropagation();
    if (increase) {
      this.addToCartData[index].quantity = this.addToCartData[index].quantity+1;
      this.addToCartData[index].addToCart = false;
    } else {
      if (this.addToCartData[index].quantity-1 === 0) {
        this.addToCartData[index].addToCart = true;
        this.addToCartData[index].quantity = 0;
      } else {
        console.log(this.addToCartData[index].quantity)
        this.addToCartData[index].quantity = this.addToCartData[index].quantity-1;
        console.log(this.addToCartData[index].quantity)

      }
    }
    this.addToCart(index);
  }

  addToCart(index: number) {
    const productClicked = this.productData[index]._id;
    const quantity = this.addToCartData[index].quantity;
    const addToCartData = {product_id: productClicked, quantity: quantity};
    this.appService.addToCart(addToCartData).subscribe();
  }



  productClicked(productId: string) {
    this.appService.selectedProduct = this.productData.find(product => product._id === productId);
    sessionStorage.setItem('selectedProduct', JSON.stringify(this.appService.selectedProduct));
    console.log(this.appService.selectedProduct)
    this.router.navigate(['user/product/view'], { queryParams: { id: productId }})
  }
 
}
