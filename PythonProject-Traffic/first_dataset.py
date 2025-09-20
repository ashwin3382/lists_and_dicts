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

traffic_data = {
    "Metropolis": {
        "Downtown": [
            {"road_name": "Main St", "hourly_counts": [120, 150, 130, 140, 160, 170, 180, 200, 220, 210, 190, 170, 160, 150, 140, 145, 155, 165, 175, 185, 195, 205, 215, 225]},
            {"road_name": "2nd Ave", "hourly_counts": [80, 90, 85, 100, 110, 120, 130, 140, 150, 160, 155, 145, 135, 125, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70]},
        ],
        "Uptown": [
            {"road_name": "Broadway", "hourly_counts": [200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430]},
            {"road_name": "5th St", "hourly_counts": [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330]},
        ]
    },
    "Gotham": {
        "Central": [
            {"road_name": "Gotham Blvd", "hourly_counts": [95, 105, 115, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320]},
            {"road_name": "Arkham Rd", "hourly_counts": [60, 65, 70, 75, 80, 85, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]}
        ],
        "Westside": [
            {"road_name": "Wayne Ave", "hourly_counts": [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380]},
        ]
    }
}

# For each city, calculate the zone with the highest average traffic per hour.
def zone_with_highest_traffic_avg(data: dict):  # PRACTICE: Missing docstring and input validation
    total = {}
    result = {}
    for cities, zones in data.items():
        for zone, roads in zones.items():
            total_traffic = 0
            for road in roads:  # CRITICAL: KeyError if roads list is empty or malformed
                total_traffic += (sum(road["hourly_counts"]))  # CRITICAL: KeyError if "hourly_counts" key missing, PRACTICE: Unnecessary parentheses
                avg = round(total_traffic / (len(road["hourly_counts"])*len(roads)), 2)  # CRITICAL: Wrong calculation - calculates average inside loop, overwrites previous calculations
                if cities in total:
                    total[cities].update({zone: avg})
                else:
                    total[cities] = ({zone: avg})  # PRACTICE: Unnecessary parentheses

    for cities, zones in total.items():
        result.update({cities:max(total.get(cities).items())})  # CRITICAL: max() on dict items returns tuple, not expected format
    return result

# Identify the road (across all cities and zones) that saw the single highest vehicle count in any given hour, and output its city, zone, road name, and the hour.
def max_vehicle_count(data: dict):  # PRACTICE: Missing docstring
    road_list = []
    traffic_at_specific_hour = {}
    road_dict = {}
    traffic_list = []
    max_traffic_with_zone = {}
    result = {}
    max_traffic_dict = {}
    for cities in data:
        for zones in data[cities]:
            for roads in data[cities][zones]:  # CRITICAL: KeyError if zones or roads keys missing
                road_list.append(roads["road_name"])  # CRITICAL: KeyError if "road_name" missing
                for traffic in roads:  # PRACTICE: Poor variable naming, 'traffic' is actually a key name
                    if isinstance(roads[traffic], list):  # PRACTICE: Should check specifically for "hourly_counts"
                        traffic_list.append(max(roads[traffic]))  # CRITICAL: Assumes list is not empty
                        traffic_at_specific_hour[max(roads[traffic])] = {"Hour": roads[traffic].index(max(roads[traffic]))}  # CRITICAL: Duplicate max() calculation, inefficient

    for road in road_list:  # CRITICAL: Complex matching logic using index - fragile and error-prone
        for k, v in traffic_at_specific_hour.items():
            if road_list.index(road) == traffic_list.index(k):  # CRITICAL: index() can raise ValueError if item not found
                road_dict[road] = [{"Vehicle count": k},v]

    for k, v in road_dict.items():
        if (max(v[0].values())) == max(traffic_list):  # PRACTICE: Unnecessary parentheses, complex nested access
            max_traffic_dict[k] = v
    for cities in data:  # CRITICAL: Another full iteration through data - inefficient
        for zones in data[cities]:
            for roads in data[cities][zones]:
                for k, v in max_traffic_dict.items():  # CRITICAL: Nested loop creates O(n²) complexity
                    if k == roads["road_name"]:
                        max_traffic_with_zone[zones] = [{"Road name":k},v]  # CRITICAL: Overwrites if multiple roads in same zone
                        result[cities] = max_traffic_with_zone  # CRITICAL: Overwrites if multiple cities

    return result

