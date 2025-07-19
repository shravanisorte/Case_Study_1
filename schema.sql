-- Table 1: Vehicles
CREATE TABLE vehicles (
    vehicle_id TEXT PRIMARY KEY,
    plate_number TEXT NOT NULL,
    type TEXT,
    owner_name TEXT
);

-- Table 2: Parking Zones
CREATE TABLE parking_zones (
    zone_id TEXT PRIMARY KEY,
    zone_name TEXT NOT NULL,
    rate_per_hour REAL CHECK (rate_per_hour >= 0),
    is_valet BOOLEAN NOT NULL
);

-- Table 3: Parking Events
CREATE TABLE parking_events (
    event_id INTEGER PRIMARY KEY,
    vehicle_id TEXT NOT NULL,
    zone_id TEXT NOT NULL,
    entry_time TIMESTAMP NOT NULL,
    exit_time TIMESTAMP NOT NULL,
    paid_amount REAL CHECK (paid_amount >= 0),

    -- Foreign key references
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (zone_id) REFERENCES parking_zones(zone_id),

    -- Logical data check
    CHECK (exit_time >= entry_time)
);
