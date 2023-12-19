from pydantic import BaseModel

class Order(BaseModel):
    id: int
    #customer_id: int

'''
from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    address1: str
    address2: Optional[str]
    city: str
    province: Optional[str]
    country: str
    zip: str

class LineItem(BaseModel):
    product_id: int
    variant_id: int
    quantity: int
    price: str
    title: str
    # Add other relevant fields from the Shopify line item structure

class Order(BaseModel):
    id: int
    email: Optional[str]
    closed_at: Optional[str]
    created_at: str
    updated_at: str
    total_price: str
    subtotal_price: str
    total_weight: Optional[int]
    total_tax: str
    currency: str
    financial_status: str
    confirmed: bool
    total_discounts: str
    total_line_items_price: str
    cart_token: Optional[str]
    buyer_accepts_marketing: bool
    name: str
    referring_site: Optional[str]
    line_items: List[LineItem]
    shipping_address: Optional[Address]
    billing_address: Optional[Address]
    customer_id: int  


'''
