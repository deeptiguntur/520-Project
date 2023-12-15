import { Component } from '@angular/core';
import { LoginService } from './login.service';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  loginForm = this.formBuilder.group({
    username: ["", Validators.required],
    password: ["", Validators.required]
  });

  showError = false;

  constructor(private loginService: LoginService, private appService: AppService, private formBuilder: FormBuilder, private router: Router) {}
// checking if the username nad password does have some value in the form 
  onSignIn() {
    console.log(this.loginForm.get('username')?.value);
    console.log(this.loginForm.get('password')?.value);
    const loginData = {
      username: this.loginForm.get('username')?.value,
      password: this.loginForm.get('password')?.value
    }
    //based on the profile login it will be routed to that particular page
    this.loginService.login(loginData).subscribe((data:any) => {
      if (data.res === "True") {
        this.showError = false;
        if (data.user_type === 'customer') {
          this.router.navigate(['/user/product-list']);
        } else {
          this.router.navigate(['/seller/dashboard']);
        }
      } else {
        this.showError = true;
      }
    });
  }

}
