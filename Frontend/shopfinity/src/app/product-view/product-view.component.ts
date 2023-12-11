import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product-view',
  templateUrl: './product-view.component.html',
  styleUrls: ['./product-view.component.scss']
})
export class ProductViewComponent {
  product: any; 

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const productId = params['id'];
      this.loadProductDetails(productId);
    });
  }

  loadProductDetails(productId: string): void {
    
    this.product = {
      id: productId,
      name: 'IPhone 15 Pro',
      description: 's',
      imageUrl: '../../assets/Images/Screenshot 2023-12-06 at 1.47.33 PM.png',
      productBrand: 'Apple',
      price: 999.99,
      sale: false,
      discount: 0,
      productSpecs: 'Sample specifications'
    };
  }

  addToCart(): void {
   
    console.log('Product added to cart:', this.product);
  }
}


