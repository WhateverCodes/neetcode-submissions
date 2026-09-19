-- Write your query below
select e.event_day as day, e.emp_id, sum(e.out_time - e.in_time) as total_time
from employees e
group by emp_id, event_day