-- create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--create the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

--grant priviledges
GRANT ALL PRIVILEDGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--grant user SELECT priviledge on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

--apply priviledges
FLUSH PRIVILEDGES;