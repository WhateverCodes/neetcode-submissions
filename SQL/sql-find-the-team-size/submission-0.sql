-- Write your query below
select e.employee_id, count(*) over (partition by e.team_id) as team_size
from employee e;