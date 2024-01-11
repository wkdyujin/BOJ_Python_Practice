select t1.food_type, t1.rest_id, t1.rest_name, t2.favorites
from rest_info t1
join    (select food_type, max(favorites) as favorites
        from rest_info
        group by food_type) t2
on t1.food_type = t2.food_type
where t1.favorites = t2.favorites
order by food_type desc;