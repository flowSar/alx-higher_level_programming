-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT tv_show_genres.genre_id AS genre,
       COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
