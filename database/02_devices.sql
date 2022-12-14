DROP TABLE IF EXISTS devices;

CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO devices (owner_id) VALUES (1);