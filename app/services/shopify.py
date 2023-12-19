'''
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

async def get_orders(customer_id: int):
    shop_url = os.getenv("SHOP_URL")
    access_token = os.getenv("ACCESS_TOKEN")
    url = f"https://{shop_url}/admin/api/2023-01/orders.json?customer_id={customer_id}"
    headers = {"X-Shopify-Access-Token": access_token}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["orders"]  

'''

import os
import httpx
from dotenv import load_dotenv
from typing import Optional, List, Dict

load_dotenv()

async def fetch_orders(customer_id: int) -> Optional[List[Dict]]:
    shop_url = os.getenv("SHOP_URL")
    access_token = os.getenv("ACCESS_TOKEN")
    #url = f"https://{shop_url}/admin/api/2023-01/orders.json?customer_id={customer_id}"
    url = f"https://{shop_url}/admin/api/2022-01/orders.json?customer_id={customer_id}"
    headers = {"X-Shopify-Access-Token": access_token}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)

            # Check for successful response
            if response.status_code == 200:
                orders = response.json().get("orders")
                return orders if orders else None

            # Handle other response statuses (e.g., 404, 401, etc.)
            response.raise_for_status()

        except httpx.HTTPStatusError as e:
            # Log the error details here, if necessary
            print(f"HTTP error occurred: {e}")
            return None
        except httpx.RequestError as e:
            # Log the request error details here, if necessary
            print(f"An error occurred while requesting {e.request.url!r}.")
            return None

    return None
