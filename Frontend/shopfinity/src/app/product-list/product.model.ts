export interface Product {
    _id: string;
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