-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows as s
INNER JOIN tv_show_genres g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id

