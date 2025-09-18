from pygments.lexers import data

orders = [
    {
        "customer": {"name": "Emily", "id": 101, "loyalty": "gold"},
        "order_id": "A1001",
        "items": [
            {"product_name": "Laptop", "category": "Electronics", "price": 1200, "quantity": 1, "discount": 0.1, "gift": False, "warranty_years": 2},
            {"product_name": "Mouse", "category": "Electronics", "price": 40, "quantity": 2, "discount": 0.0, "gift": True, "warranty_years": 1},
            {"product_name": "Notebook", "category": "Stationery", "price": 10, "quantity": 5, "discount": 0.2, "gift": False}
        ],
        "shipping": {"address": "123 Elm St", "city": "Springfield", "express": True, "shipped_by": "FedEx"},
        "payment": {"method": "credit_card", "transaction_id": "TXN123A", "split": False},
        "order_notes": ["Leave at front door", "Include gift receipt"]
    },
    {
        "customer": {"name": "John", "id": 102, "loyalty": "silver"},
        "order_id": "A1002",
        "items": [
            {"product_name": "Book", "category": "Books", "price": 20, "quantity": 2, "discount": 0.05, "gift": False, "author": "Author A"},
            {"product_name": "Pen", "category": "Stationery", "price": 5, "quantity": 10, "discount": 0.0, "gift": False}
        ],
        "shipping": {"address": "456 Oak Ave", "city": "Shelbyville", "express": False, "shipped_by": "UPS"},
        "payment": {"method": "paypal", "transaction_id": "TXN124B", "split": True, "split_with": [103]},
        "order_notes": []
    },
    {
        "customer": {"name": "Alice", "id": 103, "loyalty": "bronze"},
        "order_id": "A1003",
        "items": [
            {"product_name": "Headphones", "category": "Electronics", "price": 150, "quantity": 1, "discount": 0.15, "gift": True, "warranty_years": 1},
            {"product_name": "Book", "category": "Books", "price": 30, "quantity": 1, "discount": 0.0, "gift": False, "author": "Author B"}
        ],
        "shipping": {"address": "789 Pine Rd", "city": "Capital City", "express": True, "shipped_by": "DHL"},
        "payment": {"method": "debit_card", "transaction_id": "TXN125C", "split": False},
        "order_notes": ["Fragile"]
    },
    {
        "customer": {"name": "Emily", "id": 101, "loyalty": "gold"},
        "order_id": "A1004",
        "items": [
            {"product_name": "Laptop", "category": "Electronics", "price": 1300, "quantity": 1, "discount": 0.05, "gift": False, "warranty_years": 3},
            {"product_name": "Pen", "category": "Stationery", "price": 7, "quantity": 3, "discount": 0.0, "gift": True},
            {"product_name": "Gift Card", "category": "Gift", "price": 100, "quantity": 1, "discount": 0.0, "gift": True}
        ],
        "shipping": {"address": "123 Elm St", "city": "Springfield", "express": False, "shipped_by": "FedEx"},
        "payment": {"method": "credit_card", "transaction_id": "TXN126D", "split": False},
        "order_notes": []
    },
    {
        "customer": {"name": "Dave", "id": 104, "loyalty": "none"},
        "order_id": "A1005",
        "items": [
            {"product_name": "Notebook", "category": "Stationery", "price": 12, "quantity": 10, "discount": 0.1, "gift": False},
            {"product_name": "Book", "category": "Books", "price": 25, "quantity": 2, "discount": 0.05, "gift": True, "author": "Author C"},
            {"product_name": "Laptop", "category": "Electronics", "price": 900, "quantity": 1, "discount": 0.0, "gift": False, "warranty_years": 1}
        ],
        "shipping": {"address": "321 Maple St", "city": "Shelbyville", "express": True, "shipped_by": "UPS"},
        "payment": {"method": "paypal", "transaction_id": "TXN127E", "split": True, "split_with": [101, 102]},
        "order_notes": ["Urgent delivery"]
    },
    {
        "customer": {"name": "Priya", "id": 105, "loyalty": "silver"},
        "order_id": "A1006",
        "items": [
            {"product_name": "Tablet", "category": "Electronics", "price": 500, "quantity": 2, "discount": 0.2, "gift": True, "warranty_years": 2},
            {"product_name": "Notebook", "category": "Stationery", "price": 8, "quantity": 3, "discount": 0.0, "gift": False}
        ],
        "shipping": {"address": "555 Willow Ln", "city": "Star City", "express": False, "shipped_by": "DHL"},
        "payment": {"method": "credit_card", "transaction_id": "TXN128F", "split": False},
        "order_notes": ["Wrap as a gift"]
    },
    {
        "customer": {"name": "Frank", "id": 106, "loyalty": "bronze"},
        "order_id": "A1007",
        "items": [
            {"product_name": "Camera", "category": "Electronics", "price": 800, "quantity": 1, "discount": 0.1, "gift": False, "warranty_years": 2},
            {"product_name": "Tripod", "category": "Electronics", "price": 50, "quantity": 2, "discount": 0.05, "gift": False}
        ],
        "shipping": {"address": "66 Ocean Dr", "city": "Metropolis", "express": True, "shipped_by": "FedEx"},
        "payment": {"method": "debit_card", "transaction_id": "TXN129G", "split": False},
        "order_notes": ["Deliver before noon"]
    }
]

