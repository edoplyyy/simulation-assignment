import math

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculates the great-circle distance between two GPS coordinates (in decimal degrees)
    using the Haversine formula.
    
    Returns:
        Distance in meters.
    """
    # 1. Earth's mean radius in meters
    EARTH_RADIUS = 6371000.0

    # 2. Convert degrees to radians (Python math functions expect radians)
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # 3. Haversine formula (finding ratio 'a')
    a = (math.sin(delta_phi / 2.0) ** 2 +
         math.cos(phi1) * math.cos(phi2) * (math.sin(delta_lambda / 2.0) ** 2))

    # 4. Central angle 'c' in radians (using atan2 for numerical stability)
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    # 5. Distance = Radius * central angle
    distance_in_meters = EARTH_RADIUS * c
    return distance_in_meters


def main():
    print("=" * 60)
    print("  Autonomous Boat Simulation: GPS Distance Calculator")
    print("=" * 60)
    print("Enter the coordinates below (press Enter with no input to use default test points).\n")

    try:
        # Prompt user for Point 1
        print("📍 Point 1 (e.g. Boat current position):")
        in_lat1 = input("   Latitude  [default: 41.0256]: ").strip()
        lat1 = float(in_lat1) if in_lat1 else 41.0256

        in_lon1 = input("   Longitude [default: 28.9741]: ").strip()
        lon1 = float(in_lon1) if in_lon1 else 28.9741

        # Prompt user for Point 2
        print("\n🎯 Point 2 (e.g. Target waypoint / buoy):")
        in_lat2 = input("   Latitude  [default: 41.0211]: ").strip()
        lat2 = float(in_lat2) if in_lat2 else 41.0211

        in_lon2 = input("   Longitude [default: 29.0041]: ").strip()
        lon2 = float(in_lon2) if in_lon2 else 29.0041

    except ValueError:
        print("\n❌ Error: Please enter valid decimal numbers for coordinates!")
        return

    # Calculate distance
    dist_m = haversine_distance(lat1, lon1, lat2, lon2)
    dist_km = dist_m / 1000.0

    print("-" * 60)
    print(f"Distance between points: {dist_m:.2f} meters ({dist_km:.3f} km)")
    print("=" * 60)


if __name__ == "__main__":
    main()
