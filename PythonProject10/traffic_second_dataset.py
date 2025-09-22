# For each city, calculate the zone with the highest average traffic per hour.
# Identify the road (across all cities and zones) that saw the single highest vehicle count in any given hour, and output its city, zone, road name, and the hour.
# For each city, compute total vehicle counts per hour (aggregate all roads and zones) and list the hour with the highest and lowest total traffic.

from typing import Final
TOTAL_COUNT: Final[int] = 24

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
def zone_with_highest_traffic_avg(data: dict):
    total = {}
    result = {}

    try:
        for cities, zones in data.items():
            for zone, roads in zones.items():
                total_traffic = 0
                for road in roads:
                    if TOTAL_COUNT == len(road["hourly_counts"]):
                        total_traffic += sum(road["hourly_counts"])
                    elif TOTAL_COUNT > len(road["hourly_counts"]):
                        while TOTAL_COUNT > len(road["hourly_counts"]):
                            road["hourly_counts"].append(road["hourly_counts"][-1])
                        total_traffic += sum(road["hourly_counts"])
                    else:
                        while TOTAL_COUNT < len(road["hourly_counts"]):
                            road["hourly_counts"].remove(road["hourly_counts"][-1])
                        total_traffic += sum(road["hourly_counts"])
                avg = round(total_traffic / (TOTAL_COUNT * len(roads)), 2)
                if cities in total:
                    total[cities].update({zone: avg})
                else:
                    total[cities] = {zone: avg}

        for cities, zones in total.items():
            result.update({cities: max(total.get(cities).items())})
        for k, v in result.items():
            result.update({k: {v[0]: v[1]}})

    except KeyError as missing_key:
        return f"Key: {missing_key} not found."

    return result

# Identify the road (across all cities and zones) that saw the single highest vehicle count in any given hour, and output its city, zone, road name, and the hour.
def max_vehicle_count(data: dict):
    result = {}
    traffic_count = 0
    try:
        for cities, zones in data.items():
            for zone, roads in zones.items():
                for road in roads:
                    if filter(None, road["hourly_counts"]):
                        max_count = max(filter(None, road["hourly_counts"]))
                        if max_count > traffic_count:
                            traffic_count = max_count
                        if traffic_count == max_count:
                            result[cities] = {zone: [{road["road_name"]: max_count},
                                                     {"Hour": road["hourly_counts"].index(max_count)}]}
                    else:
                        return "Hourly count list is empty!!"
    except KeyError as missing_key:
        return f"Key: {missing_key} not found."
    return result

# For each city, compute total vehicle counts per hour (aggregate all roads and zones) and list the hour with the highest and lowest total traffic.
def total_vehicle_count(data: dict):
    result = {}
    try:
        for cities in data:
            vehicle_count = []
            my_list = []
            for zones in data[cities]:
                for roads in data[cities][zones]:
                    if TOTAL_COUNT == len(roads["hourly_counts"]):
                        vehicle_count.append(roads["hourly_counts"])
                    elif TOTAL_COUNT > len(roads["hourly_counts"]):
                        while TOTAL_COUNT > len(roads["hourly_counts"]):
                            roads["hourly_counts"].append(roads["hourly_counts"][-1])
                        vehicle_count.append(roads["hourly_counts"])
                    else:
                        while TOTAL_COUNT < len(roads["hourly_counts"]):
                            roads["hourly_counts"].remove(roads["hourly_counts"][-1])
                        vehicle_count.append(roads["hourly_counts"])

            for i in zip(*vehicle_count):
                my_list.append(sum(i))

            max_of_my_list = max(my_list)
            min_of_my_list = min(my_list)

            result[cities] = [[{"max vehicle count": max_of_my_list}, {"hour": my_list.index(max_of_my_list)}],
                              [{"min vehicle count": min_of_my_list}, {"hour": my_list.index(min_of_my_list)}]]

    except KeyError as missing_key:
        return f"Key: {missing_key} not found."

    return result

if __name__ == "__main__":
    print(zone_with_highest_traffic_avg(traffic_data))
    print(max_vehicle_count(traffic_data))
    print(total_vehicle_count(traffic_data))