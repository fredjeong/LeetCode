select a.name, b.bonus
from employee a left join bonus b on a.empId = b.empId
where b.bonus < 1000 or b.bonus is null