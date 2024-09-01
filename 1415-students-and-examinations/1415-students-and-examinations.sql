select c.student_id, c.student_name, c.subject_name, ifnull(d.attended_exams, 0) as attended_exams
from (
        select a.student_id, a.student_name, b.subject_name
        from students a inner join subjects b
        order by a.student_id, b.subject_name
    ) c 
    left join 
    (
        select *, count(*) as attended_exams
        from examinations
        group by student_id, subject_name
    ) d 
    on c.student_id = d.student_id and c.subject_name = d.subject_name
group by c.student_id, c.subject_name
order by c.student_id, c.subject_name