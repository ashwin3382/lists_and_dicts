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

import random

def random_hourly_counts(length=24, min_val=10, max_val=500, missing=0):  # PRACTICE: Good helper function for generating test data
    counts = [random.randint(min_val, max_val) for _ in range(length)]
    for _ in range(missing):
        idx = random.randint(0, length-1)
        counts[idx] = None
    return counts

traffic_data = {
    "Metropolis": {
        "Downtown": [
            {
                "road_name": "Main St",
                "hourly_counts": random_hourly_counts(24, 100, 300, missing=2),
                "road_length_km": 3.2,
                "surface": "asphalt",
                "cameras": [{"id": 101, "status": "active"}, {"id": 102, "status": "inactive"}]
            },
            {
                "road_name": "2nd Ave",
                "hourly_counts": random_hourly_counts(24, 80, 200, missing=1),
                "road_length_km": 2.1,
                "surface": "concrete",
                "cameras": [{"id": 103, "status": "active"}]
            }
        ],
        "Uptown": [
            {
                "road_name": "Broadway",
                "hourly_counts": random_hourly_counts(24, 200, 430, missing=3),
                "road_length_km": 5.0,
                "surface": "asphalt",
                "cameras": []
            },
            {
                "road_name": "5th St",
                "hourly_counts": random_hourly_counts(24, 100, 330, missing=0),
                "road_length_km": 2.5,
                "surface": "asphalt",
                "cameras": [{"id": 104, "status": "active"}]
            }
        ],
        "Suburbs": [
            {
                "road_name": "Pine St",
                "hourly_counts": random_hourly_counts(24, 10, 105, missing=4),
                "road_length_km": 8.0,
                "surface": "gravel",
                "cameras": []
            }
        ]
    },
    "Gotham": {
        "Central": [
            {
                "road_name": "Gotham Blvd",
                "hourly_counts": random_hourly_counts(24, 95, 320, missing=2),
                "road_length_km": 4.4,
                "surface": "asphalt",
                "cameras": [{"id": 201, "status": "active"}]
            },
            {
                "road_name": "Arkham Rd",
                "hourly_counts": random_hourly_counts(24, 60, 260, missing=1),
                "road_length_km": 6.2,
                "surface": "concrete",
                "cameras": []
            }
        ],
        "Westside": [
            {
                "road_name": "Wayne Ave",
                "hourly_counts": random_hourly_counts(24, 150, 380, missing=2),
                "road_length_km": 3.8,
                "surface": "asphalt",
                "cameras": [{"id": 202, "status": "inactive"}]
            }
        ]
    },
    "Star City": {
        "Old Town": [
            {
                "road_name": "Queen St",
                "hourly_counts": random_hourly_counts(24, 50, 280, missing=3),
                "road_length_km": 7.0,
                "surface": "cobblestone",
                "cameras": [{"id": 301, "status": "active"}]
            }
        ],
        "New District": [
            {
                "road_name": "Arrow Ave",
                "hourly_counts": random_hourly_counts(24, 100, 400, missing=5),
                "road_length_km": 4.2,
                "surface": "asphalt",
                "cameras": [{"id": 302, "status": "active"}, {"id": 303, "status": "active"}]
            }
        ]
    }
}
# For each city, calculate the zone with the highest average traffic per hour.
from collections import Counter  # PRACTICE: Import should be at top of file
def zone_with_highest_traffic_avg(data: dict):  # PRACTICE: Missing docstring and input validation
    total = {}
    result = {}
    for cities, zones in data.items():
        for zone, roads in zones.items():
            total_traffic = 0
            for road in roads:  # CRITICAL: KeyError if roads list is empty or malformed
                total_traffic += (sum(filter(None, road["hourly_counts"])))  # PRACTICE: Good improvement - filters out None values, CRITICAL: KeyError if "hourly_counts" key missing
                avg = round(total_traffic / ((len(road["hourly_counts"])-Counter(road["hourly_counts"])[None]) * len(roads)), 2)  # CRITICAL: STILL wrong calculation - calculates average inside loop, overwrites previous calculations, CRITICAL: Counter()[None] can be 0, making denominator inconsistent
                if cities in total:
                    total[cities].update({zone: avg})
                else:
                    total[cities] = ({zone: avg})  # PRACTICE: Unnecessary parentheses

    for cities, zones in total.items():
        result.update({cities: max(total.get(cities).items())})  # CRITICAL: max() on dict items returns tuple, not expected format
    return result

# Identify the road (across all cities and zones) that saw the single highest vehicle count in any given hour, and output its city, zone, road name, and the hour.
def max_vehicle_count(data: dict):  # PRACTICE: Missing docstring, PRACTICE: Improved logic - simpler approach
    result = {}
    traffic_count = 0

    for cities, zones in data.items():
        for zone, roads in zones.items():
            for road in roads:  # CRITICAL: KeyError if roads list is empty or malformed
                if max(filter(None,road["hourly_counts"]))> traffic_count:  # CRITICAL: KeyError if "hourly_counts" missing, CRITICAL: filter() returns empty if all None - max() will crash
                    traffic_count = max(filter(None,road["hourly_counts"]))  # CRITICAL: Duplicate max() calculation
                if traffic_count == max(filter(None, road["hourly_counts"])):  # CRITICAL: Triple max() calculation, inefficient
                    result[cities] = {zone:{max(filter(None, road["hourly_counts"])): road["hourly_counts"].index(max(filter(None, road["hourly_counts"])))}}  # CRITICAL: Quadruple max() calculation, CRITICAL: index() will find first occurrence of filtered max, not original max position
    return result

