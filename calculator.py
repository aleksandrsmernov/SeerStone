def calculate_measurement(result):
    rtt = result["avg_rtt"]
    packet_loss = result["packet_loss"]
    hop_count = result["hop_count"]

    measurement = (
        rtt
        + packet_loss * 5
        + hop_count * 2
    )

    return measurement


def find_closest_probes(results, count=3):

    for result in results:
        result["measurement"] = calculate_measurement(result)

    sorted_results = sorted(
        results,
        key=lambda x: x["measurement"]
    )

    return sorted_results[:count]