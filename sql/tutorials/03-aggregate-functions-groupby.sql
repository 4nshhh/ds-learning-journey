SELECT * FROM movies;
SELECT COUNT(*) FROM movies WHERE industry = "Hollywood";
SELECT AVG(imdb_rating) as avg_rating FROM movies;
SELECT MIN(imdb_rating) as min_rating FROM movies;
SELECT MAX(imdb_rating) as min_rating FROM movies 
WHERE industry = "BOLLYWOOD";

SELECT MIN(imdb_rating) as min_rating,
		MAX(imdb_rating) as max_rating ,
        AVG(imdb_rating) as avg_rating 
        FROM movies;
        
SELECT industry, COUNT(*) AS movie FROM movies GROUP BY industry;

