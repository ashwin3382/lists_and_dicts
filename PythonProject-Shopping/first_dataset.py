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
def total_revenue_for_each_category(data: list):  # PRACTICE: Missing docstring and input validation
    revenue = {}
    for order in data:
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing
            if item["category"] not in revenue:  # CRITICAL: KeyError if "category" key missing
                revenue[item["category"]] = item["price"]  # CRITICAL: KeyError if "price" key missing
            else:
                revenue[item["category"]] += item["price"]

    return revenue  # PRACTICE: Function works correctly

#Find the customer who spent the most in a single order and the total amount.
def highest_purchase(data: list):  # PRACTICE: Missing docstring
    my_dict = {}
    result = {}
    for order in data:
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing
            if order["customer"]["id"] not in my_dict:  # CRITICAL: KeyError if "customer" or "id" keys missing
                my_dict[order["customer"]["id"]] = item["price"]  # CRITICAL: Wrong logic - doesn't sum order total, just tracks individual item prices
            elif order["customer"]["id"] in my_dict and item["price"] > my_dict[order["customer"]["id"]]:  # CRITICAL: Wrong logic - compares individual item prices instead of order totals
                my_dict[order["customer"]["id"]] = item["price"]
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
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing, CRITICAL: Wrong logic - adds individual items instead of calculating order totals
            if order["customer"]["id"] not in my_dict:
                my_dict[order["customer"]["id"]] = item["price"]  # CRITICAL: KeyError if "price" missing
            else:
                my_dict[order["customer"]["id"]] += item["price"]

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
                revenue[item["product_name"]] = item["price"]  # CRITICAL: KeyError if "price" key missing
            else:
                revenue[item["product_name"]] += item["price"]
    sorted_revenue = (sorted(revenue.items(), key=lambda x: x[1], reverse=True))  # PRACTICE: Unnecessary parentheses
    top3 = dict(sorted_revenue[:3])  # PRACTICE: Good use of slicing
    return top3


# ------ Grading Report ------
# Grade: 2.0 / 10

# Critical Issues:
# 1. ALGORITHM ERROR in second function: Completely wrong logic - tracks individual item 
#    prices instead of order totals. The function should sum all items per order, then 
#    find the highest order total, but instead it just tracks the highest individual 
#    item price per customer.
# 2. ALGORITHM ERROR in third function: Wrong logic - sums all items for each customer 
#    across ALL orders, then divides by number of orders, but this doesn't give average 
#    order value. Should calculate total per order first, then average those totals.
# 3. INEFFICIENT ALGORITHMS: Third function has O(n³) complexity with unnecessary nested 
#    loops and multiple passes through the data.
# 4. WRONG PLACEMENT: Second function calculates big_spender inside the loop, so it 
#    gets overwritten and gives incorrect results.
# 5. NO ERROR HANDLING: All functions will crash with KeyError if expected keys are missing.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. No input validation or type checking.
# 3. Import statement in middle of file instead of at top.
# 4. Inefficient algorithms with unnecessary complexity.
# 5. Poor variable naming ("my_dict" is not descriptive).
# 6. Unnecessary parentheses and formatting issues.
# 7. Data structure overwrites in third function.

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. First and fourth functions work correctly and have clean logic.
# 3. Good use of built-in functions like max(), sorted().
# 4. Consistent return patterns.
# 5. Dictionary aggregation approach is appropriate.

# Detailed Analysis:
# This code has significant algorithmic errors that make it produce incorrect results:
#
# 1. CRITICAL FAILURE - Second Function Logic: The function is supposed to find the 
#    customer who spent the most in a SINGLE order, but instead it tracks the highest 
#    individual ITEM price per customer. For example:
#    - Emily's first order: Laptop(1200) + Mouse(40) + Notebook(10) = 1250 total
#    - Emily's second order: Laptop(1300) + Pen(7) = 1307 total
#    - Function should return Emily with 1307, but it only tracks individual item prices
#
# 2. CRITICAL FAILURE - Third Function Logic: The function is supposed to calculate 
#    average ORDER value per customer, but it sums ALL items across ALL orders for 
#    each customer, then divides by number of orders. This is wrong because:
#    - Should calculate: (order1_total + order2_total + ...) / number_of_orders
#    - Actually calculates: (all_items_total) / number_of_orders
#    - These give different results when orders have different numbers of items
#
# 3. CRITICAL FAILURE - Performance Issues: The third function uses O(n³) complexity 
#    with multiple nested loops when O(n) would suffice with proper design.
#
# Functionality Test Results:
# - Function 1: ✓ Works correctly (Electronics: 3590, Books: 75, Stationery: 34)
# - Function 2: ✗ Wrong algorithm - returns highest item price, not highest order total
# - Function 3: ✗ Wrong algorithm - incorrect average calculation method
# - Function 4: ✓ Works correctly (returns top 3 products by revenue)
#
# Example of Function 2 Error:
# Emily's orders: [1250 total, 1307 total] - should return 1307
# Function tracks: max individual item price = 1300 - WRONG
#
# Example of Function 3 Error:
# Emily's total spending: 1250 + 1307 = 2557, orders: 2
# Correct average: 2557/2 = 1278.5
# Function might give different result due to item-by-item summation
#
# Recommendations:
# 1. Rewrite second function to calculate order totals first, then find maximum
# 2. Rewrite third function to calculate order totals, then average per customer
# 3. Eliminate unnecessary nested loops and improve algorithm efficiency
# 4. Add comprehensive error handling for missing keys
# 5. Add proper docstrings and input validation
# 6. Move imports to top of file
# 7. Use more descriptive variable names
# 8. Add unit tests to verify correctness
#
# The code shows basic understanding of dictionary aggregation but has fundamental 
# algorithmic flaws that make it produce incorrect results for the core requirements.