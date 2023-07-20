-- Create a MySQL Server user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant User all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
