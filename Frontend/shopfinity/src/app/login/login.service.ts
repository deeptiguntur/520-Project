import { Injectable } from '@angular/core';
import { HttpClient } from  '@angular/common/http';
import { AppService } from '../app.service';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private httpClient: HttpClient, private appService: AppService) { }

  login(loginData: any) {
    return this.httpClient.post(this.appService.DEV + '/login', loginData);
  }

  signup(signupData: any) {
    return this.httpClient.post(this.appService.DEV + '/signup', signupData);
  }


}
