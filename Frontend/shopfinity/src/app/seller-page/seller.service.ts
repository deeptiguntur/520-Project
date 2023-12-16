import { HttpClient, HttpEvent, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppService } from '../app.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SellerService {

  // Constructor for dependency injection of HttpClient and AppService
  constructor(private httpClient: HttpClient, private appService: AppService) { }

  // Method to add a new product by making a POST request to the server
  addProduct(productData: any) {
    return this.httpClient.post(this.appService.DEV + '/seller/add-product', productData);
  }

  // Method to edit an existing product by making a POST request to the server
  editProduct(productData: any) {
    return this.httpClient.post(this.appService.DEV + '/editproduct', productData);
  }
  
}
