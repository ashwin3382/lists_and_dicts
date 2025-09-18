
orders = [
    {
        "customer": {"name": "Emily", "id": 101},
        "items": [
            {"product_name": "Laptop", "category": "Electronics", "price": 1200},
            {"product_name": "Mouse", "category": "Electronics", "price": 40},
            {"product_name": "Notebook", "category": "Stationery", "price": 10}
        ],
        "shipping": {"address": "123 Elm St", "city": "Springfield"}
    },
    {
        "customer": {"name": "John", "id": 102},
        "items": [
            {"product_name": "Book", "category": "Books", "price": 20},
            {"product_name": "Pen", "category": "Stationery", "price": 5}
        ],
        "shipping": {"address": "456 Oak Ave", "city": "Shelbyville"}
    },
    {
        "customer": {"name": "Alice", "id": 103},
        "items": [
            {"product_name": "Headphones", "category": "Electronics", "price": 150},
            {"product_name": "Book", "category": "Books", "price": 30}
        ],
        "shipping": {"address": "789 Pine Rd", "city": "Capital City"}
    },
    {
        "customer": {"name": "Emily", "id": 101},
        "items": [
            {"product_name": "Laptop", "category": "Electronics", "price": 1300},
            {"product_name": "Pen", "category": "Stationery", "price": 7}
        ],
        "shipping": {"address": "123 Elm St", "city": "Springfield"}
    },
    {
        "customer": {"name": "Dave", "id": 104},
        "items": [
            {"product_name": "Notebook", "category": "Stationery", "price": 12},
            {"product_name": "Book", "category": "Books", "price": 25},
            {"product_name": "Laptop", "category": "Electronics", "price": 900}
        ],
        "shipping": {"address": "321 Maple St", "city": "Shelbyville"}
    }
]





#Calculate the total revenue for each product category across all orders.
def total_revenue_for_each_category(data: list):
    revenue = {}
    for order in data:
        for item in order["items"]:
            if item["category"] not in revenue:
                revenue[item["category"]] = item["price"]
            else:
                revenue[item["category"]] += item["price"]

    return revenue

#Find the customer who spent the most in a single order and the total amount.
def highest_purchase(data: list):
    my_dict = {}
    result = {}
    for order in data:
        for item in order["items"]:
            if order["customer"]["id"] not in my_dict:
                my_dict[order["customer"]["id"]] = item["price"]
            elif order["customer"]["id"] in my_dict and item["price"] > my_dict[order["customer"]["id"]]:
                my_dict[order["customer"]["id"]] = item["price"]
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
                my_dict[order["customer"]["id"]] = item["price"]
            else:
                my_dict[order["customer"]["id"]] += item["price"]

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
                revenue[item["product_name"]] = item["price"]
            else:
                revenue[item["product_name"]] += item["price"]
    sorted_revenue = (sorted(revenue.items(), key=lambda x: x[1], reverse=True))
    top3 = dict(sorted_revenue[:3])
    return top3

