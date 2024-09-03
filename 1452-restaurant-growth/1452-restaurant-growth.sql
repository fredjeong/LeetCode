with customer_modified as (
    select visited_on, sum(amount) as amount
    from customer
    group by visited_on
)

select visited_on, amount, average_amount
from (
    select  visited_on, 
            sum(amount) over (order by visited_on asc rows between 6 preceding and current row) as 'amount', 
            round(avg(amount) over (order by visited_on asc rows between 6 preceding and current row), 2) as 'average_amount'
    from customer_modified) temp
where date_sub(visited_on, interval 6 day) in (select visited_on from customer_modified)
order by visited_on asc