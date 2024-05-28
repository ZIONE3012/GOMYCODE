--create the customer_details database
CREATE DATABASE CUSTOMERDETAILSDB 
GO

--Access the new database
USE CUSTOMERDETAILSDB
GO

--Create tables for Customers
CREATE TABLE CUSTOMERS (
customer_id int PRIMARY KEY,
name varchar(20) NOT NULL,
address varchar(20) NOT NULL,
);
GO 

--create tables for Products
CREATE TABLE PRODUCTS (
product_id INT PRIMARY KEY,
name VARCHAR(20) NOT NULL,
Price DECIMAL(5,2) CHECK (Price >0) NOT NULL);


--create tables for orders
CREATE TABLE ORDERS (
order_id INT PRIMARY KEY,
customer_id INT FOREIGN KEY (customer_id) REFERENCES Customers (customer_id) NOT NULL,
product_id INT FOREIGN KEY (product_id) REFERENCES Products (product_id) NOT NULL,
quantity INT NOT NULL,
order_date DATE NOT NULL);
















