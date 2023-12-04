-- Prepare dev database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on hbnb_dev_db for hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privileges on performance_schema for hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
