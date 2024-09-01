select machine_id, round(avg(processing_time), 3) as processing_time
from
(select start.machine_id, end.timestamp - start.timestamp as processing_time
from (select machine_id, process_id, timestamp from activity where activity_type = 'start') start
join (select machine_id, process_id, timestamp from activity where activity_type = 'end') end
on start.machine_id = end.machine_id and start.process_id = end.process_id) merged
group by machine_id