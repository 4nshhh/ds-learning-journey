select * from items;
select * from variants;


select * , 
CONCAT(variant_name, " " , name) as full_name,
(price + variant_price) as final_price
from 
items cross join variants