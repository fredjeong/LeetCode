(select employee_id, department_id
from employee
group by employee_id
having count(department_id) = 1)
union all
(select employee_id, department_id
from employee
where primary_flag = 1
group by employee_id)