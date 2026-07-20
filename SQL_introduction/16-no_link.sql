-- List records of second_table where name is not NULL, showing score and name, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
