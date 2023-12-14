import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { SellerService } from '../seller.service';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})
export class AddProductComponent {

  addProductForm = this.formBuilder.group({
    productName: ["", Validators.required],
    brand: ["", Validators.required],
    productDesc: ["", Validators.required],
    category: ["", Validators.required],
    price: ["", Validators.required],
    quantity: ["", Validators.required],
    sale: [false],
    discount: [""]
  });

  filesEvent: any;
  imgData: any = [];
  showSuccess = false;
  showError = false;

  constructor(private formBuilder: FormBuilder, private sellerService: SellerService) {}

  addProduct() {
    let productData: any = this.addProductForm.value;
    productData = {
      ...productData,
      'imgData': this.imgData
    };
    if (this.addProductForm.valid && this.imgData.length) {
      productData.discount = parseFloat(productData.discount);
      productData.price = parseFloat(productData.price);
      productData.quantity = parseInt(productData.quantity);
      this.sellerService.addProduct(productData).subscribe((data: any) => {
        if (data.res === 'True') {
          this.showSuccess = true;
        } else {
          this.showError = false;
        }
      });
    }
  }

  selectFiles(event: any) {
    this.filesEvent = event;
  }
  
  setImages(event: any) {
    this.imgData = Array.from(event);
  }

}
