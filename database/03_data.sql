DROP TABLE IF EXISTS data;

CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices(id) ON DELETE CASCADE,
    collected_at TIMESTAMP,
    decibels INTEGER
);

ALTER TABLE datA
ALTER COLUMN collected_at SET DEFAULT now();