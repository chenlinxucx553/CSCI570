/**
Write a SQL query to find all duplicate emails in a table named Person.
 */

CREATE TABLE Person (
  Id    INT,
  Email VARCHAR(255)
);
TRUNCATE TABLE Person;
INSERT INTO Person (Id, Email) VALUES ('1', 'a@b.com');
INSERT INTO Person (Id, Email) VALUES ('2', 'c@d.com');
INSERT INTO Person (Id, Email) VALUES ('3', 'a@b.com');

/**
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
 */

--Solution1
SELECT EMAIL
FROM (SELECT EMAIL, COUNT(EMAIL) COUNTS FROM PERSON GROUP BY (EMAIL)) T
WHERE T.COUNTS > 1;

--Solution2
SELECT EMAIL FROM PERSON GROUP BY (EMAIL) HAVING COUNT(EMAIL) > 1;

--Solution3
SELECT DISTINCT A.EMAIL
FROM PERSON A
  JOIN PERSON B
    ON A.EMAIL = B.EMAIL
WHERE A.ID <> B.ID