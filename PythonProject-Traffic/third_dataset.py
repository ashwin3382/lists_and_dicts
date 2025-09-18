import random



def random_hourly_counts(length=24, min_val=10, max_val=500, missing=0):
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
from collections import Counter
def zone_with_highest_traffic_avg(data: dict):
    total = {}
    result = {}
    for cities, zones in data.items():
        for zone, roads in zones.items():
            total_traffic = 0
            for road in roads:
                total_traffic += (sum(filter(None, road["hourly_counts"])))
                avg = round(total_traffic / ((len(road["hourly_counts"])-Counter(road["hourly_counts"])[None]) * len(roads)), 2)
                if cities in total:
                    total[cities].update({zone: avg})
                else:
                    total[cities] = ({zone: avg})

    for cities, zones in total.items():
        result.update({cities: max(total.get(cities).items())})
    return result

# Identify the road (across all cities and zones) that saw the single highest vehicle count in any given hour, and output its city, zone, road name, and the hour.
def max_vehicle_count(data: dict):
    result = {}
    traffic_count = 0

    for cities, zones in data.items():
        for zone, roads in zones.items():
            for road in roads:
                if max(filter(None,road["hourly_counts"]))> traffic_count:
                    traffic_count = max(filter(None,road["hourly_counts"]))
                if traffic_count == max(filter(None, road["hourly_counts"])):
                    result[cities] = {zone:{max(filter(None, road["hourly_counts"])): road["hourly_counts"].index(max(filter(None, road["hourly_counts"])))}}
    return result

# For each city, compute total vehicle counts per hour (aggregate all roads and zones) and list the hour with the highest and lowest total traffic.
def total_vehicle_count(data: dict):

    for cities in data:
        vehicle_count =  []
        my_list = []
        print(cities)
        for zones in data[cities]:
            for roads in data[cities][zones]:
                vehicle_count.append(filter(None,roads["hourly_counts"]))

        for i in zip(*vehicle_count):
            my_list.append(sum(i))

        print({"max vehicle count":max(my_list)} , {"hour": my_list.index(max(my_list))})
        print({"min vehicle count": min(my_list)}, {"hour": my_list.index(min(my_list))})



