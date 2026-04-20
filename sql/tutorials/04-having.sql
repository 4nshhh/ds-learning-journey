-- Print all the years where more than 2 movies were released 

select release_year, count(*) as movies_count 
from movies
group by release_year
having movies_count > 2
order by movies_count desc;

-- Remeber the sequence 
-- From --> Where --> Group by --> Having --> Order by