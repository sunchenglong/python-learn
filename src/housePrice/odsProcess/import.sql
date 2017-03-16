select area, avg(totalPrice/square) as a from ods_house_new where dealDate < '2017.03.10' and dealDate > '2017.02.01' and (region = 'BJXC' or region = 'BJCP') and room < 20 group by area order by a;



select ta.area, ta.price, tb.dealNum
from (
    select area, avg(totalPrice/square) as price from ods_house_new
    where dealDate < '2017.03.10' and dealDate > '2017.02.01' and (region = 'BJXC' or region = 'BJCP') and room < 20
    group by area order by price
) as ta
left join (
    select distinct area, count(*) as dealNum from ods_house_new group by area
) as tb
on ta.area = tb.area


    select distinct area, count(*) as dealNum from ods_house_new group by area
