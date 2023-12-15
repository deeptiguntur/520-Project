import { Component } from '@angular/core';
import { AppService } from '../app.service';

@Component({
  selector: 'app-order-details',
  templateUrl: './order-details.component.html',
  styleUrls: ['./order-details.component.scss']
})
export class OrderDetailsComponent {
  orderList:any=[]
  totalPrice = 0;
  totalSavings = 0;

  constructor(private appService: AppService) {}
  ngOnInit(){
    this.appService.getOrders().subscribe((data:any) => {
      console.log("data:",data.length)
      this.orderList = data;
      for (let i=0; i<data.length; i++) {
        this.totalPrice = parseFloat((this.totalPrice + data[i].price*data[i].quantity).toFixed(2));
        if (data[i].sale) {
          this.totalSavings = parseFloat((this.totalSavings + data[i].discount*data[i].quantity).toFixed(2));
        }
      }
  });
  }
  getDiscounted(val1: number, val2: number): number {
    return val1 - val2;
  }
  // selectedQuantity = 0;

  updateQuantity(increase: boolean, selectedQuantity: number ) :number{
    if (increase) {
      selectedQuantity = selectedQuantity+1;
    } else {
      if (selectedQuantity-1 === 0) {
        selectedQuantity = 0;
      } else {
        selectedQuantity = selectedQuantity-1;
      }
    }
    return selectedQuantity
  }

}