#Calculate the total revenue for each product category across all orders.
def total_revenue_for_each_category(data: list):
    revenue = {}
    for order in data:
        for item in order["items"]:
            if item["category"] not in revenue:
                revenue[item["category"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])
            else:
                revenue[item["category"]] += ((item["price"]- (item["price"]*item["discount"]))*item["quantity"])

    return revenue

#Find the customer who spent the most in a single order and the total amount.
def highest_purchase(data: list):
    my_dict = {}
    result = {}
    for order in data:
        for item in order["items"]:
            if order["customer"]["id"] not in my_dict:
                my_dict[order["customer"]["id"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])
            elif order["customer"]["id"] in my_dict and ((item["price"] - (item["price"]*item["discount"]))*item["quantity"]) > my_dict[order["customer"]["id"]]:
                my_dict[order["customer"]["id"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])
        big_spender = {"id": max(my_dict, key=my_dict.get), "cost": max(my_dict.values())}

        if order["customer"]["id"] == big_spender["id"]:
            result = {"name": order["customer"]["name"], "id": max(my_dict, key=my_dict.get), "cost": max(my_dict.values())}

    return result

#For each customer, compute the average order value.
from collections import Counter
def avg_order_value(data: list):
    my_dict = {}
    avg = {}
    result = {}
    id_list = []
    for order in data:
        id_list.append(order["customer"]["id"])
        for item in order["items"]:
            if order["customer"]["id"] not in my_dict:
                my_dict[order["customer"]["id"]] = ((item["price"]- (item["price"]*item["discount"]))*item["quantity"])
            else:
                my_dict[order["customer"]["id"]] += ((item["price"]- (item["price"]*item["discount"]))*item["quantity"])

    count_dict = dict(Counter(id_list))
    for k, v in count_dict.items():
        for key, value in my_dict.items():
            if key == k:
                avg[key] = value / v
    for order in data:
        for k, v  in avg.items():
            if (order["customer"]["id"]) == k:
                result[order["customer"]["name"]] = {"id": k , "spending average": v}

    return result

#Identify the top 3 products (by name) that generated the highest revenue.
def top3_products(data: list):
    revenue = {}
    for order in data:
        for item in order["items"]:
            if item["product_name"] not in revenue:
                revenue[item["product_name"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])
            else:
                revenue[item["product_name"]] += ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])
    sorted_revenue = (sorted(revenue.items(), key=lambda x: x[1], reverse=True))
    top3 = dict(sorted_revenue[:3])
    return top3

