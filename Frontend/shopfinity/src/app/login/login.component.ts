import { Component } from '@angular/core';
import { LoginService } from './login.service';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

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

  constructor(private loginService: LoginService, private formBuilder: FormBuilder, private router: Router) {}

  onSignIn() {
    console.log(this.loginForm.get('username')?.value);
    console.log(this.loginForm.get('password')?.value);
    const loginData = {
      username: this.loginForm.get('username')?.value,
      password: this.loginForm.get('password')?.value
    }
    this.loginService.login(loginData).subscribe((data:any) => {
      if (data.res === "True") {
        this.router.navigate(['/add-product']);
      }
    });
  }

}
