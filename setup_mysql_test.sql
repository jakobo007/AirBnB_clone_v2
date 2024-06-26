-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user and set passwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant priviledges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant user select to performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Appply priviledges
FLUSH PRIVILEGES;
