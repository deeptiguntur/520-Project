import { Injectable } from '@angular/core';
import { HttpClient } from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  DEV = "http://127.0.0.1:5000/";

  constructor(private httpClient: HttpClient) { }

}
