-- create a table and set default value (unique value) to it attribute

CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
