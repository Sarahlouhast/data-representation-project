-- Create a new database
CREATE DATABASE IF NOT EXISTS prod_data;
USE prod_data;

-- Create the 'productdata' table
CREATE TABLE IF NOT EXISTS productdata (
    ID INT NOT NULL AUTO_INCREMENT,
    Product TEXT,
    Manufacturer TEXT,
    Model TEXT,
    Price INT,
    PRIMARY KEY (ID)
);

-- Insert sample data into the 'productdata' table
INSERT INTO productdata (Product, Manufacturer, Model, Price) VALUES
('Iphone', 'Apple', 'iPhone version 5', 999),
('S21', 'Samsung', 'S23', 899),
('Laptop', 'Dell', 'Inspiron 123', 1200),
('Tablet', 'HP', 'HP Ex 1', 1199),
('TV', 'LG', '42 HDTV', 699);
