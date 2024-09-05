select if(count(*) = 0, null, salary) as SecondHighestSalary
from (select *, dense_rank() over (order by salary desc) as ranking
from employee) temp
where ranking = 2