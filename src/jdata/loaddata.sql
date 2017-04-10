load data infile '/tmp/file.csv' into table _tablename (set character utf8)
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n';


create table jdata.user_action (
user_id int(20),
sku_id int(20),
time_str DATETIME,
model_id int(10),
type int(10),
cate int(10),
brand int(10),
primary key (user_id, sku_id, time_str)
)

user_id,sku_id,time,model_id,type,cate,brand


load data infile 'JData_Action_201604.csv' into table  jdata.user_action (set character utf8)
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n';