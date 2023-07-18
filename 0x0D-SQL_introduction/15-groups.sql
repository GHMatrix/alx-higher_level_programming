-- Listing records with the same score in table named second_table.
-- Should display score, number of records and label number
-- in descending order
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
