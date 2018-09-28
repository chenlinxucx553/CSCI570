/**
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
 */

CREATE TABLE Customers (
  Id   INT,
  Name VARCHAR(255)
);
CREATE TABLE Orders (
  Id         INT,
  CustomerId INT
);
TRUNCATE TABLE Customers;
INSERT INTO Customers (Id, Name) VALUES ('1', 'Joe');
INSERT INTO Customers (Id, Name) VALUES ('2', 'Henry');
INSERT INTO Customers (Id, Name) VALUES ('3', 'Sam');
INSERT INTO Customers (Id, Name) VALUES ('4', 'Max');
TRUNCATE TABLE Orders;
INSERT INTO Orders (Id, CustomerId) VALUES ('1', '3');
INSERT INTO Orders (Id, CustomerId) VALUES ('2', '1');

--Solution
SELECT NAME AS "Customers"
FROM CUSTOMERS
WHERE ID NOT IN (SELECT DISTINCT (CUSTOMERID) FROM ORDERS)
