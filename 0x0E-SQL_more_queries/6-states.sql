-- Creates a database called 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Enter into the database
USE hbtn_0d_usa;
-- Create a table called states
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
