-- Using the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Each record should display: tv_genres.name
-- Sorting by ascending order
SELECT g.`name` FROM `tv_genres` AS g INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id` INNER JOIN `tv_shows` AS t ON t.`id` = s.`show_id` WHERE t.`title` = "Dexter" ORDER BY g.`name`;
