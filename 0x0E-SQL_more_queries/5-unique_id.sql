-- create a table and set default value (unique value) to it attribute

CREATE TABLE IF NOT EXISTS id_not_null(
id INT PRIMARY KEY AUTO_INCREMENT DEFAULT 1,
name VARCHAR(256)
);
