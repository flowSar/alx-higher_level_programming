-- create new database with table 

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
id INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256)
);
