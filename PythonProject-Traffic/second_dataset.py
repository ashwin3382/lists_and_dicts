
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
    for cities, zones in data.items():
        for zone, roads in zones.items():
            total_traffic = 0
            for road in roads:
                total_traffic += (sum(road["hourly_counts"]))
                avg = round(total_traffic / (len(road["hourly_counts"]) * len(roads)), 2)
                if cities in total:
                    total[cities].update({zone: avg})
                else:
                    total[cities] = ({zone: avg})

    for cities, zones in total.items():
        result.update({cities: max(total.get(cities).items())})
    return result



# Identify the road (across all cities and zones) that saw the single highest vehicle count in any given hour, and output its city, zone, road name, and the hour.
def max_vehicle_count(data: dict):
    road_list = []
    traffic_at_specific_hour = {}
    road_dict = {}
    traffic_list = []
    max_traffic_with_zone = {}
    result = {}
    max_traffic_dict = {}
    for cities in data:
        for zones in data[cities]:
            for roads in data[cities][zones]:
                road_list.append(roads["road_name"])
                for traffic in roads:
                    if isinstance(roads[traffic], list):
                        traffic_list.append(max(roads[traffic]))
                        traffic_at_specific_hour[max(roads[traffic])] = {"Hour": roads[traffic].index(max(roads[traffic]))}

    for road in road_list:
        for k, v in traffic_at_specific_hour.items():
            if road_list.index(road) == traffic_list.index(k):
                road_dict[road] = [{"Vehicle count": k},v]

    for k, v in road_dict.items():
        if (max(v[0].values())) == max(traffic_list):
            max_traffic_dict[k] = v
    for cities in data:
        for zones in data[cities]:
            for roads in data[cities][zones]:
                for k, v in max_traffic_dict.items():
                    if k == roads["road_name"]:
                        max_traffic_with_zone[zones] = [{"Road name":k},v]
                        result[cities] = max_traffic_with_zone

    return result


# For each city, compute total vehicle counts per hour (aggregate all roads and zones) and list the hour with the highest and lowest total traffic.
def total_vehicle_count(data: dict):

    for cities in data:
        vehicle_count =  []
        my_list = []
        print(cities)
        for zones in data[cities]:
            for roads in data[cities][zones]:
                vehicle_count.append((roads["hourly_counts"]))

        for i in zip(*vehicle_count):
            my_list.append(sum(i))

        print({"max vehicle count":max(my_list)} , {"hour": my_list.index(max(my_list))})
        print({"min vehicle count": min(my_list)}, {"hour": my_list.index(min(my_list))})
