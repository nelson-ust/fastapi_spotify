
from pydantic import BaseModel

class Order(BaseModel):
    order_id: int
    customer_id: int
    