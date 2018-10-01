/**
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:

Your output is the whole Person table after executing your sql. Use delete statement.
 */

--Solution(ORACLE)
DELETE FROM PERSON
WHERE ID = (SELECT MAX(ID)
            FROM PERSON A
              JOIN (SELECT
                      EMAIL,
                      COUNT(EMAIL)
                    FROM PERSON T
                    GROUP BY EMAIL
                    HAVING COUNT(EMAIL) > 1) B
                ON A.EMAIL = B.EMAIL)


--Solution(Mysql)
DELETE p1 FROM Person p1,
Person p2
WHERE
p1.Email = p2.Email AND p1.Id > p2.Id

