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
            {
                "road_name": "Main St",
                "hourly_counts": [120, 150, 130, 140, 160, 170, 180, 200, 220, 210, 190, 170, 160, 150, 140, 145, 155, 165, 175, 185, 195, 205, 215], # 23 values, 1 hour missing
                "road_length_km": 3.2
            },
            {
                "road_name": "2nd Ave",
                "hourly_counts": [80, 90, 85, 100, 110, 120, 130, 140, 150, 160, 155, 145, 135, 125, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70],
                "road_length_km": 2.1
            }
        ],
        "Uptown": [
            {
                "road_name": "Broadway",
                "hourly_counts": [200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430],
                "road_length_km": 5.0
            },
            {
                "road_name": "5th St",
                "hourly_counts": [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330],
                "road_length_km": 2.5
            }
        ],
        "Suburbs": [
            {
                "road_name": "Pine St",
                "hourly_counts": [35, 40, 33, 30, 28, 20, 18, 22, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
                "road_length_km": 8.0
            }
        ]
    },
    "Gotham": {
        "Central": [
            {
                "road_name": "Gotham Blvd",
                "hourly_counts": [95, 105, 115, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320],
                "road_length_km": 4.4
            },
            {
                "road_name": "Arkham Rd",
                "hourly_counts": [60, 65, 70, 75, 80, 85, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
                "road_length_km": 6.2
            }
        ],
        "Westside": [
            {
                "road_name": "Wayne Ave",
                "hourly_counts": [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380],
                "road_length_km": 3.8
            }
        ]
    },
    "Star City": {
        "Old Town": [
            {
                "road_name": "Queen St",
                "hourly_counts": [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280],
                "road_length_km": 7.0
            }
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
                avg = round(total_traffic / (len(road["hourly_counts"]) * len(roads)), 2)  # CRITICAL: STILL wrong calculation - calculates average inside loop, overwrites previous calculations, CRITICAL: Different road lengths cause wrong average (Main St has 23 hours, 2nd Ave has 24)
                if cities in total:
                    total[cities].update({zone: avg})
                else:
                    total[cities] = ({zone: avg})  # PRACTICE: Unnecessary parentheses

    for cities, zones in total.items():
        result.update({cities: max(total.get(cities).items())})  # CRITICAL: max() on dict items returns tuple, not expected format
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
            if road_list.index(road) == traffic_list.index(k):  # CRITICAL: index() can raise ValueError if item not found, CRITICAL: Breaks if duplicate max values exist
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

        for i in zip(*vehicle_count):  # PRACTICE: Good use of zip for aggregation, CRITICAL: Will crash due to mismatched list lengths (Main St has 23 values, others have 24)
            my_list.append(sum(i))

        print({"max vehicle count":max(my_list)} , {"hour": my_list.index(max(my_list))})  # PRACTICE: Should return, not print, CRITICAL: max() called twice
        print({"min vehicle count": min(my_list)}, {"hour": my_list.index(min(my_list))})  # PRACTICE: Should return, not print, CRITICAL: min() called twice


# ------ Grading Report ------
# Grade: 2.5 / 10

# Critical Issues:
# 1. CRASH BUG in third function: Main St has 23 hourly values while all other roads have 24. 
#    The zip(*vehicle_count) will fail with "zip argument of unequal length" error when 
#    trying to aggregate mismatched lists. This makes the function completely non-functional.
# 2. ALGORITHM ERROR in first function: Still has the same fundamental calculation error 
#    from previous iterations - calculates average inside the road loop, overwriting results.
# 3. COMPLEX AND FRAGILE LOGIC in second function: Uses index matching that will break 
#    if duplicate maximum values exist across different roads.
# 4. NO ERROR HANDLING: All functions will crash with various errors (KeyError, ValueError, 
#    zip length mismatch) if data is imperfect.
# 5. PERSISTENT ALGORITHMIC FLAWS: Same core errors remain unchanged despite multiple iterations.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. No input validation or type checking.
# 3. Poor variable naming and code organization.
# 4. Unnecessary parentheses and formatting issues.
# 5. Code duplication (multiple max()/min() calls).
# 6. Functions print instead of return (third function).
# 7. Inefficient algorithms with redundant iterations.

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. Good use of zip() concept for aggregation (when data is consistent).
# 3. Proper use of dictionary comprehensions and updates.
# 4. Round() function used for decimal precision.
# 5. Data structure correctly expanded with road lengths.

# Detailed Analysis:
# This version introduces a critical data inconsistency that exposes the fragility of the code:
#
# 1. CRITICAL FAILURE - Data Inconsistency Handling: Main St has only 23 hourly values 
#    instead of 24. This causes the third function to crash completely with:
#    "ValueError: zip argument 1 is longer than argument 0"
#    
#    Real-world data often has missing values, and robust code should handle this gracefully.
#
# 2. CRITICAL FAILURE - Algorithm Persistence: Despite this being the FIFTH iteration of 
#    similar code, the first function STILL has the same calculation error:
#    - Should calculate: (sum_all_roads_in_zone) / (total_valid_hours_in_zone)
#    - Actually calculates: (cumulative_sum) / (current_road_hours * total_roads)
#    - This gets worse with inconsistent hour counts
#
# 3. CRITICAL FAILURE - Index Matching Fragility: The second function's index-based 
#    matching will break if two roads have the same maximum traffic value, causing 
#    incorrect matches between road_list and traffic_list.
#
# 4. NO LEARNING DEMONSTRATED: The code shows no improvement in core algorithmic 
#    understanding despite multiple iterations and feedback.
#
# Functionality Test Results:
# - Function 1: ✗ Wrong algorithm, made worse by inconsistent data
# - Function 2: ✗ Fragile logic, may break with duplicate values
# - Function 3: ✗ CRASHES due to mismatched list lengths
#
# Example of Crash in Function 3:
# ```
# Main St: [120, 150, ..., 215] (23 values)
# 2nd Ave: [80, 90, ..., 70] (24 values)
# zip(*[main_st_list, second_ave_list]) → ValueError
# ```
#
# Data Quality Issues:
# The introduced data inconsistency (23 vs 24 hours) represents a common real-world 
# scenario where data might be incomplete. Production code must handle such cases.
#
# Recommendations:
# 1. URGENT: Add data validation to handle missing/inconsistent hourly data
# 2. Fix first function algorithm to properly calculate zone averages
# 3. Simplify second function to avoid fragile index matching
# 4. Make third function return results and handle variable-length data
# 5. Add comprehensive error handling for real-world data imperfections
# 6. Add data validation before processing
# 7. Use padding or interpolation for missing data points
# 8. Add unit tests with edge cases (missing data, empty lists, etc.)
# 9. Focus on algorithmic correctness before handling complex datasets
#
# This code represents a significant regression due to the crash bug and demonstrates 
# the importance of robust error handling and data validation in real-world applications.
# The persistence of the same algorithmic errors across multiple iterations indicates 
# a fundamental gap in understanding that needs to be addressed.