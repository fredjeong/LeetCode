select user_id, ifnull(round((confirmed / (confirmed + timeout)), 2), 0) as confirmation_rate
from(
    select c.user_id, ifnull(c.confirmed, 0) as confirmed, ifnull(d.timeout, 0) as timeout
    from 
        (   select a.user_id, b.confirmed
            from signups a
            left join
            (   select user_id, count(*) as confirmed
                from confirmations
                where action = 'confirmed'
                group by user_id) b
            on a.user_id = b.user_id
        ) c
    left join
        (   select user_id, count(*) as timeout
            from confirmations
            where action = 'timeout'
            group by user_id
        ) d
    on c.user_id = d.user_id
) temp
