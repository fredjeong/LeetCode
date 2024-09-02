select product_id, year as first_year, quantity, price
from (select *, rank() over (partition by product_id order by year) as ranking
from sales) temp
where ranking = 1