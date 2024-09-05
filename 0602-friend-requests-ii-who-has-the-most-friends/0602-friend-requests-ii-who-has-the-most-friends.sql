with temp as (
    select id, sum(num) as num
    from (
        select requester_id as id, count(requester_id) as num
        from requestaccepted
        group by requester_id
        union all
        select accepter_id as id, count(accepter_id) as num
        from requestaccepted
        group by accepter_id
    ) merged
    group by id
)

select id, num
from temp
inner join
(
    select max(num) as maxnum
    from temp
) maxnum
where num = maxnum