# For each city, compute total vehicle counts per hour (aggregate all roads and zones) and list the hour with the highest and lowest total traffic.
def total_vehicle_count(data: dict):  # PRACTICE: Missing docstring, doesn't return anything

    for cities in data:
        vehicle_count =  []  # PRACTICE: Extra space before =
        my_list = []
        print(cities)  # PRACTICE: Should return data instead of printing
        for zones in data[cities]:
            for roads in data[cities][zones]:  # CRITICAL: KeyError if zones or roads keys missing
                vehicle_count.append(filter(None,roads["hourly_counts"]))  # CRITICAL: KeyError if "hourly_counts" missing, CRITICAL: filter() returns iterator, not list - zip() won't work properly

        for i in zip(*vehicle_count):  # CRITICAL: zip() with filter iterators of different lengths will truncate to shortest, giving wrong results
            my_list.append(sum(i))

        print({"max vehicle count":max(my_list)} , {"hour": my_list.index(max(my_list))})  # PRACTICE: Should return, not print, CRITICAL: max() called twice
        print({"min vehicle count": min(my_list)}, {"hour": my_list.index(min(my_list))})  # PRACTICE: Should return, not print, CRITICAL: min() called twice


# ------ Grading Report ------
# Grade: 3.0 / 10

# Critical Issues:
# 1. ALGORITHM ERROR in first function: STILL has the same fundamental calculation error 
#    from previous 5 iterations - calculates average inside the road loop, overwriting results.
#    Despite adding None handling, the core mathematical error persists.
# 2. FILTER ITERATOR BUG in third function: filter(None, list) returns an iterator, not a list. 
#    When used with zip(*vehicle_count), it creates unpredictable behavior because iterators 
#    are consumed and can't be reused.
# 3. INDEX MISMATCH in second function: After filtering None values with filter(), using 
#    index() on the original list will return wrong hour positions.
# 4. EMPTY FILTER CRASH: If all hourly_counts are None, max(filter(None, list)) will crash 
#    with "max() arg is an empty sequence" error.
# 5. MASSIVE INEFFICIENCY: Second function calls max(filter()) up to 4 times per road, 
#    creating O(n⁴) complexity in worst case.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. No input validation or type checking.
# 3. Import statement in middle of file instead of at top.
# 4. Poor variable naming and code organization.
# 5. Unnecessary parentheses and formatting issues.
# 6. Functions print instead of return (third function).
# 7. Code duplication (multiple max()/min() calls).

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. IMPROVEMENT: Attempts to handle None values with filter(None, ...).
# 3. IMPROVEMENT: Second function uses simpler logic than previous complex index matching.
# 4. Good helper function for generating test data with missing values.
# 5. Data structure expanded with realistic fields (surface, cameras).
# 6. Recognizes the need to handle missing data.

# Detailed Analysis:
# This is the SIXTH iteration showing some recognition of data quality issues but 
# introduces new critical bugs while maintaining old ones:
#
# 1. IMPROVEMENT ATTEMPT - None Value Handling: Shows awareness that missing data (None) 
#    needs to be handled. Uses filter(None, ...) to remove None values before calculations.
#
# 2. CRITICAL FAILURE - Iterator vs List Confusion: filter() returns an iterator, not a list.
#    In the third function:
#    ```python
#    vehicle_count.append(filter(None, roads["hourly_counts"]))  # Appends iterator
#    for i in zip(*vehicle_count):  # Zip with iterators - unpredictable
#    ```
#    This causes wrong aggregation results.
#
# 3. CRITICAL FAILURE - Index Position Bug: In second function, after filtering None values,
#    using index() on the original list gives wrong hour positions:
#    ```python
#    max_val = max(filter(None, [100, None, 200, 150]))  # Returns 200
#    original_list.index(200)  # Returns position in original list with None values
#    ```
#
# 4. PERSISTENT ALGORITHM ERROR: First function STILL has the same calculation error 
#    from 5 previous iterations despite adding None handling complexity.
#
# 5. PERFORMANCE REGRESSION: Second function now has O(n⁴) complexity due to repeated 
#    max(filter()) calls, making it slower than previous versions.
#
# Functionality Test Results:
# - Function 1: ✗ Wrong algorithm, Counter complexity adds confusion
# - Function 2: ✗ Multiple max() calls, wrong hour indexing
# - Function 3: ✗ Iterator/list confusion causes wrong aggregation
#
# Example of Iterator Bug in Function 3:
# ```python
# list1 = [100, None, 200]  # After filter: [100, 200]
# list2 = [150, 300, None]  # After filter: [150, 300]
# # zip(*[filter1, filter2]) may not align properly with original positions
# ```
#
# Pattern Analysis:
# This represents a concerning pattern across 6 iterations:
# - Shows awareness of new problems (missing data)
# - Attempts solutions but introduces new bugs
# - Core algorithmic errors remain unchanged
# - Complexity increases without improving correctness
# - No systematic testing to catch regressions
#
# Recommendations:
# 1. URGENT: Convert filter() results to lists: list(filter(None, data))
# 2. Fix index position tracking after filtering
# 3. Store max() calculation results instead of recalculating
# 4. Fix first function's fundamental calculation error (6th iteration!)
# 5. Add proper error handling for empty filtered lists
# 6. Make third function return results instead of printing
# 7. Add comprehensive unit tests to prevent regressions
# 8. Focus on getting basic algorithms right before handling edge cases
# 9. Use debugging/testing to verify each change works correctly
#
# This code shows some progress in recognizing real-world data issues but introduces 
# critical bugs while failing to fix fundamental algorithmic errors. The pattern suggests 
# a need for more systematic development and testing practices.