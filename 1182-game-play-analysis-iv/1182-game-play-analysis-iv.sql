select round(numerator / denominator, 2) as fraction
from (select count(*) as numerator
from
(select *
from (select player_id, event_date, rank() over (partition by player_id order by event_date asc) as ranking
from activity) temp
where ranking = 1) a
right join
(select *
from (select player_id, event_date, rank() over (partition by player_id order by event_date asc) as ranking
from activity) temp_2
where ranking = 2) b
on a.player_id = b.player_id
where datediff(b.event_date, a.event_date) = 1) a
join
(select count(distinct(player_id)) as denominator
from activity) b