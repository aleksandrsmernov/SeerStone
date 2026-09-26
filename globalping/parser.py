def parse_ping(data):
    result = data["results"][0]

    probe = result["probe"]
    stats = result["result"]["stats"]

    return {
        "city": probe["city"],
        "country": probe["country"],
        "latitude": probe["latitude"],
        "longitude": probe["longitude"],
        "avg_rtt": stats["avg"],
        "min_rtt": stats["min"],
        "max_rtt": stats["max"],
        "packet_loss": stats["loss"]
    }


def parse_traceroute(data):
    result = data["results"][0]

    traceroute = result["result"]
    hops = traceroute["hops"]

    responding_hops = [
        hop for hop in hops
        if hop["resolvedAddress"] is not None
    ]

    return {
        "hop_count": len(responding_hops),
        "hops": hops
    }