from flask import Blueprint,jsonify, request
import time
data_fetch = Blueprint("data_fetch", __name__)

shopify_mock_data = {
  "products": [
    {
      "id": 1,
      "title": "Product 1",
      "description": "This is a description of Product 1",
      "price": 19.99,
      "variants": [
        {
          "id": 1,
          "sku": "PROD1-VAR1",
          "price": 19.99,
          "inventory_quantity": 10
        },
        {
          "id": 2,
          "sku": "PROD1-VAR2",
          "price": 24.99,
          "inventory_quantity": 5
        }
      ]
    },
    {
      "id": 2,
      "title": "Product 2",
      "description": "This is a description of Product 2",
      "price": 9.99,
      "variants": [
        {
          "id": 3,
          "sku": "PROD2-VAR1",
          "price": 9.99,
          "inventory_quantity": 15
        }
      ]
    }
  ],
  "customers": [
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@example.com",
      "phone": "123-456-7890",
      "addresses": [
        {
          "id": 1,
          "address1": "123 Main St",
          "city": "Anytown",
          "province": "CA",
          "country": "USA",
          "zip": "12345"
        }
      ]
    }
  ],
  "orders": [
    {
      "id": 1,
      "customer_id": 1,
      "order_date": "2022-01-01",
      "total": 19.99,
      "line_items": [
        {
          "id": 1,
          "product_id": 1,
          "quantity": 1,
          "price": 19.99
        }
      ]
    }
  ]
}

def update_to_lowercase(data):
    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = update_to_lowercase(value)
        elif isinstance(value, list):
            data[key] = [update_to_lowercase(item) if isinstance(item, dict) else item.lower() for item in value]
        elif isinstance(value, str):
            data[key] = value.lower()
    return data


# endpoint to fetch dummy shopify data
@data_fetch.route("/fetch-data", methods=["GET"])
def fetch_data():
  try:
    # add a delay to simulate the actual shopify call
    time.sleep(1)
    return jsonify({"message":"successfully fetched shopify data",  "data":shopify_mock_data})
  except Exception as error:
    print("error occoured to fetch data")

# function to get processed data after converting all values to lowercase
@data_fetch.route("/get-processed-data", methods = ["POST"])
def fetch_processsed_data():
   try:
    data = request.get_json()
    processed_data = update_to_lowercase(dict(data))
    return jsonify({"message":"successfully fetched processed data", "data":processed_data})
   except Exception as error:
    print("error occoured to fetch processed data", error)
    return jsonify({"error":"error occoured to fetch processed data"}), 500