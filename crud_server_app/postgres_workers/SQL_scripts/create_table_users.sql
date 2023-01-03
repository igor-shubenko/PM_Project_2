CREATE TABLE IF NOT EXISTS Users (
    id serial PRIMARY KEY,
    name text,
    last_name text,
    time_created int,
    balance real,
    gender text,
    age int,
    city text,
    birth_day text,
    premium bool,
    ip text
    );