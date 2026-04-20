select * from movies;
select * from movie_actor;
select * from actors;

select a.name, GROUP_CONCAT(m.title) as movies from movies m 
join movie_actor ma on m.movie_id = ma.movie_id
join actors a on a.actor_id = ma.actor_id
group by a.name;