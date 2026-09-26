from config import LOCATIONS

from globalping.client import create_measurement, wait_for_result
from globalping.parser import parse_ping, parse_traceroute

from calculator import find_closest_probes


def measure_target(target, location):

    city = location["city"]
    country = location["country"]

    print()
    print("=" * 50)
    print(f"Measuring from {city}, {country}")
    print("=" * 50)

    # PING

    print("Starting ping...")

    ping_id = create_measurement(
        target,
        city,
        country,
        measurement_type="ping"
    )

    ping_data = wait_for_result(ping_id)
    ping_result = parse_ping(ping_data)

    print(
        f"Ping: "
        f"{ping_result['avg_rtt']} ms, "
        f"loss {ping_result['packet_loss']}%"
    )

    # TRACEROUTE

    print("Starting traceroute...")

    traceroute_id = create_measurement(
        target,
        city,
        country,
        measurement_type="traceroute"
    )

    traceroute_data = wait_for_result(traceroute_id)
    traceroute_result = parse_traceroute(traceroute_data)

    print(
        f"Traceroute: "
        f"{traceroute_result['hop_count']} hops"
    )

    return {
        "city": city,
        "country": country,
        "latitude": ping_result["latitude"],
        "longitude": ping_result["longitude"],

        "avg_rtt": ping_result["avg_rtt"],
        "min_rtt": ping_result["min_rtt"],
        "max_rtt": ping_result["max_rtt"],
        "packet_loss": ping_result["packet_loss"],

        "hop_count": traceroute_result["hop_count"]
    }


def locate(target):

    results = []

    for location in LOCATIONS:

        result = measure_target(
            target,
            location
        )

        results.append(result)

    closest = find_closest_probes(
        results,
        3
    )

    return closest