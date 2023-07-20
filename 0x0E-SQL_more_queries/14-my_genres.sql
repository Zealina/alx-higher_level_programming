-- List all genres of the show 'Dexter'
-- Using the hbtn_0d_tvshows database
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter';
