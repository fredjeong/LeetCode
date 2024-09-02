select round(100 * sum(if(order_date = customer_pref_delivery_date, 1, 0)) / count(*), 2) as immediate_percentage
from (select customer_id, order_date, customer_pref_delivery_date
from (select *, rank() over (partition by customer_id order by order_date asc) ranking
from delivery) temp
where ranking = 1) temp2