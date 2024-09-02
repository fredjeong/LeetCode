select class
from (select class, count(student) as count
from courses
group by class) temp
where count >= 5