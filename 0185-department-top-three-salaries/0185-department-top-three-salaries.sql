select b.name as Department, a.name as Employee, a.Salary
from (
    select *
    from (
        select *, dense_rank() over (partition by departmentid order by salary desc) as ranking
        from employee
    ) temp
    where ranking <= 3) a 
join department b 
on a.departmentid = b.id