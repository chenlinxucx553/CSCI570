/**
The Employee table holds all employees including their managers.
Every employee has an Id, and there is also a column for the manager Id.
 */


CREATE TABLE Employee (
  ID        INT,
  NAME      VARCHAR(255
            ),
  Salary    INT,
  ManagerId INT
);
TRUNCATE TABLE Employee;
INSERT INTO Employee (Id, Name, Salary, ManagerId) VALUES ('1', 'Joe', '70000', '3');
INSERT INTO Employee (Id, Name, Salary, ManagerId) VALUES ('2', 'Henry', '80000', '4');
INSERT INTO Employee (Id, Name, Salary, ManagerId) VALUES ('3', 'Sam', '60000', NULL);
INSERT INTO Employee (Id, Name, Salary, ManagerId) VALUES ('4', 'Max', '90000', NULL);

/**
Given the Employee table, write a SQL query that finds out employees who earn more than their managers.
For the above table, Joe is the only employee who earns more than his manager.
 */

SELECT WORKER.NAME AS "Employee"
FROM EMPLOYEE MANAGER
  INNER JOIN (SELECT * FROM EMPLOYEE WHERE MANAGERID IS NOT NULL) WORKER
    ON WORKER.MANAGERID = MANAGER.ID
WHERE WORKER.SALARY > MANAGER.SALARY