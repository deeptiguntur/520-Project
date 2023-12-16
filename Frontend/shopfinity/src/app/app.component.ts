import { Component } from '@angular/core';
import { AppService } from './app.service';
import { NavigationEnd, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  notificationArr: any;
  showNotification = false;
  styling: any = [];
  constructor(public router: Router, private appService: AppService) { }

  ngOnInit() {
    // To check current page url
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        if (event.urlAfterRedirects === '/login') {
          this.showNotification = false;
        } else if (event.urlAfterRedirects === '/user/product-list') {
          // Check if user is a customer then see if any products went on sale recently. If yes show notification in the UI.
          if (sessionStorage.getItem('user') === 'customer') {
            this.appService.saleNotification().subscribe((data: any) => {
              if (data.res === 'True') {
                this.notificationArr = data.product;
                this.showNotification = true;
                let n;
                for (let i = 0; i < this.notificationArr.length; i++) {
                  if (i === 0) {
                    n = '2rem';
                  } else {
                    n = (9 * i) + 'rem';
                  }
                  this.styling.push(n);
                }
              }
            });
          }
        }
      }
    });
  }
}
