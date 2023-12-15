import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { SellerService } from '../seller.service';
import { Product } from 'src/app/product-list/product.model';

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
  showImg = false;
  editProduct: any;

  constructor(private formBuilder: FormBuilder, private sellerService: SellerService) {}

  ngOnInit() {
    this.editProduct = JSON.parse(String(sessionStorage.getItem('editProduct')));
    if (this.editProduct?._id) {
      this.showImg = true;
      this.addProductForm.get('productName')?.setValue(this.editProduct.productName);
      this.addProductForm.get('brand')?.setValue(this.editProduct.brand);
      this.addProductForm.get('productDesc')?.setValue(this.editProduct.productDesc);
      this.addProductForm.get('category')?.setValue(this.editProduct.category);
      this.addProductForm.get('price')?.setValue(this.editProduct.price);
      this.addProductForm.get('quantity')?.setValue(this.editProduct.quantity);
      this.addProductForm.get('price')?.setValue(this.editProduct.price);
      this.addProductForm.get('sale')?.setValue(this.editProduct.sale);
      this.addProductForm.get('discount')?.setValue(this.editProduct.discount);
      // sessionStorage.removeItem('editProduct');
    }
  }

  addProduct() {
    if (this.editProduct?._id) {
      let productData: any = this.addProductForm.value;
      productData = {
        ...productData,
        'imgData': this.imgData.length ? this.imgData : this.editProduct.imgData,
        'product_id': this.editProduct._id
      };
      this.sellerService.editProduct(productData).subscribe((data: any) => {
        if (data.res === 'True') {
          this.showSuccess = true;
        } else {
          this.showError = false;
        }
      });
    } else {
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
  }

  selectFiles(event: any) {
    this.filesEvent = event;
  }
  
  setImages(event: any) {
    this.showImg = false;
    this.imgData = Array.from(event);
  }

}
