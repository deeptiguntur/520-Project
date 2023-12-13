import { Injectable } from '@angular/core';
import { HttpClient } from  '@angular/common/http';
import { Observable } from 'rxjs';
import { Product } from './product-list/product.model';
// import { AppService } from '../app.service';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  DEV = "http://127.0.0.1:5000";
  loginId = '';
  user_type = '';
  selectedProduct: Product | undefined;

  constructor(private httpClient: HttpClient) { }

  getProducts():Observable<Product[]> {
    return this.httpClient.get<Product[]>(this.DEV + '/product/all-products');
  }

}



