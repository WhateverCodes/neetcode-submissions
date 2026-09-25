-- Write your query below
select distinct c.title
from tv_program t
join
content c
on t.content_id = c.content_id
where kids_content = 'Y' and content_type = 'Movies'
and t.program_date like '2020-06%';