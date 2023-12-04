import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppService } from '../app.service';

@Injectable({
  providedIn: 'root'
})
export class SellerService {

  constructor(private httpClient: HttpClient, private appService: AppService) { }

  addProduct(productData: any) {
    return this.httpClient.post(this.appService.DEV + '/seller/addProduct', productData);
  }
  
}
