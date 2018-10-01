/**
Given a Weather table, write a SQL query to find
all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+
 */

CREATE TABLE Weather (
  ID          INT,
  RecordDate  DATE,
  Temperature INT
);
TRUNCATE TABLE Weather;
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('1', to_date('2015-01-01', 'yyyy-mm-dd'), '10');
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('2', to_date('2015-01-02', 'yyyy-mm-dd'), '25');
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('3', to_date('2015-01-03', 'yyyy-mm-dd'), '20');
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('4', to_date('2015-01-04', 'yyyy-mm-dd'), '30');

--Solution(Oracle)
SELECT B.ID
FROM WEATHER A
  INNER JOIN WEATHER B
    ON A.RECORDDATE + 1 = B.RECORDDATE
WHERE A.TEMPERATURE < B.TEMPERATURE


