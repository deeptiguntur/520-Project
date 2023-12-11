export interface Product {
    productId: number;
    productName: string;
    brand: string;
    productDesc: string;
    category: string;
    price: number;
    quantity: number;
    sale: boolean;
    discount: number;
    imgData: string[];
}