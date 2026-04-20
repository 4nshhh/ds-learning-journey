select * from movies;
select * from financials;


select m.movie_id, title, budget, revenue, currency, unit,
case 
	when unit = "Thousands" then (revenue-budget)/1000
    when unit = "Billions" then (revenue-budget)*1000
    else (revenue - budget)
end as profit_mln
from movies m 
join financials f
on m.movie_id = f.movie_id
where industry = "bollywood"
order by profit_mln desc;