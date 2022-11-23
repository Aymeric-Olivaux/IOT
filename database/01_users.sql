DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id serial PRIMARY KEY,
    firstname VARCHAR(256),
    lastname VARCHAR(256),
    email VARCHAR(256),
    password VARCHAR(256)
);