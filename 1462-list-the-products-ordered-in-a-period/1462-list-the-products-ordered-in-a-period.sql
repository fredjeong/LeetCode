select a.product_name, b.unit
from products a
join (
    select product_id, sum(unit) as unit
    from orders
    where date_format(order_date, '%Y-%m-%d') like '2020-02-%'
    group by product_id
    having sum(unit) >= 100
    ) b
on a.product_id = b.product_id