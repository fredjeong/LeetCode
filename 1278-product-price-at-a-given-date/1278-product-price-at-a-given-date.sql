select a.product_id, ifnull(new_price, 10) as price
from 
    (
        select distinct(product_id) 
        from products 
        order by product_id
    ) a
left join
    (
        select product_id, new_price
        from products
        where (product_id, change_date) in (
            select product_id, max(change_date) 
            from products 
            where change_date <= '2019-08-16' 
            group by product_id)
        group by product_id
    ) b 
on a.product_id = b.product_id