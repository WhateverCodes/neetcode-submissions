-- Write your query below
select p.first_name, p.last_name, a.city, a.state
from person as p left join address as a using (person_id);