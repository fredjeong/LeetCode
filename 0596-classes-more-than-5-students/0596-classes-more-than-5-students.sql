select class
from courses
group by class
having count(Student) >= 5