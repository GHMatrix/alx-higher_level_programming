-- Listing all the shows in hbtn_0d_tvshows that have at least one genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id` FROM `tv_shows` AS s INNER JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id` ORDER BY s.`title`, g.`genre_id`;
