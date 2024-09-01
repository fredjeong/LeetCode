select product_id, ifnull(round(sum(price * units) / sum(units), 2), 0) as average_price
from (
    select a.product_id, a.price, ifnull(sum(b.units), 0) as units
    from prices a 
    left join unitssold b 
    on a.product_id = b.product_id and (b.purchase_date between a.start_date and a.end_date)
    group by a.product_id, a.start_date
) temp
group by product_id