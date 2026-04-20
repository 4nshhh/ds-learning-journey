select * from movies;
select * from financials;

-- Inner JOIN 
select m.movie_id, title, budget, revenue, unit 
from movies m 
join 
financials f
on m.movie_id = f.movie_id;

-- Outer JOINS

-- LEFT JOIN

select m.movie_id, title, budget, revenue, unit 
from movies m 
left join 
financials f
on m.movie_id = f.movie_id;

-- RIGHT JOIN 

select f.movie_id, title, budget, revenue, unit 
from movies m 
right join 
financials f
on m.movie_id = f.movie_id;

-- FULL JOIN 

select m.movie_id, title, budget, revenue, unit from movies m 
left join financials f on m.movie_id = f.movie_id
UNION 
select f.movie_id, title, budget, revenue, unit from movies m 
right join financials f on m.movie_id = f.movie_id;

-- Using Clause : Works when we have same primary key

select movie_id, title, budget, revenue, unit 
from movies 
join financials 
using (movie_id)