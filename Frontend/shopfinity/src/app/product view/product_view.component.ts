import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product-view',
  templateUrl: './pro.html',
  styleUrls: ['./product-view.component.scss']
})
export class ProductViewComponent implements OnInit {
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
      name: 'S',
      description: 'S',
      imageUrl: 'sa.jpg',
      productBrand: 'S',
      category: 'Electr',
      price: 99.99,
      quantity: 10,
      sale: true,
      discount: 10,
      shippingDetails: 's',
      productSpecs: 'S'
    };
  }

  addToCart(): void {
   
    console.log('Product added to cart:', this.product);
  }
}
