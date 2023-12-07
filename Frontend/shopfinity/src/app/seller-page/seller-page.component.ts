import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-seller-page',
  templateUrl: './seller-page.component.html',
  styleUrls: ['./seller-page.component.scss']
})
export class SellerPageComponent {

  constructor(private router: Router, private appService: AppService) {}

  ngOnInit() {
    this.appService.getProducts().subscribe((data:any) => {
      console.log("data:",data.length)
  });
}

  goToAddProduct() {
    this.router.navigate(['/add-product']);
  }
}
