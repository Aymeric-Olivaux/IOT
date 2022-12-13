DROP TABLE IF EXISTS thresholds;

CREATE TABLE thresholds (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices(id) ON DELETE CASCADE,
    threshold INTEGER
);

INSERT INTO thresholds (device_id, threshold) VALUES (1, 50);