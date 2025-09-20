# Grading Rules:
# 1. Grade out of 10, in increments of 0.5.
# 2. < 3.0 indicates the code fails to function altogether (FAIL).
# 3. 3.0 indicates the .py file works but the code is poorly written.
# 4. 3.5–5.0 indicates many bad practices or loopholes, code may run but is fragile.
# 5. 5.5–7.0 indicates acceptable code with some issues in style or edge cases.
# 6. 7.5–9.0 indicates good code with minor style or best-practice lapses.
# 7. 9.5–10.0 is reserved for excellent, clean, idiomatic, well-tested code.
#
# Issue Severity:
# - CRITICAL: Affects the entire code or dataset handling in all cases.
# - PRACTICE: Bad coding practice that could lead to errors or maintenance burden.

from pygments.lexers import data  # PRACTICE: Unused import, should be removed

orders = [
    {
        "customer": {"name": "Emily", "id": 101, "loyalty": "gold"},
        "items": [
            {"product_name": "Laptop", "category": "Electronics", "price": 1200, "quantity": 1, "discount": 0.1, "gift": False},
            {"product_name": "Mouse", "category": "Electronics", "price": 40, "quantity": 2, "discount": 0.0, "gift": True},
            {"product_name": "Notebook", "category": "Stationery", "price": 10, "quantity": 5, "discount": 0.2, "gift": False}
        ],
        "shipping": {"address": "123 Elm St", "city": "Springfield", "express": True}
    },
    {
        "customer": {"name": "John", "id": 102, "loyalty": "silver"},
        "items": [
            {"product_name": "Book", "category": "Books", "price": 20, "quantity": 2, "discount": 0.05, "gift": False},
            {"product_name": "Pen", "category": "Stationery", "price": 5, "quantity": 10, "discount": 0.0, "gift": False}
        ],
        "shipping": {"address": "456 Oak Ave", "city": "Shelbyville", "express": False}
    },
    {
        "customer": {"name": "Alice", "id": 103, "loyalty": "bronze"},
        "items": [
            {"product_name": "Headphones", "category": "Electronics", "price": 150, "quantity": 1, "discount": 0.15, "gift": True},
            {"product_name": "Book", "category": "Books", "price": 30, "quantity": 1, "discount": 0.0, "gift": False}
        ],
        "shipping": {"address": "789 Pine Rd", "city": "Capital City", "express": True}
    },
    {
        "customer": {"name": "Emily", "id": 101, "loyalty": "gold"},
        "items": [
            {"product_name": "Laptop", "category": "Electronics", "price": 1300, "quantity": 1, "discount": 0.05, "gift": False},
            {"product_name": "Pen", "category": "Stationery", "price": 7, "quantity": 3, "discount": 0.0, "gift": True},
            {"product_name": "Gift Card", "category": "Gift", "price": 100, "quantity": 1, "discount": 0.0, "gift": True}
        ],
        "shipping": {"address": "123 Elm St", "city": "Springfield", "express": False}
    },
    {
        "customer": {"name": "Dave", "id": 104, "loyalty": "none"},
        "items": [
            {"product_name": "Notebook", "category": "Stationery", "price": 12, "quantity": 10, "discount": 0.1, "gift": False},
            {"product_name": "Book", "category": "Books", "price": 25, "quantity": 2, "discount": 0.05, "gift": True},
            {"product_name": "Laptop", "category": "Electronics", "price": 900, "quantity": 1, "discount": 0.0, "gift": False}
        ],
        "shipping": {"address": "321 Maple St", "city": "Shelbyville", "express": True}
    },
    {
        "customer": {"name": "Priya", "id": 105, "loyalty": "silver"},
        "items": [
            {"product_name": "Tablet", "category": "Electronics", "price": 500, "quantity": 2, "discount": 0.2, "gift": True},
            {"product_name": "Notebook", "category": "Stationery", "price": 8, "quantity": 3, "discount": 0.0, "gift": False}
        ],
        "shipping": {"address": "555 Willow Ln", "city": "Star City", "express": False}
    }
]

