import swisseph as swe
from datetime import datetime

# Constants
PLANETS = {
    swe.SUN: "Sun",
    swe.MOON: "Moon",
    swe.MERCURY: "Mercury",
    swe.VENUS: "Venus",
    swe.MARS: "Mars",
    swe.JUPITER: "Jupiter",
    swe.SATURN: "Saturn",
    swe.URANUS: "Uranus",
    swe.NEPTUNE: "Neptune",
    swe.PLUTO: "Pluto",
    swe.MEAN_NODE: "Rahu (North Node)",
    swe.TRUE_NODE: "Ketu (South Node)"
}

ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def calculate_kundli(birth_date, birth_time, latitude, longitude):
    """
    Calculate the Kundli (natal chart) based on birth details.

    :param birth_date: Date of birth (YYYY-MM-DD)
    :param birth_time: Time of birth (HH:MM in 24-hour format)
    :param latitude: Latitude of birth place (e.g., 19.0760 for Mumbai)
    :param longitude: Longitude of birth place (e.g., 72.8777 for Mumbai)
    :return: Kundli with planetary positions and zodiac signs
    """
    # Combine birth date and time
    birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")

    # Convert to Julian Day
    julian_day = swe.julday(
        birth_datetime.year,
        birth_datetime.month,
        birth_datetime.day,
        birth_datetime.hour + birth_datetime.minute / 60.0
    )

    kundli = {}
    for planet_id, planet_name in PLANETS.items():
        # Compute planetary position
        position, _ = swe.calc_ut(julian_day, planet_id)
        zodiac_index = int(position[0] // 30)  # Each zodiac covers 30 degrees
        degree_in_sign = position[0] % 30

        kundli[planet_name] = {
            "Zodiac Sign": ZODIAC_SIGNS[zodiac_index],
            "Degrees in Sign": round(degree_in_sign, 2),
            "Position in Ecliptic (Degrees)": round(position[0], 2),
        }

    # Ascendant (Lagna) Calculation
    ascendant = calculate_ascendant(julian_day, latitude, longitude)
    kundli["Ascendant (Lagna)"] = ascendant

    return kundli

def calculate_ascendant(julian_day, latitude, longitude):
    """
    Calculate the Ascendant (Lagna) based on birth details.

    :param julian_day: Julian Day for birth time
    :param latitude: Latitude of birth place
    :param longitude: Longitude of birth place
    :return: Ascendant zodiac sign and degrees
    """
    asc_position = swe.houses(julian_day, latitude, longitude, "P")[0][0]
    zodiac_index = int(asc_position // 30)
    degree_in_sign = asc_position % 30

    return {
        "Zodiac Sign": ZODIAC_SIGNS[zodiac_index],
        "Degrees in Sign": round(degree_in_sign, 2),
        "Position in Ecliptic (Degrees)": round(asc_position, 2),
    }

def display_kundli(kundli):
    """
    Display the generated Kundli in a readable format.

    :param kundli: Kundli dictionary with planetary positions
    """
    print("\n--- Kundli (Natal Chart) ---\n")
    for planet, details in kundli.items():
        print(f"{planet}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()

# Main Program
if __name__ == "__main__":
    print("Welcome to the Kundli Generator!")
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    birth_time = input("Enter your birth time (HH:MM in 24-hour format): ")
    latitude = float(input("Enter your birth latitude (e.g., 19.0760 for Mumbai): "))
    longitude = float(input("Enter your birth longitude (e.g., 72.8777 for Mumbai): "))

    kundli = calculate_kundli(birth_date, birth_time, latitude, longitude)
    display_kundli(kundli)
