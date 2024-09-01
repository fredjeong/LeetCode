select a.id
from weather a right join weather b on date_sub(a.recordDate, interval 1 day) = b.recordDate
where a.id is not null and a.temperature > b.temperature