#Calculate the total revenue for each product category across all orders.
def total_revenue_for_each_category(data: list):  # PRACTICE: Missing docstring and input validation
    revenue = {}
    for order in data:
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing
            if item["category"] not in revenue:  # CRITICAL: KeyError if "category" key missing
                revenue[item["category"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])  # CRITICAL: KeyError if "price", "discount", or "quantity" missing, PRACTICE: Complex calculation, could extract to variable
            else:
                revenue[item["category"]] += ((item["price"]- (item["price"]*item["discount"]))*item["quantity"])  # PRACTICE: Code duplication

    return revenue  # PRACTICE: Function works correctly with discounts and quantities

#Find the customer who spent the most in a single order and the total amount.
def highest_purchase(data: list):  # PRACTICE: Missing docstring
    my_dict = {}
    result = {}
    for order in data:
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing
            if order["customer"]["id"] not in my_dict:  # CRITICAL: KeyError if "customer" or "id" keys missing
                my_dict[order["customer"]["id"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])  # CRITICAL: Still wrong logic - doesn't sum order total, just tracks individual item prices
            elif order["customer"]["id"] in my_dict and ((item["price"] - (item["price"]*item["discount"]))*item["quantity"]) > my_dict[order["customer"]["id"]]:  # CRITICAL: Wrong logic - compares individual item prices instead of order totals
                my_dict[order["customer"]["id"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])
        big_spender = {"id": max(my_dict, key=my_dict.get), "cost": max(my_dict.values())}  # CRITICAL: Calculated inside loop, wrong placement

        if order["customer"]["id"] == big_spender["id"]:  # CRITICAL: Wrong logic and placement
            result = {"name": order["customer"]["name"], "id": max(my_dict, key=my_dict.get), "cost": max(my_dict.values())}  # CRITICAL: KeyError if "name" missing

    return result

#For each customer, compute the average order value.
from collections import Counter  # PRACTICE: Import should be at top of file
def avg_order_value(data: list):  # PRACTICE: Missing docstring
    my_dict = {}
    avg = {}
    result = {}
    id_list = []
    for order in data:
        id_list.append(order["customer"]["id"])  # CRITICAL: KeyError if "customer" or "id" keys missing
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing, CRITICAL: Still wrong logic - adds individual items instead of calculating order totals
            if order["customer"]["id"] not in my_dict:
                my_dict[order["customer"]["id"]] = ((item["price"]- (item["price"]*item["discount"]))*item["quantity"])  # CRITICAL: KeyError if keys missing
            else:
                my_dict[order["customer"]["id"]] += ((item["price"]- (item["price"]*item["discount"]))*item["quantity"])

    count_dict = dict(Counter(id_list))  # PRACTICE: Unnecessarily complex, could use simpler approach
    for k, v in count_dict.items():
        for key, value in my_dict.items():  # CRITICAL: Nested loop is inefficient O(n²)
            if key == k:
                avg[key] = value / v
    for order in data:  # CRITICAL: Another unnecessary loop through all data
        for k, v  in avg.items():  # CRITICAL: Another nested loop, very inefficient
            if (order["customer"]["id"]) == k:  # PRACTICE: Unnecessary parentheses
                result[order["customer"]["name"]] = {"id": k , "spending average": v}  # CRITICAL: KeyError if "name" missing, CRITICAL: Overwrites result for same customer

    return result

#Identify the top 3 products (by name) that generated the highest revenue.
def top3_products(data: list):  # PRACTICE: Missing docstring
    revenue = {}
    for order in data:
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing
            if item["product_name"] not in revenue:  # CRITICAL: KeyError if "product_name" key missing
                revenue[item["product_name"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])  # CRITICAL: KeyError if keys missing, PRACTICE: Code duplication
            else:
                revenue[item["product_name"]] += ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])
    sorted_revenue = (sorted(revenue.items(), key=lambda x: x[1], reverse=True))  # PRACTICE: Unnecessary parentheses
    top3 = dict(sorted_revenue[:3])  # PRACTICE: Good use of slicing
    return top3


# ------ Grading Report ------
# Grade: 3.5 / 10

