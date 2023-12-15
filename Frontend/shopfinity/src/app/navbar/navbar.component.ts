import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent {

  @Output() category: EventEmitter<string> = new EventEmitter<string>();
  @Output() searchKeyword: EventEmitter<string> = new EventEmitter<string>();

  @Input() showCategoryBar = false; 

  constructor(private router: Router){}

  selectCategory(category: string) {
    this.category.emit(category);
  }

  search(event: any) {
    this.searchKeyword.emit(event.target.value);
  }
  homePage() {
    if(sessionStorage.getItem('user') === 'customer') {
      this.router.navigate(['/user/product-list']);
    } else {
      this.router.navigate(['/seller/dashboard']);
    }
  }

}
