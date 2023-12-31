import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from '../login/login.service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent {

  // Signup form
  signupForm = this.formBuilder.group({
    user_type: ["customer", Validators.required],
    username: ["", Validators.required],
    email: ["", [Validators.required, Validators.email]],
    password: ["", Validators.required],
    first_name: ["", Validators.required],
    last_name: ["", Validators.required],
    address: ["", Validators.required],
    phone: ["", Validators.required],
    confirmPassword: ["", Validators.required]
  });

  // Flags and messages for displaying success and error messages to the user
  showSuccess = true;
  showError = false;
  successMsg = '';
  errorMsg = '';

  constructor(private formBuilder: FormBuilder, private router: Router, private loginService: LoginService) {}

  // Signup method to call API when user submits signup form
  onSignUp() {
    const password = this.signupForm.get('password')?.value;
    const confirmPassword = this.signupForm.get('confirmPassword')?.value;

    if (this.signupForm.valid && password === confirmPassword) {
      this.loginService.signup(this.signupForm.value).subscribe((data: any) => {
        if (data.res === 'True') {
          this.successMsg = data.msg;
          this.showSuccess = true;
          this.errorMsg = '';
          this.showError = false;
        } else {
          this.successMsg = '';
          this.showSuccess = false;
          this.errorMsg = data.msg;
          this.showError = true;
        }
      });
    }

  }
  
}
