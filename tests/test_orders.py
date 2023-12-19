'''
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_orders():
    response = client.get("/orders/5592251564110")
    assert response.status_code == 200

def test_read_orders_invalid_id():
    response = client.get("/orders/123c")
    #5592251564110
    assert response.status_code == 404
'''

from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

# Example of valid customer IDs (adjust according to your data)
VALID_CUSTOMER_IDS = [5592251564110, 2669175815] 
INVALID_CUSTOMER_IDS = [0, "invalid_id"] # Non-existing or invalid format IDs

# Test with valid customer IDs
@pytest.mark.parametrize("customer_id", VALID_CUSTOMER_IDS)
def test_get_orders_valid_customer_id(customer_id):
    response = client.get(f"/orders/{customer_id}")
    assert response.status_code == 200
    # Additional assertions to verify the response content

# Test with invalid customer IDs
@pytest.mark.parametrize("customer_id", INVALID_CUSTOMER_IDS)
def test_get_orders_invalid_customer_id(customer_id):
    response = client.get(f"/orders/{customer_id}")
    assert response.status_code == 404 # or other appropriate error code
    # Additional assertions for error response

# Test edge cases
def test_get_orders_edge_cases():
    # Example: extremely large ID
    response = client.get("/orders/99999999999999999999")
    assert response.status_code == 404 # Assuming this ID does not exist

    # Additional edge case tests as required
