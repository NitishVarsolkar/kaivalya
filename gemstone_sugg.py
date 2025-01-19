import swisseph as swe
from datetime import datetime

# Zodiac signs and corresponding ruling planets
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

# Additional gemstone recommendations based on concerns
CONCERN_GEMSTONES = {
    "career": ["Citrine", "Green Aventurine", "Tiger's Eye"],
    "health": ["Amethyst", "Malachite", "Bloodstone"],
    "relationships": ["Rose Quartz", "Moonstone", "Emerald"],
    "wealth": ["Pyrite", "Citrine", "Garnet"],
    "protection": ["Black Tourmaline", "Obsidian", "Tiger's Eye"],
}

def get_zodiac_sign(day, month):
    """
    Determine zodiac sign based on day and month of birth.
    """
    zodiac_dates = [
        ("Capricorn", (1, 19)), ("Aquarius", (2, 18)), ("Pisces", (3, 20)),
        ("Aries", (4, 19)), ("Taurus", (5, 20)), ("Gemini", (6, 20)),
        ("Cancer", (7, 22)), ("Leo", (8, 22)), ("Virgo", (9, 22)),
        ("Libra", (10, 22)), ("Scorpio", (11, 21)), ("Sagittarius", (12, 21)),
        ("Capricorn", (12, 31))
    ]
    for sign, (sign_month, sign_day) in zodiac_dates:
        if (month == sign_month and day <= sign_day) or (month == sign_month - 1 and day > sign_day):
            return sign
    return "Invalid Date"

def suggest_gemstone(zodiac_sign, concerns=None):
    """
    Suggest gemstones based on zodiac sign and specific concerns.
    """
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

def planetary_influence(julian_day):
    """
    Check planetary influence based on current positions.
    """
    influences = {}
    for planet_id, planet_name in PLANETS.items():
        position, _ = swe.calc_ut(julian_day, planet_id)
        zodiac_index = int(position[0] // 30)
        influences[planet_name] = ZODIAC_SIGNS[zodiac_index]
    return influences

def main():
    print("Welcome to the Gemstone Suggestor!")

    # Input birth details
    try:
        birth_day = int(input("Enter your birth day (1-31): "))
        birth_month = int(input("Enter your birth month (1-12): "))
        concerns = input(
            "Enter your concerns (comma-separated, e.g., career, health, relationships): "
        ).lower().split(",")
        concerns = [c.strip() for c in concerns]

        # Determine zodiac sign
        zodiac_sign = get_zodiac_sign(birth_day, birth_month)
        if zodiac_sign == "Invalid Date":
            print("The date entered is invalid. Please try again.")
            return

        # Suggest gemstones
        print("\n--- Gemstone Recommendations ---")
        print(suggest_gemstone(zodiac_sign, concerns))

        # Planetary influence
        include_influences = input("\nWould you like to see planetary influences? (yes/no): ").strip().lower()
        if include_influences == "yes":
            now = datetime.now()
            julian_day = swe.julday(now.year, now.month, now.day, now.hour + now.minute / 60.0)
            influences = planetary_influence(julian_day)
            print("\n--- Current Planetary Influences ---")
            for planet, zodiac in influences.items():
                print(f"{planet}: {zodiac}")

    except ValueError:
        print("Invalid input. Please ensure you enter numbers for dates and valid concerns.")

# Zodiac signs and planets
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
}

ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

if __name__ == "__main__":
    main()
