DROP TABLE IF EXISTS threshold;

CREATE TABLE threshold (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices(id) ON DELETE CASCADE,
    threshold INTEGER
);

INSERT INTO threshold (device_id, threshold) VALUES (1, 50);