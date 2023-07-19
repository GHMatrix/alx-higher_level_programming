-- Listing all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_genres.name
SELECT t.`title`, g.`name` FROM `tv_shows` AS t LEFT JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id` LEFT JOIN `tv_genres` AS g ON s.`genre_id` = g.`id` ORDER BY t.`title`, g.`name`;
