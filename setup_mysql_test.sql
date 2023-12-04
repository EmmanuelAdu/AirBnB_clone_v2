-- Prepare test database
-- Database name hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create User
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on hbnb_test_db for hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privileges on performance_schema for hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
