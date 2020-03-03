-- creates database with table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select database
USE hbtn_0d_usa;
-- creates table with variable restrictions
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
name VARCHAR(256) NOT NULL);