-- create a table and set default value (unique value) to it attribute

CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256)
);
