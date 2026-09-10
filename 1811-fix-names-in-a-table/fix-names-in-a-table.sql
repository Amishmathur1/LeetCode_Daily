-- Write your PostgreSQL query statement below

SELECT user_id, UPPER(LEFT(name, 1)) || LOWER(SUBSTRING(name, 2)) AS name
FROM users
ORDER BY user_id;