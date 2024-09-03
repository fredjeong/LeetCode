# user who has rated the greatest number of movies
(select a.name as results
from users a join movierating b on a.user_id = b.user_id
group by a.user_id
order by count(b.rating) desc, a.name asc
limit 1)
union all
# movie name with the highest rating in feb 2020
(select a.title as results
from movies a join movierating b on a.movie_id = b.movie_id
where b.created_at like '2020-02-%'
group by a.movie_id
order by avg(b.rating) desc, a.title asc
limit 1)