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

ZODIAC_RULERS = {
    "Aries": {"Planet": "Mars", "Gemstones": ["Red Coral", "Carnelian"]},
    "Taurus": {"Planet": "Venus", "Gemstones": ["Emerald", "Diamond"]},
    "Gemini": {"Planet": "Mercury", "Gemstones": ["Emerald", "Peridot"]},
    "Cancer": {"Planet": "Moon", "Gemstones": ["Pearl", "Moonstone"]},
    "Leo": {"Planet": "Sun", "Gemstones": ["Ruby", "Garnet"]},
    "Virgo": {"Planet": "Mercury", "Gemstones": ["Emerald", "Peridot"]},
    "Libra": {"Planet": "Venus", "Gemstones": ["Diamond", "Opal"]},
    "Scorpio": {"Planet": "Mars", "Gemstones": ["Red Coral", "Carnelian"]},
    "Sagittarius": {"Planet": "Jupiter", "Gemstones": ["Yellow Sapphire", "Citrine"]},
    "Capricorn": {"Planet": "Saturn", "Gemstones": ["Blue Sapphire", "Amethyst"]},
    "Aquarius": {"Planet": "Saturn", "Gemstones": ["Blue Sapphire", "Amethyst"]},
    "Pisces": {"Planet": "Jupiter", "Gemstones": ["Yellow Sapphire", "Aquamarine"]},
}

CONCERN_GEMSTONES = {
    "career": ["Citrine", "Green Aventurine", "Tiger's Eye"],
    "health": ["Amethyst", "Malachite", "Bloodstone"],
    "relationships": ["Rose Quartz", "Moonstone", "Emerald"],
    "wealth": ["Pyrite", "Citrine", "Garnet"],
    "protection": ["Black Tourmaline", "Obsidian", "Tiger's Eye"],
}

def horoscope_prediction(zodiac_sign):
    # Simplified horoscope prediction
    horoscopes = {
        "Aries": "Focus on new beginnings today.",
        "Taurus": "Embrace stability and persistence.",
        # Add predictions for all zodiac signs...
    }
    return horoscopes.get(zodiac_sign, "Horoscope not available.")

def calculate_kundli(birth_date, birth_time, latitude, longitude):
    birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    julian_day = swe.julday(
        birth_datetime.year,
        birth_datetime.month,
        birth_datetime.day,
        birth_datetime.hour + birth_datetime.minute / 60.0
    )
    kundli = {}
    for planet_id, planet_name in PLANETS.items():
        position, _ = swe.calc_ut(julian_day, planet_id)
        zodiac_index = int(position[0] // 30)
        degree_in_sign = position[0] % 30
        kundli[planet_name] = {
            "Zodiac Sign": ZODIAC_SIGNS[zodiac_index],
            "Degrees in Sign": round(degree_in_sign, 2),
            "Position in Ecliptic (Degrees)": round(position[0], 2),
        }
    return kundli

def suggest_gemstone(zodiac_sign, concerns=None):
    if zodiac_sign not in ZODIAC_RULERS:
        return f"Invalid zodiac sign: {zodiac_sign}"

    ruling_planet = ZODIAC_RULERS[zodiac_sign]["Planet"]
    gemstones = ZODIAC_RULERS[zodiac_sign]["Gemstones"]

    suggestions = f"Zodiac Sign: {zodiac_sign}\n"
    suggestions += f"Ruling Planet: {ruling_planet}\n"
    suggestions += f"Recommended Gemstones: {', '.join(gemstones)}\n"

    if concerns:
        suggestions += "\nBased on your concerns:\n"
        for concern in concerns:
            if concern in CONCERN_GEMSTONES:
                suggestions += f"- {concern.capitalize()}: {', '.join(CONCERN_GEMSTONES[concern])}\n"
            else:
                suggestions += f"- {concern.capitalize()}: No specific recommendation found.\n"

    return suggestions

def main():
    while True:
        print("\n--- Welcome to the Astrology Suite ---")
        print("1. Horoscope Prediction")
        print("2. Kundli Generation")
        print("3. Gemstone Suggestion")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            zodiac_sign = input("Enter your zodiac sign (e.g., Aries, Taurus): ")
            print("\n--- Horoscope Prediction ---")
            print(horoscope_prediction(zodiac_sign))
        elif choice == "2":
            birth_date = input("Enter your birth date (YYYY-MM-DD): ")
            birth_time = input("Enter your birth time (HH:MM in 24-hour format): ")
            latitude = float(input("Enter your birth latitude: "))
            longitude = float(input("Enter your birth longitude: "))
            kundli = calculate_kundli(birth_date, birth_time, latitude, longitude)
            print("\n--- Kundli (Natal Chart) ---")
            for planet, details in kundli.items():
                print(f"{planet}: {details}")
        elif choice == "3":
            birth_day = int(input("Enter your birth day (1-31): "))
            birth_month = int(input("Enter your birth month (1-12): "))
            concerns = input(
                "Enter your concerns (comma-separated, e.g., career, health): ").lower().split(",")
            zodiac_sign = get_zodiac_sign(birth_day, birth_month)
            print("\n--- Gemstone Suggestion ---")
            print(suggest_gemstone(zodiac_sign, concerns))
        elif choice == "4":
            print("Thank you for using the Astrology Suite!")
            break
        else:
            print("Invalid choice. Please try again.")

def get_zodiac_sign(day, month):
    zodiac_dates = [
        ("Capricorn", (1, 19)), ("Aquarius", (2, 18)), ("Pisces", (3, 20)),
        ("Aries", (4, 19)), ("Taurus", (5, 20)), ("Gemini", (6, 20)),
        ("Cancer", (7, 22)), ("Leo", (8, 22)), ("Virgo", (9, 22)),
        ("Libra", (10, 22)), ("Scorpio", (11, 21)), ("Sagittarius", (12, 21)),
        ("Capricorn", (12, 31))
    ]
    for sign, (end_month, end_day) in zodiac_dates:
        if (month == end_month and day <= end_day) or (month == end_month - 1 and day > end_day):
            return sign
    return "Invalid Date"

if __name__ == "__main__":
    main()
