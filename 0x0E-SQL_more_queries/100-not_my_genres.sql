--
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS dexter_genres ON tv_genres.id = dexter_genres.genre_id
WHERE dexter_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
