import { Component } from '@angular/core';
import { AppService } from '../app.service';

@Component({
  selector: 'app-order-details',
  templateUrl: './order-details.component.html',
  styleUrls: ['./order-details.component.scss']
})
export class OrderDetailsComponent {
  orderList=[]

  constructor(private appService: AppService) {}
  ngOnInit(){
    this.appService.getOrders().subscribe((data:any) => {
      console.log("data:",data.length)
      this.orderList = data;
  });
  }
  getDiscounted(val1: number, val2: number): number {
    return val1 - val2;
  }

}
