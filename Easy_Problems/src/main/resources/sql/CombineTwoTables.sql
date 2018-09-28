/**
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.


Write a SQL query for a report that provides the following information for each person in the Person table,
regardless if there is an address for each of those people:

FirstName, LastName, City, State
 */


CREATE TABLE Person (
  PersonId  INT,
  FirstName VARCHAR(255),
  LastName  VARCHAR(255)
);
CREATE TABLE Address (
  AddressId INT,
  PersonId  INT,
  City      VARCHAR(255),
  State     VARCHAR(255)
);
TRUNCATE TABLE Person;
INSERT INTO Person (PersonId, LastName, FirstName) VALUES ('1', 'Wang', 'Allen');
TRUNCATE TABLE Address;
INSERT INTO Address (AddressId, PersonId, City, State) VALUES ('1', '2', 'New York City', 'New York');

--Solution

SELECT
  A.FirstName,
  A.LastName,
  B.City,
  B.State
FROM Person A LEFT JOIN Address B ON A.PersonId = B.PersonId