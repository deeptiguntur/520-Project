import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})
export class AddProductComponent {

  addProductForm = this.formBuilder.group({
    productName: ["", Validators.required],
    productDesc: ["", Validators.required],
    category: ["", Validators.required],
    price: ["", Validators.required],
    quantity: ["", Validators.required],
    sale: [false],
    discount: [""],
  });

  constructor(private formBuilder: FormBuilder) {}

  addProduct() {
    console.log(this.addProductForm);
  }

}
