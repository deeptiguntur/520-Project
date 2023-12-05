import { HttpClient, HttpEvent, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppService } from '../app.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SellerService {

  constructor(private httpClient: HttpClient, private appService: AppService) { }

  addProduct(productData: any) {
    return this.httpClient.post(this.appService.DEV + '/seller/add-product', productData);
  }
  
}
