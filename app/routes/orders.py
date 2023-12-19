''' 
from fastapi import APIRouter, HTTPException
from ..services.shopify import fetch_orders
from ..models import Order
from typing import List

router = APIRouter()

@router.get("/orders/{customer_id}", response_model=List[Order])
async def read_orders(customer_id: str):  # Accept customer_id as string to handle different formats
    # Check for valid customer ID format (e.g., numeric)
    if not customer_id.isdigit():
        raise HTTPException(status_code=404, detail="Invalid customer ID format")

    # Convert customer_id to int if it's a valid format
    numeric_customer_id = int(customer_id)

    try:
        orders_data = await fetch_orders(numeric_customer_id)
        if not orders_data:
            raise HTTPException(status_code=404, detail="No orders found for this customer ID")
        return [Order(**order) for order in orders_data]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
'''

from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Order
from ..services.shopify import fetch_orders

router = APIRouter()

@router.get("/orders/{customer_id}", response_model=List[Order])
async def read_orders(customer_id: str):
    try:
        # Validate and convert customer ID to an integer
        numeric_customer_id = int(customer_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Invalid customer ID format")

    # Handle edge case for extremely large customer IDs
    if numeric_customer_id > 9999999999999999:
        raise HTTPException(status_code=404, detail="Customer ID is too large")

    orders_data = await fetch_orders(numeric_customer_id)
    if orders_data is None:
        raise HTTPException(status_code=404, detail="No orders found for this customer ID")

    return [Order(**order) for order in orders_data]
