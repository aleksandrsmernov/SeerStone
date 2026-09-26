import argparse

from config import LOCATIONS
from locate import locate


def main():

    parser = argparse.ArgumentParser(
        description="Seerstone - Network Geolocation & Triangulation Tool"
    )

    parser.add_argument(
        "target",
        help="Target IP address"
    )

    args = parser.parse_args()

    print()
    print("========================================")
    print("             SEERSTONE")
    print("========================================")
    print()

    print(f"Target: {args.target}")
    print(f"Probes: {len(LOCATIONS)}")

    print()
    print("Starting measurements...")

    closest = locate(args.target)

    print()
    print("========================================")
    print("             TOP 3 PROBES")
    print("========================================")

    for number, result in enumerate(closest, start=1):

        print(
            f"{number}. "
            f"{result['city']}, {result['country']} "
            f"→ measurement = {result['measurement']:.2f}"
        )

    print()
    print("Coordinates:")

    for result in closest:

        print(
            f"{result['city']}: "
            f"{result['latitude']}, "
            f"{result['longitude']}"
        )


if __name__ == "__main__":
    main()