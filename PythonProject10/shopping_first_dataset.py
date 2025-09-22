#Calculate the total revenue for each product category across all orders.
#Find the customer who spent the most in a single order and the total amount.
#For each customer, compute the average order value.
#Identify the top 3 products (by name) that generated the highest revenue.

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
    try:
        for order in data:
            for item in order["items"]:
                if item["category"] not in revenue:
                    revenue[item["category"]] = item["price"]
                else:
                    revenue[item["category"]] += item["price"]
    except KeyError as missing_key:
        return f"Key: {missing_key} not found."

    return revenue

#Find the customer who spent the most in a single order and the total amount.
def highest_purchase(data: list):
    my_list = []
    try:
        for order in data:
            total = 0
            for item in order["items"]:
                total += item["price"]
            order["customer"].update({"cost": total})
            my_list.append(order["customer"])
        result = max(my_list, key=lambda x: x["cost"])
    except KeyError as missing_key:
        return f"Key: {missing_key} not found."

    return result

#For each customer, compute the average order value.
def avg_order_value(data: list):
    my_list = []
    my_dict = {}
    try:
        for order in data:
            total = 0
            for item in order["items"]:
                total += item["price"]
            avg = round(total / len(order["items"]), 2)
            order["customer"].update({"avg": avg})
            my_list.append(order["customer"])

        for ele in my_list:
            i = ele["id"]
            if i not in my_dict:
                my_dict[i] = {"name": ele["name"], "total": 0, "count": 0}
            my_dict[i]["count"] += 1
            my_dict[i]["total"] += ele["avg"]

        result = []
        for k, v in my_dict.items():
            avg = round(v["total"] / v["count"], 2)
            result.append({"name": v["name"], "id": k, "avg": avg})
    except KeyError or ZeroDivisionError as missing_key:
        if KeyError:
            return f"Key: {missing_key} not found."
        else:
            return f"There are no orders!!"

    return result

#Identify the top 3 products (by name) that generated the highest revenue.
def top3_products(data: list):
    revenue = {}
    try:
        for order in data:
            for item in order["items"]:
                if item["product_name"] not in revenue:
                    revenue[item["product_name"]] = item["price"]
                else:
                    revenue[item["product_name"]] += item["price"]
    except KeyError as missing_key:
        return f"Key: {missing_key} not found."

    sorted_revenue = sorted(revenue.items(), key=lambda x: x[1], reverse=True)
    top3 = dict(sorted_revenue[:3])
    return top3





if __name__ == '__main__':
    print(total_revenue_for_each_category(orders))
    print(highest_purchase(orders))
    print(avg_order_value(orders))
    print(top3_products(orders))