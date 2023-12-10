import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ActivatedRoute } from '@angular/router';
import { ProductViewComponent } from './product_view.component';
import { of } from 'rxjs';

describe('ProductViewComponent', () => {
  let component: ProductViewComponent;
  let fixture: ComponentFixture<ProductViewComponent>;
  let activatedRouteMock: any;

  beforeEach(() => {
    activatedRouteMock = {
      snapshot: { paramMap: { get: (param: string) => '1' } }
    };

    TestBed.configureTestingModule({
      declarations: [ProductViewComponent],
      providers: [
        { provide: ActivatedRoute, useValue: activatedRouteMock }
      ],
    });

    fixture = TestBed.createComponent(ProductViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should fetch product details on init', () => {
    spyOn(component, 'loadProductDetails');
    component.ngOnInit();
    expect(component.loadProductDetails).toHaveBeenCalledWith('1');
    expect(component.product).toEqual({
      id: '1',
      name: 'Sample Product',
      description: 'Sample product description.',
      imageUrl: 'sample-image.jpg',
      productBrand: 'Sample Brand',
      category: 'Electronics',
      price: 99.99,
      quantity: 10,
      sale: true,
      discount: 10,
      shippingDetails: 'Free shipping worldwide!',
      productSpecs: 'Sample specifications.'
    });
  });

  
});
