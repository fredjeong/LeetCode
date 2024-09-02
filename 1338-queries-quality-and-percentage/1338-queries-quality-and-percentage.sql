select query_name, round(avg(rating/position), 2) as quality, round(100 * sum(if(rating >= 3, 0, 1)) / count(rating), 2) as poor_query_percentage
from queries
where query_name is not null
group by query_name