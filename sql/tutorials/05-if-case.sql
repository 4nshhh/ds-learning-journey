select * from financials;

select *, (revenue - budget) as profit from financials;

select * , if(currency = "USD",revenue*80, revenue) as revenue_inr from financials;

select * , 
case 
	when unit = "Billions" then revenue*1000
    when unit = "thousands" then revenue/1000
    else revenue
end
as revenue_mln
 from financials;

