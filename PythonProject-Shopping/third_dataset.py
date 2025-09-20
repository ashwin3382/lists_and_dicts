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
                my_dict[order["customer"]["id"]] = ((item["price"] - (item["price"]*item["discount"]))*item["quantity"])  # CRITICAL: STILL wrong logic - doesn't sum order total, just tracks individual item prices
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
        for item in order["items"]:  # CRITICAL: KeyError if "items" key missing, CRITICAL: STILL wrong logic - adds individual items instead of calculating order totals
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
# 1. ALGORITHM ERROR in second function: Despite the expanded dataset, the function STILL 
#    has the same fundamental flaw - tracks individual item prices instead of order totals. 
#    This completely misses the requirement to find the customer with the highest SINGLE ORDER total.
# 2. ALGORITHM ERROR in third function: STILL has wrong logic - sums all items for each 
#    customer across ALL orders, then divides by number of orders. This doesn't calculate 
#    average order value correctly.
# 3. INEFFICIENT ALGORITHMS: Third function still has O(n³) complexity with unnecessary 
#    nested loops and multiple data passes.
# 4. WRONG PLACEMENT: Second function still calculates big_spender inside the loop, 
#    causing incorrect results.
# 5. NO ERROR HANDLING: All functions will crash with KeyError if expected keys are missing.
# 6. NO PROGRESS: Despite multiple iterations and dataset expansions, the core algorithmic 
#    errors remain unchanged.

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
# 2. Correctly handles discounts and quantities in calculations.
# 3. First and fourth functions work correctly with the expanded data structure.
# 4. Good use of built-in functions like max(), sorted().
# 5. Consistent return patterns.
# 6. Dictionary aggregation approach is appropriate.
# 7. Data structure correctly expanded with additional fields (order_id, payment, etc.).

# Detailed Analysis:
# This is the FOURTH iteration of essentially the same code with the same fundamental 
# errors, despite progressively more complex datasets:
#
# 1. NO IMPROVEMENT IN CORE LOGIC: Despite adding order_id, payment details, shipping 
#    information, and other fields to the dataset, the core algorithmic errors in 
#    functions 2 and 3 remain completely unchanged.
#
# 2. CRITICAL FAILURE - Second Function: The function should calculate the total for 
#    each ORDER (sum of all items in that order), then find which customer has the 
#    highest single order total. Instead, it tracks individual item values per customer.
#    
#    Example with current dataset:
#    - Emily's Order A1001: (1200*0.9*1) + (40*1.0*2) + (10*0.8*5) = 1080 + 80 + 40 = 1200
#    - Emily's Order A1004: (1300*0.95*1) + (7*1.0*3) + (100*1.0*1) = 1235 + 21 + 100 = 1356
#    - Should find Emily with single order total of 1356
#    - Function only tracks highest individual item: 1235 (Laptop) - WRONG
#
# 3. CRITICAL FAILURE - Third Function: Should calculate order totals first, then average:
#    - Correct: Calculate each order total, then (order1 + order2 + ...) / num_orders
#    - Current: Sum all individual items, divide by order count - gives wrong result
#
# 4. PERSISTENT ISSUES: Same inefficiencies, same poor practices, same lack of error 
#    handling as in previous iterations.
#
# Functionality Test Results:
# - Function 1: ✓ Works correctly (calculates category revenue with discounts/quantities)
# - Function 2: ✗ Wrong algorithm - same error as previous 3 iterations
# - Function 3: ✗ Wrong algorithm - same error as previous 3 iterations  
# - Function 4: ✓ Works correctly (returns top 3 products by revenue)
#
# Pattern of Non-Improvement:
# This represents a concerning pattern where:
# - Dataset complexity increased (simple → discounts → quantities → full order details)
# - Cosmetic improvements made (better variable names in some places)
# - Core algorithmic errors remain completely unchanged across 4 iterations
# - No learning or improvement demonstrated in the fundamental logic
#
# Recommendations:
# 1. URGENT: Understand the difference between individual item values and order totals
# 2. Fix second function: Group items by order, calculate order totals, find maximum
# 3. Fix third function: Calculate order totals per order, then average per customer
# 4. Stop expanding datasets until core logic is correct
# 5. Add comprehensive error handling
# 6. Improve algorithm efficiency 
# 7. Add unit tests to verify correctness
# 8. Focus on understanding requirements rather than data structure complexity
#
# This code demonstrates a failure to learn from previous feedback and shows no 
# improvement in the core algorithmic understanding despite multiple iterations.