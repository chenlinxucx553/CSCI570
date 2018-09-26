/**
 Write a SQL query to get the second highest salary from the Employee table.
 If there is no second highest salary, then the query should return null.
 */

CREATE TABLE Employee (
  ID     INT,
  Salary INT
);
TRUNCATE TABLE Employee;
INSERT INTO Employee (Id, Salary) VALUES ('1', '100');
INSERT INTO Employee (Id, Salary) VALUES ('2', '200');
INSERT INTO Employee (Id, Salary) VALUES ('3', '300');

--Solution
SELECT NVL(A.Salary, 'null') AS "SecondHighestSalary"
FROM (SELECT Salary
      FROM Employee
      ORDER BY Salary DESC) A
WHERE ROWNUM = 2;

SELECT NVL(Salary, 'null') AS "SecondHighestSalary"
FROM (SELECT DISTINCT
        Salary,
        DENSE_RANK()
        OVER (
          ORDER BY Salary DESC NULLS LAST ) AS Rank
      FROM Employee)
WHERE Rank = 2;
