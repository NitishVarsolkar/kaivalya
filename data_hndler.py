CREATE TABLE horoscope_predictions (
    zodiac_sign TEXT PRIMARY KEY,
    daily_prediction TEXT
);


CREATE TABLE kundli_data (
    user_id UUID PRIMARY KEY,
    birth_date DATE,
    birth_time TIME,
    latitude DOUBLE,
    longitude DOUBLE,
    kundli_details MAP<TEXT, TEXT>  -- Stores planets and their positions
);

CREATE TABLE gemstone_suggestions (
    zodiac_sign TEXT PRIMARY KEY,
    ruling_planet TEXT,
    gemstones LIST<TEXT>,
    concerns MAP<TEXT, LIST<TEXT>>  -- Concern type and suggested gemstones
);