# For each city, compute total vehicle counts per hour (aggregate all roads and zones) and list the hour with the highest and lowest total traffic.
def total_vehicle_count(data: dict):  # PRACTICE: Missing docstring, doesn't return anything

    for cities in data:
        vehicle_count =  []  # PRACTICE: Extra space before =
        my_list = []
        print(cities)  # PRACTICE: Should return data instead of printing
        for zones in data[cities]:
            for roads in data[cities][zones]:  # CRITICAL: KeyError if zones or roads keys missing
                vehicle_count.append((roads["hourly_counts"]))  # CRITICAL: KeyError if "hourly_counts" missing, PRACTICE: Unnecessary parentheses

        for i in zip(*vehicle_count):  # PRACTICE: Good use of zip for aggregation
            my_list.append(sum(i))

        print({"max vehicle count":max(my_list)} , {"hour": my_list.index(max(my_list))})  # PRACTICE: Should return, not print, CRITICAL: max() called twice
        print({"min vehicle count":min(my_list)} , {"hour": my_list.index(min(my_list))})  # PRACTICE: Should return, not print, CRITICAL: min() called twice


# ------ Grading Report ------
# Grade: 4.0 / 10

# Critical Issues:
# 1. ALGORITHM ERROR in first function: Calculates average inside the road loop, so the 
#    calculation gets overwritten for each road in a zone. Should calculate total for 
#    all roads in zone first, then divide by total hours across all roads.
# 2. COMPLEX AND FRAGILE LOGIC in second function: Uses multiple lists and index matching 
#    which is error-prone and fragile. The logic is overly complicated and hard to follow.
# 3. INEFFICIENT ALGORITHMS: Second function has O(n²) complexity with unnecessary nested 
#    loops and multiple full data iterations.
# 4. NO RETURN VALUE: Third function prints instead of returning results, making it 
#    unusable programmatically.
# 5. NO ERROR HANDLING: All functions will crash with KeyError if expected keys are missing.
# 6. DATA OVERWRITES: Second function overwrites results if multiple items exist in 
#    same zone or city.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. No input validation or type checking.
# 3. Poor variable naming ("my_list", "traffic" for keys).
# 4. Unnecessary parentheses and formatting issues.
# 5. Code duplication (multiple max()/min() calls).
# 6. Complex nested data access patterns.
# 7. Inefficient algorithms with redundant iterations.

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. Good use of zip() for aggregating parallel lists in third function.
# 3. Proper use of dictionary comprehensions and updates.
# 4. Round() function used for decimal precision.
# 5. Meaningful variable names in some places.
# 6. Functions attempt to solve the stated problems.

# Detailed Analysis:
# The code attempts to solve complex traffic analysis problems but has significant issues:
#
# 1. CRITICAL FAILURE - First Function Average Calculation: The function calculates 
#    average inside the road loop, meaning:
#    - For Downtown with 2 roads: processes road1, calculates avg, then processes road2, 
#      overwrites the average calculation
#    - Should calculate: (total_traffic_all_roads) / (total_hours_all_roads)
#    - Actually calculates: (total_traffic_so_far) / (hours_current_road * total_roads)
#
# 2. CRITICAL FAILURE - Second Function Complexity: Uses a convoluted approach:
#    - Creates parallel lists (road_list, traffic_list)
#    - Matches them using index positions (fragile)
#    - Multiple loops through same data
#    - Complex nested dictionary structures
#    - Should use simpler approach: track max with metadata during single iteration
#
# 3. PARTIAL SUCCESS - Third Function Logic: The aggregation logic using zip() is correct 
#    and clever, but the function doesn't return results, making it unusable.
#
# 4. DESIGN ISSUES: 
#    - Functions don't handle edge cases (empty data, missing keys)
#    - Overly complex data structures and access patterns
#    - Poor separation of concerns
#
# Functionality Test Results:
# - Function 1: ✗ Wrong average calculation algorithm
# - Function 2: ✗ Overly complex and fragile, may work but unreliable
# - Function 3: ✓ Correct aggregation logic but doesn't return results
#
# Example of Function 1 Error:
# Downtown has Main St (sum=4020) and 2nd Ave (sum=2520)
# Correct: (4020 + 2520) / (24 + 24) = 6540 / 48 = 136.25 average per hour
# Function: Calculates differently due to loop placement and overwrites
#
# Example of Function 2 Complexity:
# Could be solved simply by tracking max_count, max_hour, max_road_info during iteration
# Instead uses 8 variables and complex index matching
#
# Recommendations:
# 1. Fix first function: Calculate zone totals outside the road loop
# 2. Simplify second function: Use single iteration with max tracking
# 3. Make third function return results instead of printing
# 4. Add comprehensive error handling for missing keys
# 5. Simplify data access patterns and reduce complexity
# 6. Add proper docstrings and input validation
# 7. Eliminate redundant calculations and iterations
# 8. Use more descriptive variable names
# 9. Add unit tests to verify correctness
#
# The code shows understanding of the problem domain but needs significant simplification 
# and algorithmic fixes to work correctly and reliably.