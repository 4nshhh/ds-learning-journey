SELECT * FROM movies WHERE imdb_rating >= 9;
SELECT * FROM movies WHERE imdb_rating BETWEEN 7 AND 8;
SELECT * FROM movies WHERE release_year = 2022 OR release_year = 2017 OR release_year = 2018;
SELECT * FROM movies WHERE release_year in (2022,2017,2018);
SELECT * FROM movies WHERE imdb_rating IS NULL;
SELECT * FROM movies WHERE imdb_rating IS NOT NULL;
SELECT * FROM movies WHERE industry = "Hollywood" ORDER BY imdb_rating DESC;
SELECT * FROM movies WHERE industry = "Hollywood" ORDER BY imdb_rating DESC LIMIT 5;
SELECT * FROM movies WHERE industry = "Hollywood" ORDER BY imdb_rating DESC LIMIT 5 OFFSET 1;