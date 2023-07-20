-- Create Database and Read New user
-- Create The Database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant user_0d_2 the select privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
