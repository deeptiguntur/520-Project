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
  signupForm = this.formBuilder.group({
    user_type: ["customer", Validators.required],
    user_name: ["", Validators.required],
    email: ["", [Validators.required, Validators.email]],
    password: ["", Validators.required],
    first_name: ["", Validators.required],
    last_name: ["", Validators.required],
    address: ["", Validators.required],
    phone: ["", Validators.required],
    confirmPassword: ["", Validators.required]
  });
  constructor(private formBuilder: FormBuilder, private router: Router, private loginService: LoginService) {}
  onSignUp() {
    console.log(this.signupForm.value);
    const password = this.signupForm.get('password')?.value;
    const confirmPassword = this.signupForm.get('confirmPassword')?.value;

    if (this.signupForm.valid && password === confirmPassword) {
      this.loginService.signup(this.signupForm.value).subscribe(data => {
        this.router.navigate(['/login']);
      });
    }

    
    



  }


  
}
