with temp as (
    select pid, tiv_2015, tiv_2016, concat(lat, ', ', lon) as coordinate 
    from insurance
)

select round(sum(tiv_2016),2) as tiv_2016
from insurance
where pid in (
    select pid 
    from insurance 
    where tiv_2015 in (
        select tiv_2015 
        from insurance 
        group by tiv_2015 
        having count(tiv_2015) > 1)
    ) 
and pid in (
    select pid
    from temp
    group by coordinate
    having count(coordinate) = 1
    )