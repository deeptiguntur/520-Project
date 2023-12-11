import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { AddProductComponent } from './seller-page/add-product/add-product.component';
import { SellerPageComponent } from './seller-page/seller-page.component';
import { OrderDetailsComponent } from './order-details/order-details.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductViewComponent } from './product-view/product-view.component';

const routes: Routes = [
  {path: '', redirectTo: '/login', pathMatch: 'full' },
  {path: 'login', component: LoginComponent},
  {path: 'signup', component: SignUpComponent},
  {path: 'add-product', component: AddProductComponent},
  {path: 'seller/dashboard', component: SellerPageComponent},
  {path: 'user/cart', component: OrderDetailsComponent},
  {path: 'user/product-list', component: ProductListComponent},
  {path: 'product/view', component: ProductViewComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {

 }
