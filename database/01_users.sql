DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id serial PRIMARY KEY,
    email VARCHAR(256) UNIQUE,
    password VARCHAR(256)
);

INSERT INTO users (email, password) VALUES ('admin@localhost', 'admin');