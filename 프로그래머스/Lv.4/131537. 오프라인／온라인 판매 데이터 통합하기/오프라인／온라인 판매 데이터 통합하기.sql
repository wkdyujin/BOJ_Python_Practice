select date_format(t.sales_date, "%Y-%m-%d"), t.product_id, t.user_id, t.sales_amount
from (select sales_date, product_id, user_id,sales_amount
    from online_sale as onn
    where YEAR(sales_date) = 2022 and month(sales_date) = 3
    union
    select sales_date, product_id, null as user_id, sales_amount
    from offline_sale as off
    where year(sales_date) = 2022 and month(sales_date) = 3) as t
order by sales_date, product_id, user_id;