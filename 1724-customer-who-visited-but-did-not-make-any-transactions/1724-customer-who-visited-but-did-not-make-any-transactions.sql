select a.customer_id, count(a.visit_id) as count_no_trans
from visits a left join transactions b on a.visit_id = b.visit_id
where b.transaction_id is null
group by customer_id