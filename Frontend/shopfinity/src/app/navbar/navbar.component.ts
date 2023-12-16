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

  // Handle category filter if user click on a category
  selectCategory(category: string) {
    this.category.emit(category);
  }

  // Handle search if user enter on search bar
  search(event: any) {
    this.searchKeyword.emit(event.target.value);
  }

  // Navigate to home page when user clicks on logo
  homePage() {
    if(sessionStorage.getItem('user') === 'customer') {
      this.router.navigate(['/user/product-list']);
    } else {
      this.router.navigate(['/seller/dashboard']);
    }
  }

}
