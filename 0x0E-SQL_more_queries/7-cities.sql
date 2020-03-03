-- creates database with table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select database
USE hbtn_0d_usa;
-- creates table with variable restrictions
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
state_id INT NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
