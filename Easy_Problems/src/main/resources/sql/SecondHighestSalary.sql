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

--Solution (Failed)
-- SELECT NVL(Salary, to_number(null)) AS "SecondHighestSalary"
-- FROM (SELECT ROWNUM R, Salary
--       FROM (SELECT Salary FROM Employee ORDER BY Salary DESC) A
--       WHERE ROWNUM < 3) B
-- WHERE B.R > 1

--Solution2
SELECT MAX(SALARY) "SecondHighestSalary"
FROM EMPLOYEE
WHERE SALARY != (SELECT MAX(SALARY)
                 FROM EMPLOYEE)