# Critical Issues:
# 1. ALGORITHM ERROR in second function: Still has the same fundamental flaw - tracks 
#    individual item prices instead of order totals. The function should sum all items 
#    per order, then find the highest order total, but it only tracks the highest 
#    individual item value per customer.
# 2. ALGORITHM ERROR in third function: Still has wrong logic - sums all items for 
#    each customer across ALL orders, then divides by number of orders. Should calculate 
#    total per order first, then average those totals.
# 3. INEFFICIENT ALGORITHMS: Third function still has O(n³) complexity with unnecessary 
#    nested loops and multiple passes through the data.
# 4. WRONG PLACEMENT: Second function still calculates big_spender inside the loop.
# 5. NO ERROR HANDLING: All functions will crash with KeyError if expected keys are missing.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. No input validation or type checking.
# 3. Import statement in middle of file instead of at top.
# 4. Unused import (pygments.lexers.data).
# 5. Code duplication in discount calculation formula.
# 6. Poor variable naming ("my_dict" is not descriptive).
# 7. Unnecessary parentheses and formatting issues.
# 8. Complex calculation expressions that should be extracted to variables.

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. IMPROVEMENT: Now correctly handles discounts and quantities in calculations.
# 3. First and fourth functions work correctly with the new data structure.
# 4. Good use of built-in functions like max(), sorted().
# 5. Consistent return patterns.
# 6. Dictionary aggregation approach is appropriate.

# Detailed Analysis:
# This version shows improvement in handling the more complex data structure with 
# discounts and quantities, but still has the same fundamental algorithmic errors:
#
# 1. IMPROVEMENT - Discount and Quantity Handling: All functions now correctly calculate 
#    revenue using the formula: (price - (price * discount)) * quantity. This is a 
#    significant improvement over the previous version.
#
# 2. CRITICAL FAILURE - Second Function Logic: Still has the same fundamental error. 
#    The function should calculate total order value by summing all items in an order, 
#    then find the customer with the highest single order total. Instead, it only 
#    tracks the highest individual item value per customer.
#
# 3. CRITICAL FAILURE - Third Function Logic: Still calculates average incorrectly. 
#    It sums all items across all orders for each customer, then divides by number 
#    of orders. This doesn't give average order value - it gives total spending 
#    divided by order count, which is different when orders have varying item counts.
#
# Functionality Test Results:
# - Function 1: ✓ Works correctly (calculates category revenue with discounts/quantities)
# - Function 2: ✗ Wrong algorithm - returns highest item value, not highest order total
# - Function 3: ✗ Wrong algorithm - incorrect average calculation method
# - Function 4: ✓ Works correctly (returns top 3 products by revenue with discounts/quantities)
#
# Example of Function 2 Error:
# Emily's first order total: (1200*0.9*1) + (40*1.0*2) + (10*0.8*5) = 1080 + 80 + 40 = 1200
# Emily's second order total: (1300*0.95*1) + (7*1.0*3) + (100*1.0*1) = 1235 + 21 + 100 = 1356
# Should return Emily with order total 1356
# Function only tracks highest individual item: 1235 (Laptop after discount) - WRONG
#
# Example of Function 3 Error:
# For a customer with 2 orders totaling 1000 and 500:
# Correct average order value: (1000 + 500) / 2 = 750
# Function approach: sum all individual items, divide by order count - may give different result
#
# Recommendations:
# 1. Fix second function: Calculate complete order totals first, then find maximum
# 2. Fix third function: Calculate order totals per order, then average per customer
# 3. Extract discount calculation to a helper function to reduce code duplication
# 4. Eliminate unnecessary nested loops and improve algorithm efficiency
# 5. Add comprehensive error handling for missing keys
# 6. Add proper docstrings and input validation
# 7. Move imports to top of file and remove unused imports
# 8. Use more descriptive variable names
# 9. Add unit tests to verify correctness
#
# The code shows good understanding of the new data structure requirements (discounts, 
# quantities) but still has the same fundamental algorithmic flaws in the core logic 
# that prevent it from producing correct results for orders and averages.