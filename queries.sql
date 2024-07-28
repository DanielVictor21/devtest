CREATE TABLE elevator_calls (
    id INTEGER PRIMARY KEY,
    floor_called INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE elevator_status (
    id INTEGER PRIMARY KEY,
    current_floor INTEGER,
    is_vacant BOOLEAN,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);