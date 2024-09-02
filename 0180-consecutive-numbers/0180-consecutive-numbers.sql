select distinct(num) as ConsecutiveNums
from (select c.id, c.num, c.id_2, c.num_2, d.id as id_3, d.num as num_3
from
((select a.id, a.num, b.id as id_2, b.num as num_2
from logs a join logs b on a.id + 1 = b.id) c
join 
logs d 
on c.id + 2 = d.id and c.id_2 + 1 = d.id)) temp
where num = num_2 and num_2 = num_3