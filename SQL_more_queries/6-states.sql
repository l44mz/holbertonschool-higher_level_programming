-- Create the database hbtn_0d_usa and the table states within it
-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;
-- Create the table states with an auto-incrementing primary key id and a required name
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
